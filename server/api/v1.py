from flask import Blueprint
from flask_restplus import Api

v1 = Blueprint('api_v1', __name__)
v1_api = Api(
    v1,
    version='1.0',
    title='Wanted-test: API',
    description='Wanted의 coding assessment를 위한 API DOC 페이지 입니다.'
)

