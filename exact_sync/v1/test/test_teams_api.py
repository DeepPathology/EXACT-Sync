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
from api.teams_api import TeamsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_team(self):
        """Test case for create_team

        """
        pass

    def test_destroy_team(self):
        """Test case for destroy_team

        """
        pass

    def test_list_teams(self):
        """Test case for list_teams

        """
        pass

    def test_partial_update_team(self):
        """Test case for partial_update_team

        """
        pass

    def test_retrieve_team(self):
        """Test case for retrieve_team

        """
        pass

    def test_update_team(self):
        """Test case for update_team

        """
        pass


if __name__ == '__main__':
    unittest.main()
