"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.precisely.apis
from com.precisely.apis.api.zones_service_api import ZonesServiceApi  # noqa: E501


class TestZonesServiceApi(unittest.TestCase):
    """ZonesServiceApi unit test stubs"""

    def setUp(self):
        self.api = ZonesServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_basic_boundary_by_address(self):
        """Test case for get_basic_boundary_by_address

        Gets Basic Boundary by Address.  # noqa: E501
        """
        pass

    def test_get_basic_boundary_by_location(self):
        """Test case for get_basic_boundary_by_location

        Gets Basic Boundary by Location.  # noqa: E501
        """
        pass

    def test_get_poi_boundary_by_address(self):
        """Test case for get_poi_boundary_by_address

        Gets Point of Interests Boundary by Address.  # noqa: E501
        """
        pass

    def test_get_poi_boundary_by_address_batch(self):
        """Test case for get_poi_boundary_by_address_batch

        Batch method for getting Point of Interests Boundary by Address.  # noqa: E501
        """
        pass

    def test_get_poi_boundary_by_location(self):
        """Test case for get_poi_boundary_by_location

        Get Point of Interests Boundary by Location.  # noqa: E501
        """
        pass

    def test_get_poi_boundary_by_location_batch(self):
        """Test case for get_poi_boundary_by_location_batch

        Batch method for getting Point of Interests Boundary by Location.  # noqa: E501
        """
        pass

    def test_get_travel_boundary_by_distance(self):
        """Test case for get_travel_boundary_by_distance

        Get TravelBoundary By Distance.  # noqa: E501
        """
        pass

    def test_get_travel_boundary_by_time(self):
        """Test case for get_travel_boundary_by_time

        Get TravelBoundary By Time.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
