"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 17.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from com.precisely.apis.api_client import ApiClient, Endpoint as _Endpoint
from com.precisely.apis.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.typeahead_locations import TypeaheadLocations


class AddressAutocompleteServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.search_v2_endpoint = _Endpoint(
            settings={
                'response_type': (TypeaheadLocations,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/typeahead/v1/locations',
                'operation_id': 'search_v2',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'search_text',
                    'latitude',
                    'longitude',
                    'search_radius',
                    'search_radius_unit',
                    'max_candidates',
                    'country',
                    'match_on_address_number',
                    'auto_detect_location',
                    'ip_address',
                    'area_name1',
                    'area_name3',
                    'post_code',
                    'return_admin_areas_only',
                    'include_ranges_details',
                    'search_type',
                    'search_on_address_number',
                    'search_on_unit_info',
                ],
                'required': [
                    'search_text',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'search_text':
                        (str,),
                    'latitude':
                        (str,),
                    'longitude':
                        (str,),
                    'search_radius':
                        (str,),
                    'search_radius_unit':
                        (str,),
                    'max_candidates':
                        (str,),
                    'country':
                        (str,),
                    'match_on_address_number':
                        (str,),
                    'auto_detect_location':
                        (str,),
                    'ip_address':
                        (str,),
                    'area_name1':
                        (str,),
                    'area_name3':
                        (str,),
                    'post_code':
                        (str,),
                    'return_admin_areas_only':
                        (str,),
                    'include_ranges_details':
                        (str,),
                    'search_type':
                        (str,),
                    'search_on_address_number':
                        (str,),
                    'search_on_unit_info':
                        (str,),
                },
                'attribute_map': {
                    'search_text': 'searchText',
                    'latitude': 'latitude',
                    'longitude': 'longitude',
                    'search_radius': 'searchRadius',
                    'search_radius_unit': 'searchRadiusUnit',
                    'max_candidates': 'maxCandidates',
                    'country': 'country',
                    'match_on_address_number': 'matchOnAddressNumber',
                    'auto_detect_location': 'autoDetectLocation',
                    'ip_address': 'ipAddress',
                    'area_name1': 'areaName1',
                    'area_name3': 'areaName3',
                    'post_code': 'postCode',
                    'return_admin_areas_only': 'returnAdminAreasOnly',
                    'include_ranges_details': 'includeRangesDetails',
                    'search_type': 'searchType',
                    'search_on_address_number': 'searchOnAddressNumber',
                    'search_on_unit_info': 'searchOnUnitInfo',
                },
                'location_map': {
                    'search_text': 'query',
                    'latitude': 'query',
                    'longitude': 'query',
                    'search_radius': 'query',
                    'search_radius_unit': 'query',
                    'max_candidates': 'query',
                    'country': 'query',
                    'match_on_address_number': 'query',
                    'auto_detect_location': 'query',
                    'ip_address': 'query',
                    'area_name1': 'query',
                    'area_name3': 'query',
                    'post_code': 'query',
                    'return_admin_areas_only': 'query',
                    'include_ranges_details': 'query',
                    'search_type': 'query',
                    'search_on_address_number': 'query',
                    'search_on_unit_info': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def search_v2(
        self,
        search_text,
        **kwargs
    ):
        """Address Autocomplete Search  # noqa: E501

        Performs search to retrieve list of places by input text and location vicinity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_v2(search_text, async_req=True)
        >>> result = thread.get()

        Args:
            search_text (str): The input to be searched.

        Keyword Args:
            latitude (str): Latitude of the location. We need to make sure that either Lat/Lng or Country is provided to API. [optional]
            longitude (str): Longitude of the location. We need to make sure that either Lat/Lng or Country is provided to API. [optional]
            search_radius (str): Radius range within which search is performed.. [optional]
            search_radius_unit (str): Radius unit such as Feet, Kilometers, Miles or Meters.. [optional]
            max_candidates (str): Maximum number of POIs that can be retrieved.. [optional]
            country (str): Country ISO code. We need to make sure that either Lat/Lng or Country is provided to API. [optional]
            match_on_address_number (str): Option so that we force api to match on address number. [optional]
            auto_detect_location (str): Option to allow API to detect origin of API request automatically. [optional]
            ip_address (str): [optional]
            area_name1 (str): State province of the input to be searched. [optional]
            area_name3 (str): City of the input to be searched. [optional]
            post_code (str): Postal Code of the input to be searched. [optional]
            return_admin_areas_only (str): if value set 'Y' then it will only do a matching on postcode or areaName1, areaName2, areaName3 and areaName4 fields in the data. [optional]
            include_ranges_details (str): if value set 'Y' then display all unit info of ranges, if value set 'N' then don't show ranges. [optional]
            search_type (str): Preference to control search type of interactive requests.. [optional]
            search_on_address_number (str): Preference to search on address number.. [optional]
            search_on_unit_info (str): Preference to search on unit info.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TypeaheadLocations
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['search_text'] = \
            search_text
        return self.search_v2_endpoint.call_with_http_info(**kwargs)

