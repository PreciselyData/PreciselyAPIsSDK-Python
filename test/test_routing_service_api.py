"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.precisely.apis
from com.precisely.apis.api.routing_service_api import RoutingServiceApi  # noqa: E501


class TestRoutingServiceApi(unittest.TestCase):
    """RoutingServiceApi unit test stubs"""

    def setUp(self):
        self.api = RoutingServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_route_by_address(self):
        """Test case for get_route_by_address

        Gets Route By Address.  # noqa: E501
        """
        pass

    def test_get_route_by_location(self):
        """Test case for get_route_by_location

        Gets Route By Location.  # noqa: E501
        """
        pass

    def test_get_travel_cost_matrix_by_address(self):
        """Test case for get_travel_cost_matrix_by_address

        Get Cost Matrix By Address.  # noqa: E501
        """
        pass

    def test_get_travel_cost_matrix_by_location(self):
        """Test case for get_travel_cost_matrix_by_location

        Get Cost Matrix By Location.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
