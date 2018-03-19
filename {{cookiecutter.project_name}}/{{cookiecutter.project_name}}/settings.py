import os


class Config:
    """Base configuration."""

    ENV = None

    PATH = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(PATH)
    DEBUG = False
    THREADED = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'

    DEBUG = True
    TESTING = True
    SECRET_KEY = ENV


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'

    DEBUG = True
    SECRET_KEY = ENV


def get_config(name):
    assert name, "No configuration specified"

    for config in Config.__subclasses__():
        if config.ENV == name:
            return config

    assert False, "No matching configuration"
    return None
