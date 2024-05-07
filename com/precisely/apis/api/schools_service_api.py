"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 18.1.0
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
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.schools_near_by_response import SchoolsNearByResponse


class SchoolsServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_schools_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (SchoolsNearByResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/schools/v1/school/byaddress',
                'operation_id': 'get_schools_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'address',
                    'ed_level',
                    'school_type',
                    'school_sub_type',
                    'gender',
                    'assigned_schools_only',
                    'district_schools_only',
                    'search_radius',
                    'search_radius_unit',
                    'travel_time',
                    'travel_time_unit',
                    'travel_distance',
                    'travel_distance_unit',
                    'travel_mode',
                    'max_candidates',
                ],
                'required': [
                    'address',
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
                    'address':
                        (str,),
                    'ed_level':
                        (str,),
                    'school_type':
                        (str,),
                    'school_sub_type':
                        (str,),
                    'gender':
                        (str,),
                    'assigned_schools_only':
                        (str,),
                    'district_schools_only':
                        (str,),
                    'search_radius':
                        (str,),
                    'search_radius_unit':
                        (str,),
                    'travel_time':
                        (str,),
                    'travel_time_unit':
                        (str,),
                    'travel_distance':
                        (str,),
                    'travel_distance_unit':
                        (str,),
                    'travel_mode':
                        (str,),
                    'max_candidates':
                        (str,),
                },
                'attribute_map': {
                    'address': 'address',
                    'ed_level': 'edLevel',
                    'school_type': 'schoolType',
                    'school_sub_type': 'schoolSubType',
                    'gender': 'gender',
                    'assigned_schools_only': 'assignedSchoolsOnly',
                    'district_schools_only': 'districtSchoolsOnly',
                    'search_radius': 'searchRadius',
                    'search_radius_unit': 'searchRadiusUnit',
                    'travel_time': 'travelTime',
                    'travel_time_unit': 'travelTimeUnit',
                    'travel_distance': 'travelDistance',
                    'travel_distance_unit': 'travelDistanceUnit',
                    'travel_mode': 'travelMode',
                    'max_candidates': 'maxCandidates',
                },
                'location_map': {
                    'address': 'query',
                    'ed_level': 'query',
                    'school_type': 'query',
                    'school_sub_type': 'query',
                    'gender': 'query',
                    'assigned_schools_only': 'query',
                    'district_schools_only': 'query',
                    'search_radius': 'query',
                    'search_radius_unit': 'query',
                    'travel_time': 'query',
                    'travel_time_unit': 'query',
                    'travel_distance': 'query',
                    'travel_distance_unit': 'query',
                    'travel_mode': 'query',
                    'max_candidates': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_schools_by_address(
        self,
        address,
        **kwargs
    ):
        """Search Nearby Schools by Address  # noqa: E501

        Search Nearby Schools by Address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_schools_by_address(address, async_req=True)
        >>> result = thread.get()

        Args:
            address (str): free form address text

        Keyword Args:
            ed_level (str): Single digit code for education level applicable values are P -> primary, M -> Middle, H -> High, O -> Mixed Grades for public school type andE -> Elementary , S -> Secondary , O -> Others mixed grades for private schools . [optional]
            school_type (str): Single digit code for schoolTypes applicable values are PRI and PUB. [optional]
            school_sub_type (str): Single digit code for schoolSubType Applicable values are C, M, A, R, I, L, P, V, U, S (i.e. Charter, Magnet, Alternative, Regular, Indian, Military, Reportable Program, Vocational, Unknown, Special Education). [optional]
            gender (str): Single digit code for gender Applicable values are C, F, M (Coed, All Females, All Males) Applicable for Private Schools Only. [optional]
            assigned_schools_only (str): Single digit code for assignedSchoolOnly applicable values are  Y/N . [optional]
            district_schools_only (str): Single digit code for districtSchoolOnly applicable values are Y/N . [optional]
            search_radius (str): Search Radius within which schools are searched. [optional]
            search_radius_unit (str): Search Radius unit applicable values are feet,kilometers,miles,meters. [optional]
            travel_time (str): Travel Time based on ‘travelMode’ within which schools are searched.. [optional]
            travel_time_unit (str): Travel Time unit applicable values are minutes,hours,seconds,milliseconds . [optional]
            travel_distance (str): Travel Distance based on ‘travelMode’ within which schools are searched.. [optional]
            travel_distance_unit (str): Travel distanceUnit applicable values are feet,kilometers,miles,meters. [optional]
            travel_mode (str): Travel mode Required when travelDistance or travelTime is specified. Accepted values are walking,driving. [optional]
            max_candidates (str): Max result to search . [optional]
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
            SchoolsNearByResponse
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
        kwargs['address'] = \
            address
        return self.get_schools_by_address_endpoint.call_with_http_info(**kwargs)

