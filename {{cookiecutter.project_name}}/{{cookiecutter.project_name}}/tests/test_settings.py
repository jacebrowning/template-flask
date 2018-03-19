# pylint: disable=unused-variable,expression-not-assigned

from expecter import expect

from {{cookiecutter.project_name}}.settings import get_config


def describe_get_config():

    def when_valid():
        config = get_config('prod')
        expect(config.ENV) == 'prod'

    def when_empty():
        with expect.raises(AssertionError):
            get_config('')

    def when_unknown():
        with expect.raises(AssertionError):
            get_config('unknown')
