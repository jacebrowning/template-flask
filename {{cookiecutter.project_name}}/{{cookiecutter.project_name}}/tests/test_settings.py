# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect

from {{cookiecutter.project_name}}.settings import get_config


def describe_get_config():

    def when_valid():
        config = get_config('production')
        expect(config.ENV) == 'production'

    def when_extended():
        config = get_config('staging')
        expect(config.ENV) == 'staging'

    def when_empty():
        with expect.raises(AssertionError):
            get_config('')

    def when_unknown():
        with expect.raises(AssertionError):
            get_config('unknown')
