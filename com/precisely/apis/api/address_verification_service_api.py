"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 16.0.1
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
from com.precisely.apis.model.get_city_state_province_api_request import GetCityStateProvinceAPIRequest
from com.precisely.apis.model.get_city_state_province_api_response import GetCityStateProvinceAPIResponse
from com.precisely.apis.model.get_postal_codes_api_request import GetPostalCodesAPIRequest
from com.precisely.apis.model.get_postal_codes_api_response import GetPostalCodesAPIResponse
from com.precisely.apis.model.validate_mailing_address_premium_request import ValidateMailingAddressPremiumRequest
from com.precisely.apis.model.validate_mailing_address_premium_response import ValidateMailingAddressPremiumResponse
from com.precisely.apis.model.validate_mailing_address_pro_request import ValidateMailingAddressProRequest
from com.precisely.apis.model.validate_mailing_address_pro_response import ValidateMailingAddressProResponse
from com.precisely.apis.model.validate_mailing_address_request import ValidateMailingAddressRequest
from com.precisely.apis.model.validate_mailing_address_response import ValidateMailingAddressResponse
from com.precisely.apis.model.validate_mailing_address_uscanapi_request import ValidateMailingAddressUSCANAPIRequest
from com.precisely.apis.model.validate_mailing_address_uscanapi_response import ValidateMailingAddressUSCANAPIResponse


class AddressVerificationServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_city_state_province_endpoint = _Endpoint(
            settings={
                'response_type': (GetCityStateProvinceAPIResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/getcitystateprovince/results.json',
                'operation_id': 'get_city_state_province',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (GetCityStateProvinceAPIRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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
        self.get_postal_codes_endpoint = _Endpoint(
            settings={
                'response_type': (GetPostalCodesAPIResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/getpostalcodes/results.json',
                'operation_id': 'get_postal_codes',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (GetPostalCodesAPIRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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
        self.validate_mailing_address_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateMailingAddressResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/validatemailingaddress/results.json',
                'operation_id': 'validate_mailing_address',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (ValidateMailingAddressRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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
        self.validate_mailing_address_premium_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateMailingAddressPremiumResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/validatemailingaddresspremium/results.json',
                'operation_id': 'validate_mailing_address_premium',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (ValidateMailingAddressPremiumRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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
        self.validate_mailing_address_pro_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateMailingAddressProResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/validatemailingaddresspro/results.json',
                'operation_id': 'validate_mailing_address_pro',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (ValidateMailingAddressProRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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
        self.validate_mailing_address_uscan_endpoint = _Endpoint(
            settings={
                'response_type': (ValidateMailingAddressUSCANAPIResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/addressverification/v1/validatemailingaddressuscan/results.json',
                'operation_id': 'validate_mailing_address_uscan',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'input_address',
                ],
                'required': [
                    'input_address',
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
                    'input_address':
                        (ValidateMailingAddressUSCANAPIRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'input_address': 'body',
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

    def get_city_state_province(
        self,
        input_address,
        **kwargs
    ):
        """GetCityStateProvince  # noqa: E501

        GetCityStateProvince returns a city and state/province for a given input postal code for U.S. and Canadian addresses.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_city_state_province(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (GetCityStateProvinceAPIRequest):

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
            GetCityStateProvinceAPIResponse
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
        kwargs['input_address'] = \
            input_address
        return self.get_city_state_province_endpoint.call_with_http_info(**kwargs)

    def get_postal_codes(
        self,
        input_address,
        **kwargs
    ):
        """GetPostalCodes  # noqa: E501

        GetPostalCodes takes a city and state as input for U.S. addresses and returns the postal codes for that city.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_postal_codes(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (GetPostalCodesAPIRequest):

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
            GetPostalCodesAPIResponse
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
        kwargs['input_address'] = \
            input_address
        return self.get_postal_codes_endpoint.call_with_http_info(**kwargs)

    def validate_mailing_address(
        self,
        input_address,
        **kwargs
    ):
        """ValidateMailingAddress  # noqa: E501

        ValidateMailingAddress analyses and compares the input addresses against the known address databases around the world to output a standardized detail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_mailing_address(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (ValidateMailingAddressRequest):

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
            ValidateMailingAddressResponse
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
        kwargs['input_address'] = \
            input_address
        return self.validate_mailing_address_endpoint.call_with_http_info(**kwargs)

    def validate_mailing_address_premium(
        self,
        input_address,
        **kwargs
    ):
        """ValidateMailingAddressPremium  # noqa: E501

        ValidateMailing AddressPremium expands on the ValidateMailingAddressPro service by adding premium address data sources to get the best address validation result possible.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_mailing_address_premium(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (ValidateMailingAddressPremiumRequest):

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
            ValidateMailingAddressPremiumResponse
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
        kwargs['input_address'] = \
            input_address
        return self.validate_mailing_address_premium_endpoint.call_with_http_info(**kwargs)

    def validate_mailing_address_pro(
        self,
        input_address,
        **kwargs
    ):
        """ValidateMailingAddressPro  # noqa: E501

        ValidateMailingAddressPro builds upon the ValidateMailingAddress service by using additional address databases so it can provide enhanced detail.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_mailing_address_pro(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (ValidateMailingAddressProRequest):

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
            ValidateMailingAddressProResponse
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
        kwargs['input_address'] = \
            input_address
        return self.validate_mailing_address_pro_endpoint.call_with_http_info(**kwargs)

    def validate_mailing_address_uscan(
        self,
        input_address,
        **kwargs
    ):
        """ValidateMailingAddressUSCAN  # noqa: E501

        ValidateMailingAddressUSCAN analyses and compares the input addresses against the known address databases around the world to output a standardized detail for US and CANADAIt gives RDI and DPV also along with other US/CAN specific functionalities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_mailing_address_uscan(input_address, async_req=True)
        >>> result = thread.get()

        Args:
            input_address (ValidateMailingAddressUSCANAPIRequest):

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
            ValidateMailingAddressUSCANAPIResponse
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
        kwargs['input_address'] = \
            input_address
        return self.validate_mailing_address_uscan_endpoint.call_with_http_info(**kwargs)

