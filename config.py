# config.py

class Config(object):
    DEBUG = False
    # Outras configurações gerais

class DevelopmentConfig(Config):
    DEBUG = True
    # Configurações específicas para ambiente de desenvolvimento
    DATABASE_HOST = 'localhost'
    DATABASE_USER = 'rafael'
    DATABASE_PASSWORD = 'nova_senha'
    DATABASE_NAME = 'banco_de_dados'
class ProductionConfig(Config):
    DEBUG = False
    # Configurações específicas para ambiente de produção
    DATABASE_HOST = 'dpg-ciqkhe6nqql4qa7csi10-a.oregon-postgres.render.com'
    DATABASE_USER = 'rafael'
    DATABASE_PASSWORD = 'PuObkrabERkdbxhSFmGtAuXTum4fTjr5'
    DATABASE_NAME = 'banco_de_dados_rvj4'