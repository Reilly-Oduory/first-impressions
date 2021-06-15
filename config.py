import os

class Config:
    SECRET_KEY = 'monkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost:5433/firstimpression'
    SIMPLEMDE_JS_LIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}