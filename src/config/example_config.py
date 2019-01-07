class ExampleConfig():
    DEBUG = False
    SECRET_KEY = 'secret_key'
    SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:db_password@localohost/catalog_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False