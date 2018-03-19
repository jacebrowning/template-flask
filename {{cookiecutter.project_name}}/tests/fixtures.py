# pylint: disable=redefined-outer-name

import pytest

from {{cookiecutter.project_name}}.settings import get_config
from {{cookiecutter.project_name}}.factory import create_app


@pytest.fixture
def app():
    return create_app(get_config('test'))


@pytest.fixture
def client(app):
    return app.test_client()
