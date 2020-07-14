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
from api.company_api import CompanyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCompanyApi(unittest.TestCase):
    """CompanyApi unit test stubs"""

    def setUp(self):
        self.api = api.company_api.CompanyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_company(self):
        """Test case for add_company

        Create a new Company  # noqa: E501
        """
        pass

    def test_add_product(self):
        """Test case for add_product

        Create a new Product  # noqa: E501
        """
        pass

    def test_delete_company(self):
        """Test case for delete_company

        Delete a Company  # noqa: E501
        """
        pass

    def test_delete_product(self):
        """Test case for delete_product

        Delete a Product  # noqa: E501
        """
        pass

    def test_get_company(self):
        """Test case for get_company

        Load an individual Company  # noqa: E501
        """
        pass

    def test_get_product(self):
        """Test case for get_product

        Load an individual Product  # noqa: E501
        """
        pass

    def test_search_companies(self):
        """Test case for search_companies

        Load the list of Companies  # noqa: E501
        """
        pass

    def test_search_products(self):
        """Test case for search_products

        Load the list of Products  # noqa: E501
        """
        pass

    def test_update_company(self):
        """Test case for update_company

        Update a Company  # noqa: E501
        """
        pass

    def test_update_product(self):
        """Test case for update_product

        Update a Product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()