# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.element import Element  # noqa: E501
from swagger_server.models.element_input import ElementInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_elements_post(self):
        """Test case for elements_post

        Insert an element
        """
        body = ElementInput()
        response = self.client.open(
            '/elements',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_elements_status60_get(self):
        """Test case for elements_status60_get

        Get elements with status=60
        """
        response = self.client.open(
            '/elements/status-60',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
