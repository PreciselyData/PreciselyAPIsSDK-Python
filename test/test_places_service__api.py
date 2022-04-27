"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.2
    Generated by: https://openapi-generator.tech
"""


import unittest

import com.precisely.apis
from com.precisely.apis.api.places_service__api import PlacesServiceApi  # noqa: E501


class TestPlacesServiceApi(unittest.TestCase):
    """PlacesServiceApi unit test stubs"""

    def setUp(self):
        self.api = PlacesServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_category_code_metadata(self):
        """Test case for get_category_code_metadata

        Category Code Metadata.  # noqa: E501
        """
        pass

    def test_get_poiby_id(self):
        """Test case for get_poiby_id

        Points Of Interest Details By Id  # noqa: E501
        """
        pass

    def test_get_pois_by_address(self):
        """Test case for get_pois_by_address

        Get POIs By Address.  # noqa: E501
        """
        pass

    def test_get_pois_by_area(self):
        """Test case for get_pois_by_area

        GET Points Of Interest By Area.  # noqa: E501
        """
        pass

    def test_get_pois_by_geometry(self):
        """Test case for get_pois_by_geometry

        Points Of Interest By Boundary  # noqa: E501
        """
        pass

    def test_get_pois_by_location(self):
        """Test case for get_pois_by_location

        Get POIs By Location.  # noqa: E501
        """
        pass

    def test_get_pois_count(self):
        """Test case for get_pois_count

        Points Of Interest Count  # noqa: E501
        """
        pass

    def test_get_sic_metadata(self):
        """Test case for get_sic_metadata

        Get SIC Metadata  # noqa: E501
        """
        pass

    def test_pois_autocomplete(self):
        """Test case for pois_autocomplete

        Points Of Interest Autocomplete  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
