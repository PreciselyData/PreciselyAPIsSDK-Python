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
from com.precisely.apis.model.addresses_by_boundary_request import AddressesByBoundaryRequest
from com.precisely.apis.model.addresses_count import AddressesCount
from com.precisely.apis.model.addresses_response import AddressesResponse
from com.precisely.apis.model.error_info import ErrorInfo


class AddressesServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_addresses_count_by_boundary_name_endpoint = _Endpoint(
            settings={
                'response_type': (AddressesCount,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addresses/v1/addresscount/byboundaryname',
                'operation_id': 'get_addresses_count_by_boundary_name',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country',
                    'area_name1',
                    'area_name2',
                    'area_name3',
                    'area_name4',
                    'post_code',
                ],
                'required': [
                    'country',
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
                    'country':
                        (str,),
                    'area_name1':
                        (str,),
                    'area_name2':
                        (str,),
                    'area_name3':
                        (str,),
                    'area_name4':
                        (str,),
                    'post_code':
                        (str,),
                },
                'attribute_map': {
                    'country': 'country',
                    'area_name1': 'areaName1',
                    'area_name2': 'areaName2',
                    'area_name3': 'areaName3',
                    'area_name4': 'areaName4',
                    'post_code': 'postCode',
                },
                'location_map': {
                    'country': 'query',
                    'area_name1': 'query',
                    'area_name2': 'query',
                    'area_name3': 'query',
                    'area_name4': 'query',
                    'post_code': 'query',
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
        self.get_addresses_countby_boundary_endpoint = _Endpoint(
            settings={
                'response_type': (AddressesCount,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addresses/v1/addresscount/byboundary',
                'operation_id': 'get_addresses_countby_boundary',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'addresses_by_boundary_request',
                ],
                'required': [
                    'addresses_by_boundary_request',
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
                    'addresses_by_boundary_request':
                        (AddressesByBoundaryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'addresses_by_boundary_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.get_addressesby_boundary_endpoint = _Endpoint(
            settings={
                'response_type': (AddressesResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addresses/v1/address/byboundary',
                'operation_id': 'get_addressesby_boundary',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'addresses_by_boundary_request',
                ],
                'required': [
                    'addresses_by_boundary_request',
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
                    'addresses_by_boundary_request':
                        (AddressesByBoundaryRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'addresses_by_boundary_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'text/csv'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_addressesby_boundary_name_endpoint = _Endpoint(
            settings={
                'response_type': (AddressesResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addresses/v1/address/byboundaryname',
                'operation_id': 'get_addressesby_boundary_name',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country',
                    'area_name1',
                    'area_name2',
                    'area_name3',
                    'area_name4',
                    'post_code',
                    'max_candidates',
                    'page',
                ],
                'required': [
                    'country',
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
                    'country':
                        (str,),
                    'area_name1':
                        (str,),
                    'area_name2':
                        (str,),
                    'area_name3':
                        (str,),
                    'area_name4':
                        (str,),
                    'post_code':
                        (str,),
                    'max_candidates':
                        (str,),
                    'page':
                        (str,),
                },
                'attribute_map': {
                    'country': 'country',
                    'area_name1': 'areaName1',
                    'area_name2': 'areaName2',
                    'area_name3': 'areaName3',
                    'area_name4': 'areaName4',
                    'post_code': 'postCode',
                    'max_candidates': 'maxCandidates',
                    'page': 'page',
                },
                'location_map': {
                    'country': 'query',
                    'area_name1': 'query',
                    'area_name2': 'query',
                    'area_name3': 'query',
                    'area_name4': 'query',
                    'post_code': 'query',
                    'max_candidates': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'text/csv'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_addresses_count_by_boundary_name(
        self,
        country,
        **kwargs
    ):
        """Addresses Count by Boundary Name.  # noqa: E501

        This service accepts zip code, neighborhood, county, or city names, and returns the total number of addresses associated with these names.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addresses_count_by_boundary_name(country, async_req=True)
        >>> result = thread.get()

        Args:
            country (str): Name of country. Acceptable values are CAN, USA.

        Keyword Args:
            area_name1 (str): Specifies the largest geographical area, typically a state or province.. [optional]
            area_name2 (str): Specifies the secondary geographic area, typically a county or district.. [optional]
            area_name3 (str): Specifies a city or town name.. [optional]
            area_name4 (str): Specifies a city subdivision or locality/neighborhood.. [optional]
            post_code (str): Specifies the postcode (ZIP code) in the appropriate format for the country.. [optional]
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
            AddressesCount
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
        kwargs['country'] = \
            country
        return self.get_addresses_count_by_boundary_name_endpoint.call_with_http_info(**kwargs)

    def get_addresses_countby_boundary(
        self,
        addresses_by_boundary_request,
        **kwargs
    ):
        """Addresses count by Boundary.  # noqa: E501

        This service accepts custom geographic boundaries or drive time & drive distance, returns the total number of addresses within these boundaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addresses_countby_boundary(addresses_by_boundary_request, async_req=True)
        >>> result = thread.get()

        Args:
            addresses_by_boundary_request (AddressesByBoundaryRequest):

        Keyword Args:
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
            AddressesCount
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
        kwargs['addresses_by_boundary_request'] = \
            addresses_by_boundary_request
        return self.get_addresses_countby_boundary_endpoint.call_with_http_info(**kwargs)

    def get_addressesby_boundary(
        self,
        addresses_by_boundary_request,
        **kwargs
    ):
        """Addresses by Boundary.  # noqa: E501

        This service accepts custom geographic boundaries or drive time & drive distance, returns all known & valid addresses within these boundaries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addressesby_boundary(addresses_by_boundary_request, async_req=True)
        >>> result = thread.get()

        Args:
            addresses_by_boundary_request (AddressesByBoundaryRequest):

        Keyword Args:
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
            AddressesResponse
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
        kwargs['addresses_by_boundary_request'] = \
            addresses_by_boundary_request
        return self.get_addressesby_boundary_endpoint.call_with_http_info(**kwargs)

    def get_addressesby_boundary_name(
        self,
        country,
        **kwargs
    ):
        """Addresses by Boundary Name.  # noqa: E501

        This service accepts zip code, neighborhood, county, or city names, and returns all known & valid addresses associated with these names.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_addressesby_boundary_name(country, async_req=True)
        >>> result = thread.get()

        Args:
            country (str): Name of country. Acceptable values are CAN, USA.

        Keyword Args:
            area_name1 (str): Specifies the largest geographical area, typically a state or province.. [optional]
            area_name2 (str): Specifies the secondary geographic area, typically a county or district.. [optional]
            area_name3 (str): Specifies a city or town name.. [optional]
            area_name4 (str): Specifies a city subdivision or locality/neighborhood.. [optional]
            post_code (str): Specifies the postcode (ZIP code) in the appropriate format for the country.. [optional]
            max_candidates (str): Maximum number of addresses to be returned in response. Max. value is 100 for XML/JSON, and 2000 for CSV.. [optional]
            page (str): Response will indicate the page number.. [optional]
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
            AddressesResponse
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
        kwargs['country'] = \
            country
        return self.get_addressesby_boundary_name_endpoint.call_with_http_info(**kwargs)

