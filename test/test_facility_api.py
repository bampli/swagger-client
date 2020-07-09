# coding: utf-8

"""
    bampli-api

    The API for the Business Amplifier project.  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.facility_api import FacilityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFacilityApi(unittest.TestCase):
    """FacilityApi unit test stubs"""

    def setUp(self):
        self.api = api.facility_api.FacilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_facility(self):
        """Test case for add_facility

        Create a new Facility  # noqa: E501
        """
        pass

    def test_add_wip(self):
        """Test case for add_wip

        Create a new Wip  # noqa: E501
        """
        pass

    def test_delete_facility(self):
        """Test case for delete_facility

        Delete a Facility  # noqa: E501
        """
        pass

    def test_delete_wip(self):
        """Test case for delete_wip

        Delete a Wip  # noqa: E501
        """
        pass

    def test_get_facility(self):
        """Test case for get_facility

        Load an individual Facility  # noqa: E501
        """
        pass

    def test_get_wip(self):
        """Test case for get_wip

        Load an individual Wip  # noqa: E501
        """
        pass

    def test_search_facility(self):
        """Test case for search_facility

        Load the list of Facilities  # noqa: E501
        """
        pass

    def test_search_wips(self):
        """Test case for search_wips

        Load the list of Wips  # noqa: E501
        """
        pass

    def test_update_facility(self):
        """Test case for update_facility

        Update a Facility  # noqa: E501
        """
        pass

    def test_update_wip(self):
        """Test case for update_wip

        Update a Wip  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()