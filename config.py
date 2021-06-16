import os

class Config:
    SECRET_KEY = 'monkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost:5433/firstimpression'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'reilly.oduory@student.moringaschool.com'
    MAIL_PASSWORD = 'BitchIcode'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}