from flask import Blueprint
from flask_restplus import Api, Resource, fields, reqparse
from sqlalchemy import or_

from server.api.serializers import response_serializer
from server.models.mariadb import Company, db

v1 = Blueprint('api_v1', __name__)
v1_api = Api(
    v1,
    version='1.0',
    title='Wanted-test: API',
    description='Wanted의 coding assessment를 위한 API DOC 페이지 입니다.'
)

company_ns = v1_api.namespace('company', description='URL Pattern : /apis/v1/company/~')


@company_ns.route('/<int:company_id>/tags', endpoint='company_tags_api')
class CompanyTagsApi(Resource):
    parser = reqparse.RequestParser()

    # PUT & DELETE
    parser.add_argument('tag_ko', type=str, location='form', help='한글 태그 ex) 태그_4|태그_20|태그_16')
    parser.add_argument('tag_en', type=str, location='form', help='영문 태그 ex) tag_4|tag_20|tag_16')
    parser.add_argument('tag_ja', type=str, location='form', help='일본어 태그 ex) タグ_4|タグ_20|タグ_16')

    add_company_tags = company_ns.clone('AddCompanyTags', response_serializer, {})

    @company_ns.doc(
        responses={
            204: 'No Content',
            400: 'Validation Error',
            500: 'Server Error'
        },
        description='회사 태그정보 추가'
    )
    @company_ns.expect(parser)
    @company_ns.marshal_with(add_company_tags)
    def put(self, company_id):
        args = self.parser.parse_args()
        tag_ko = args.get('tag_ko').split('|') if args.get('tag_ko') else []
        tag_en = args.get('tag_en').split('|') if args.get('tag_en') else []
        tag_ja = args.get('tag_ja').split('|') if args.get('tag_ja') else []

        try:
            company = Company.query.filter(Company.id == company_id).first()
            if not company:
                return dict(success=False, reason='NoCompanyFound'), 404, dict()
            if tag_ko:
                prev_tag_ko = company.tag_ko.split('|') if company.tag_ko else []
                updated_tag_ko = '|'.join(list(dict.fromkeys(prev_tag_ko + tag_ko)))
                company.tag_ko = updated_tag_ko
            if tag_en:
                prev_tag_en = company.tag_en.split('|') if company.tag_en else []
                updated_tag_en = '|'.join(list(dict.fromkeys(prev_tag_en + tag_en)))
                company.tag_en = updated_tag_en
            if tag_ja:
                prev_tag_ja = company.tag_ja.split('|') if company.tag_ja else []
                updated_tag_ja = '|'.join(list(dict.fromkeys(prev_tag_ja + tag_ja)))
                company.tag_ja = updated_tag_ja

            db.session.commit()

            return dict(success=True, reason='SUCCESS'), 200, dict()
        except Exception as e:
            print(e)
            return dict(success=False, reason='ServerError'), 500, dict()

    delete_company_tags = company_ns.clone('DeleteCompanyTags', response_serializer, {})

    @company_ns.doc(
        responses={
            204: 'No Content',
            400: 'Validation Error',
            500: 'Server Error'
        },
        description='회사 태그정보 삭제'
    )
    @company_ns.expect(parser)
    @company_ns.marshal_with(delete_company_tags)
    def delete(self, company_id):
        args = self.parser.parse_args()
        tag_ko = args.get('tag_ko').split('|') if args.get('tag_ko') else []
        tag_en = args.get('tag_en').split('|') if args.get('tag_en') else []
        tag_ja = args.get('tag_ja').split('|') if args.get('tag_ja') else []

        try:
            company = Company.query.filter(Company.id == company_id).first()
            if not company:
                return dict(success=False, reason='NoCompanyFound'), 404, dict()
            if tag_ko:
                prev_tag_ko = company.tag_ko.split('|') if company.tag_ko else []
                updated_tag_ko = '|'.join([tag for tag in prev_tag_ko if tag not in tag_ko])
                company.tag_ko = updated_tag_ko
            if tag_en:
                prev_tag_en = company.tag_en.split('|') if company.tag_en else []
                updated_tag_en = '|'.join([tag for tag in prev_tag_en if tag not in tag_en])
                company.tag_en = updated_tag_en
            if tag_ja:
                prev_tag_ja = company.tag_ja.split('|') if company.tag_ja else []
                updated_tag_ja = '|'.join([tag for tag in prev_tag_ja if tag not in tag_ja])
                company.tag_ja = updated_tag_ja

            db.session.commit()

            return dict(success=True, reason='SUCCESS'), 200, dict()
        except Exception as e:
            print(e)
            return dict(success=False, reason='ServerError'), 500, dict()


@company_ns.route('/search', endpoint='company_search_api')
class CompanySearchApi(Resource):
    parser = reqparse.RequestParser()

    # GET
    parser.add_argument('search_word', type=str, location='args', help='회사명 ex) 원티드랩')
    parser.add_argument('tags', type=str, location='args', help='태그 ex) tag1|tag2|tag3')

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
        responses={
            400: 'Validation Error',
            500: 'Server Error'
        },
        description='회사명 혹은 태그로 회사를 검색할 수 있습니다.'
    )
    @company_ns.expect(parser)
    @company_ns.marshal_with(company_list)
    def get(self):
        args = self.parser.parse_args()
        search_word = args.get('search_word')
        tags = args.get('tags')
        tags = tags.split('|') if tags else []

        if not search_word and not tags:
            return dict(success=False,
                        reason='ParamsMissing',
                        companies=[]), 400, dict()

        try:
            company_query = Company.query
            query_filter = []
            if search_word:
                query_filter.append(or_(Company.name_ko.contains(search_word),
                                        Company.name_en.contains(search_word),
                                        Company.name_ja.contains(search_word)))
            if tags:
                company_tag_ko_filter = [Company.tag_ko.contains(tag) for tag in tags]
                company_tag_en_filter = [Company.tag_en.contains(tag) for tag in tags]
                company_tag_ja_filter = [Company.tag_ja.contains(tag) for tag in tags]

                query_filter.append(or_(*company_tag_ko_filter,
                                        *company_tag_en_filter,
                                        *company_tag_ja_filter))
            if query_filter:
                company_query = company_query.filter(or_(*query_filter))
            companies = company_query.all()

            return dict(success=True,
                        reason='SUCCESS',
                        companies=[
                            dict(
                                id=company.id,
                                name_ko=company.name_ko,
                                name_en=company.name_en,
                                name_ja=company.name_ja,
                                tag_ko=company.tag_ko,
                                tag_en=company.tag_en,
                                tag_ja=company.tag_ja
                            ) for company in companies]), 200, dict()
        except Exception as e:
            print(e)
            return dict(success=False,
                        reason='ServerError',
                        companies=[]), 500, dict()
