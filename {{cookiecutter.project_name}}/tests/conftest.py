"""Integration tests configuration file."""

from {{cookiecutter.project_name}}.tests.conftest import pytest_configure  # pylint: disable=unused-import

from .fixtures import *  # pylint: disable=wildcard-import,unused-wildcard-import
