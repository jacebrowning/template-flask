# pylint: disable=unused-variable,unused-argument,expression-not-assigned,singleton-comparison

import pytest
from expecter import expect

from .utils import load


def describe_root():

    def describe_index():

        @pytest.fixture
        def url():
            return "/api"

        def describe_GET():

            def it_returns_metadata(client, url):
                status, content = load(client.get(url))

                expect(status) == 200
                expect(content) == {
                    '_links': {
                        'self': "http://localhost/api",
                        'collections': "http://localhost/api/collections/",
                        'redirects': "http://localhost/api/redirects/",
                    }
                }

        def redirects_with_slash(client, url):
            status, content = load(client.get(url + "/"))

            expect(status) == 302
