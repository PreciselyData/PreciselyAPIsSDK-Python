"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.3
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
from com.precisely.apis.model.intersection_response import IntersectionResponse
from com.precisely.apis.model.speed_limit import SpeedLimit


class StreetsServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_intersection_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (IntersectionResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/streets/v1/intersection/byaddress',
                'operation_id': 'get_intersection_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'address',
                    'road_class',
                    'drive_time',
                    'drive_time_unit',
                    'search_radius',
                    'search_radius_unit',
                    'historic_speed',
                    'max_candidates',
                ],
                'required': [],
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
                    'road_class':
                        (str,),
                    'drive_time':
                        (str,),
                    'drive_time_unit':
                        (str,),
                    'search_radius':
                        (str,),
                    'search_radius_unit':
                        (str,),
                    'historic_speed':
                        (str,),
                    'max_candidates':
                        (str,),
                },
                'attribute_map': {
                    'address': 'address',
                    'road_class': 'roadClass',
                    'drive_time': 'driveTime',
                    'drive_time_unit': 'driveTimeUnit',
                    'search_radius': 'searchRadius',
                    'search_radius_unit': 'searchRadiusUnit',
                    'historic_speed': 'historicSpeed',
                    'max_candidates': 'maxCandidates',
                },
                'location_map': {
                    'address': 'query',
                    'road_class': 'query',
                    'drive_time': 'query',
                    'drive_time_unit': 'query',
                    'search_radius': 'query',
                    'search_radius_unit': 'query',
                    'historic_speed': 'query',
                    'max_candidates': 'query',
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
        self.get_intersection_by_location_endpoint = _Endpoint(
            settings={
                'response_type': (IntersectionResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/streets/v1/intersection/bylocation',
                'operation_id': 'get_intersection_by_location',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'longitude',
                    'latitude',
                    'road_class',
                    'drive_time',
                    'drive_time_unit',
                    'search_radius',
                    'search_radius_unit',
                    'historic_speed',
                    'max_candidates',
                ],
                'required': [],
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
                    'longitude':
                        (str,),
                    'latitude':
                        (str,),
                    'road_class':
                        (str,),
                    'drive_time':
                        (str,),
                    'drive_time_unit':
                        (str,),
                    'search_radius':
                        (str,),
                    'search_radius_unit':
                        (str,),
                    'historic_speed':
                        (str,),
                    'max_candidates':
                        (str,),
                },
                'attribute_map': {
                    'longitude': 'longitude',
                    'latitude': 'latitude',
                    'road_class': 'roadClass',
                    'drive_time': 'driveTime',
                    'drive_time_unit': 'driveTimeUnit',
                    'search_radius': 'searchRadius',
                    'search_radius_unit': 'searchRadiusUnit',
                    'historic_speed': 'historicSpeed',
                    'max_candidates': 'maxCandidates',
                },
                'location_map': {
                    'longitude': 'query',
                    'latitude': 'query',
                    'road_class': 'query',
                    'drive_time': 'query',
                    'drive_time_unit': 'query',
                    'search_radius': 'query',
                    'search_radius_unit': 'query',
                    'historic_speed': 'query',
                    'max_candidates': 'query',
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
        self.get_nearest_speed_limit_endpoint = _Endpoint(
            settings={
                'response_type': (SpeedLimit,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/streets/v1/speedlimit',
                'operation_id': 'get_nearest_speed_limit',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'path',
                ],
                'required': [],
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
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'path': 'path',
                },
                'location_map': {
                    'path': 'query',
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

    def get_intersection_by_address(
        self,
        **kwargs
    ):
        """Nearest Intesection By Address.  # noqa: E501

        This service accepts an address as input and returns the Nearest Intersection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_intersection_by_address(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            address (str): Address. [optional]
            road_class (str): Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All. [optional]
            drive_time (str): Returns Intersection in specified drive time. [optional]
            drive_time_unit (str): Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes. [optional]
            search_radius (str): Search radius within which user wants to search, default is 50 miles. [optional]
            search_radius_unit (str): Search radius unit, allowed values are (feet, meter, kilometers and miles). [optional]
            historic_speed (str): Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT). [optional]
            max_candidates (str): max candidates to be returned default is 1. [optional]
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
            IntersectionResponse
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
        return self.get_intersection_by_address_endpoint.call_with_http_info(**kwargs)

    def get_intersection_by_location(
        self,
        **kwargs
    ):
        """Nearest Intesection By Location.  # noqa: E501

        This service accepts latitude/longitude as input and returns the Nearest Intersection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_intersection_by_location(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            longitude (str): Longitude of the location.. [optional]
            latitude (str): Latitude of the location.. [optional]
            road_class (str): Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All. [optional]
            drive_time (str): Returns Intersection in specified drive time. [optional]
            drive_time_unit (str): Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes. [optional]
            search_radius (str): Search radius within which user wants to search, default is 50 miles. [optional]
            search_radius_unit (str): Search radius unit, allowed values are (feet, meter, kilometers and miles). [optional]
            historic_speed (str): Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT). [optional]
            max_candidates (str): max candidates to be returned default is 1. [optional]
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
            IntersectionResponse
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
        return self.get_intersection_by_location_endpoint.call_with_http_info(**kwargs)

    def get_nearest_speed_limit(
        self,
        **kwargs
    ):
        """Nearest Speedlimit.  # noqa: E501

        This service accepts point coordinates of a path as input and returns the posted speed limit of the road segment on which this path will snap.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_nearest_speed_limit(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            path (str): Accepts multiple points which will be snapped to the nearest road segment. Longitude and Latitude will be comma separated (longitude,latitude) and Point Coordinates will be separated by semi-colon(;). [optional]
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
            SpeedLimit
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
        return self.get_nearest_speed_limit_endpoint.call_with_http_info(**kwargs)

