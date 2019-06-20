class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PROFILE = False

    PORT = 5000

    # Swagger
    SWAGGER_UI_OPERATION_ID = True
    SWAGGER_UI_REQUEST_DURATION = True
    SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_MASK_SWAGGER = False

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = 'mysql://test:test@mariadb/wanted?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PROFILE = True

    # SQLALCHEMY for test
    SQLALCHEMY_DATABASE_URI = 'mysql://test:test@mariadb/wanted_test?charset=utf8'


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    PROFILE = False
