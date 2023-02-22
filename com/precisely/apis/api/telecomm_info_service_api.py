"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 14.0.0
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
from com.precisely.apis.model.rate_center_response import RateCenterResponse


class TelecommInfoServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_rate_center_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (RateCenterResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/telecomm/v1/ratecenter/byaddress',
                'operation_id': 'get_rate_center_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'address',
                    'country',
                    'area_code_info',
                    'level',
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
                    'country':
                        (str,),
                    'area_code_info':
                        (str,),
                    'level':
                        (str,),
                },
                'attribute_map': {
                    'address': 'address',
                    'country': 'country',
                    'area_code_info': 'areaCodeInfo',
                    'level': 'level',
                },
                'location_map': {
                    'address': 'query',
                    'country': 'query',
                    'area_code_info': 'query',
                    'level': 'query',
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
        self.get_rate_center_by_location_endpoint = _Endpoint(
            settings={
                'response_type': (RateCenterResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/telecomm/v1/ratecenter/bylocation',
                'operation_id': 'get_rate_center_by_location',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'longitude',
                    'latitude',
                    'area_code_info',
                    'level',
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
                    'area_code_info':
                        (str,),
                    'level':
                        (str,),
                },
                'attribute_map': {
                    'longitude': 'longitude',
                    'latitude': 'latitude',
                    'area_code_info': 'areaCodeInfo',
                    'level': 'level',
                },
                'location_map': {
                    'longitude': 'query',
                    'latitude': 'query',
                    'area_code_info': 'query',
                    'level': 'query',
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

    def get_rate_center_by_address(
        self,
        **kwargs
    ):
        """Rate Center By Address.  # noqa: E501

        Accepts addresses as input and returns Incumbent Local Exchange Carrier (ILEC) doing-business-as names.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rate_center_by_address(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            address (str): The address to be searched. [optional]
            country (str): 3 letter ISO code of the country to be searched. Allowed values USA,CAN. [optional]
            area_code_info (str): Specifies whether area code information will be part of response.Allowed values True,False.. [optional]
            level (str): Level (basic/detail).Allowed values detail,basic.. [optional]
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
            RateCenterResponse
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
        return self.get_rate_center_by_address_endpoint.call_with_http_info(**kwargs)

    def get_rate_center_by_location(
        self,
        **kwargs
    ):
        """Rate Center By Location.  # noqa: E501

        Accepts latitude & longitude as input and returns Incumbent Local Exchange Carrier (ILEC) doing-business-as names.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rate_center_by_location(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            longitude (str): Longitude of the location. [optional]
            latitude (str): Latitude of the location. [optional]
            area_code_info (str): Specifies whether area code information will be part of response.Allowed values True,False.. [optional]
            level (str): Level (basic/detail).Allowed values detail,basic.. [optional]
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
            RateCenterResponse
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
        return self.get_rate_center_by_location_endpoint.call_with_http_info(**kwargs)

