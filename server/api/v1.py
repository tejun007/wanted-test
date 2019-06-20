from flask import Blueprint
from flask_restplus import Api, Resource, fields, reqparse
from sqlalchemy import or_, and_

from server.api.serializers import response_serializer
from server.models.mariadb import Company

v1 = Blueprint('api_v1', __name__)
v1_api = Api(
    v1,
    version='1.0',
    title='Wanted-test: API',
    description='Wanted의 coding assessment를 위한 API DOC 페이지 입니다.'
)

company_ns = v1_api.namespace('company', description='URL Pattern : /apis/v1/company/~')


@company_ns.route('/search')
class CompanySearchApi(Resource):
    parser = reqparse.RequestParser()

    # GET
    parser.add_argument('search_word', type=str, location='args', default='', help='회사명 ex) 원티드랩')
    parser.add_argument('tags', type=str, location='args', default='', help='태그 ex) tag1|tag2|tag3')

    # GET return models
    company_detail = company_ns.model('CompanyDetail', {
        'id': fields.Integer(description='회사 아이디'),
        'name_ko': fields.String,
        'name_en': fields.String,
        'name_ja': fields.String,
        'tag_ko': fields.String,
        'tag_en': fields.String,
        'tag_ja': fields.String,
    })
    company_list = company_ns.clone('CompanyList', response_serializer, {
        'companies': fields.List(fields.Nested(company_detail))
    })

    @company_ns.doc(
        description='회사명 혹은 태그로 회사를 검색할 수 있습니다.'
    )
    @company_ns.expect(parser)
    @company_ns.marshal_with(company_list)
    def get(self):
        args = self.parser.parse_args()
        search_word = args.get('search_word')
        tags = args.get('tags')
        print(search_word)
        print(tags)
        if tags:
            tags = tags.split('|')
        companies = Company.query \
            .filter(or_(Company.name_ko.contains(search_word),
                        Company.name_en.contains(search_word),
                        Company.name_ja.contains(search_word)),
                    or_(Company.tag_ko.contains(tags),
                        Company.tag_en.contains(tags),
                        Company.tag_ja.contains(tags))).all()
        print('companies', companies)
        return dict(success=True,
                    reason='SUCCESS',
                    companies=[]), 200, dict()
