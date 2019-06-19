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

    # Mongodb
    MONGO_DB = "mongodb://mongodb:27017/"


class TestConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PROFILE = True


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    PROFILE = False
