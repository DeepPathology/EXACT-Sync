# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.images_api import ImagesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestImagesApi(unittest.TestCase):
    """ImagesApi unit test stubs"""

    def setUp(self):
        self.api = api.images_api.ImagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_image(self):
        """Test case for create_image

        """
        pass

    def test_destroy_image(self):
        """Test case for destroy_image

        """
        pass

    def test_list_images(self):
        """Test case for list_images

        """
        pass

    def test_partial_update_image(self):
        """Test case for partial_update_image

        """
        pass

    def test_retrieve_image(self):
        """Test case for retrieve_image

        """
        pass

    def test_update_image(self):
        """Test case for update_image

        """
        pass


if __name__ == '__main__':
    unittest.main()
