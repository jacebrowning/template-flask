# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned

from . import user


def describe_index():

    def it_renders_a_browsable_api(expect):
        user.visit("/api")

        expect(user.browser.title) == "Flask API"
