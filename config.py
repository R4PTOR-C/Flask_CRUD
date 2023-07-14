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
    DATABASE_URI = 'postgresql://rafael:kYZA6JXz9KKleygUmD4zJb3EMcyBjsO0@dpg-cinvestgkuvudi9v5370-a:5432/banco_de_dados_odbf'
