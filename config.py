# config.py

class Config(object):
    DEBUG = False
    # Outras configurações gerais

class DevelopmentConfig(Config):
    DEBUG = True
    # Configurações específicas para ambiente de desenvolvimento
    DATABASE_URI = 'postgresql://rafael/banco_de_dados'

class ProductionConfig(Config):
    DEBUG = False
    # Configurações específicas para ambiente de produção
    DATABASE_URI = 'postgresql://rafael/banco_de_dados'
