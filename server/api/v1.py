from flask import Blueprint
from flask_restplus import Api, Resource, reqparse, Model, fields

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
    parser.add_argument('search_word', type=str, location='args', help='회사명 ex) 원티드랩')
    parser.add_argument('tags', type=str, location='args', help='태그 ex) tag1|tag2|tag3')

    # GET return
    company_detail = company_ns.model('CompanyDetail', {
        'id': fields.Integer(description='회사 아이디'),
        'name_ko': fields.String,
        'name_en': fields.String,
        'name_ja': fields.String,
        'tag_ko': fields.String,
        'tag_en': fields.String,
        'tag_ja': fields.String,
    })
    company_list = company_ns.model('CompanyList', {
        'companies': fields.List(fields.Nested(company_detail))
    })

    @company_ns.doc(
        description='회사명 혹은 태그로 회사를 검색할 수 있습니다.'
    )
    @company_ns.expect(parser)
    @company_ns.marshal_with(company_list)
    def get(self):
        pass


