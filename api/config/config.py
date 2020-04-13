from src.credentials import DB_PASSWORD, DB_USER, FLASK_SECRET_KEY as secret_key, FLASK_SECURITY_PASSWORD_SALT as salt, MAIL_USERNAME as mail_usrname, MAIL_PASSWORD as mail_pswd


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secret_key
    SECURITY_PASSWORD_SALT = salt
    MAIL_DEFAULT_SENDER = mail_usrname
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = mail_usrname
    MAIL_PASSWORD = mail_pswd
    UPLOAD_FOLDER = 'static\images'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:3306/api_prod'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:3306/api_dev'
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:3306/api_test'
    SQLALCHEMY_ECHO = True
