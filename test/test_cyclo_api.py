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
from api.cyclo_api import CycloApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCycloApi(unittest.TestCase):
    """CycloApi unit test stubs"""

    def setUp(self):
        self.api = api.cyclo_api.CycloApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_cyclo(self):
        """Test case for add_cyclo

        Create a new Cyclo  # noqa: E501
        """
        pass

    def test_add_stage(self):
        """Test case for add_stage

        Create a new Stage  # noqa: E501
        """
        pass

    def test_add_task(self):
        """Test case for add_task

        Create a new Task  # noqa: E501
        """
        pass

    def test_delete_cyclo(self):
        """Test case for delete_cyclo

        Delete a Cyclo  # noqa: E501
        """
        pass

    def test_delete_stage(self):
        """Test case for delete_stage

        Delete a Stage  # noqa: E501
        """
        pass

    def test_delete_task(self):
        """Test case for delete_task

        Delete a Task  # noqa: E501
        """
        pass

    def test_get_cyclo(self):
        """Test case for get_cyclo

        Load an individual Cyclo  # noqa: E501
        """
        pass

    def test_get_stage(self):
        """Test case for get_stage

        Load an individual Stage  # noqa: E501
        """
        pass

    def test_get_task(self):
        """Test case for get_task

        Load an individual Task  # noqa: E501
        """
        pass

    def test_search_cyclos(self):
        """Test case for search_cyclos

        Load the list of Cyclos  # noqa: E501
        """
        pass

    def test_search_stages(self):
        """Test case for search_stages

        Load the list of Stages  # noqa: E501
        """
        pass

    def test_search_tasks(self):
        """Test case for search_tasks

        Load the list of Tasks  # noqa: E501
        """
        pass

    def test_update_cyclo(self):
        """Test case for update_cyclo

        Update a Cyclo  # noqa: E501
        """
        pass

    def test_update_stage(self):
        """Test case for update_stage

        Update a Stage  # noqa: E501
        """
        pass

    def test_update_task(self):
        """Test case for update_task

        Update a Task  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()