import os


class Config:

    ENV = None

    PATH = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(PATH)
    DEBUG = False
    THREADED = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProductionConfig(Config):

    ENV = 'production'


class StagingConfig(ProductionConfig):

    ENV = 'staging'


class LocalConfig(Config):

    ENV = 'local'

    DEBUG = True
    SECRET_KEY = ENV


class TestConfig(LocalConfig):

    ENV = 'test'

    TESTING = True
    SECRET_KEY = ENV


def get_config(name):
    assert name, "No configuration specified"

    for config in Config.__subclasses__():
        if config.ENV == name:
            return config

    assert False, "No matching configuration"
    return None
