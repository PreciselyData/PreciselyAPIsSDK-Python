"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.4
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
from com.precisely.apis.model.geo_location_access_point import GeoLocationAccessPoint
from com.precisely.apis.model.geo_location_ip_addr import GeoLocationIpAddr


class GeolocationServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_location_by_ip_address_endpoint = _Endpoint(
            settings={
                'response_type': (GeoLocationIpAddr,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/geolocation/v1/location/byipaddress',
                'operation_id': 'get_location_by_ip_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ip_address',
                ],
                'required': [
                    'ip_address',
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
                    'ip_address':
                        (str,),
                },
                'attribute_map': {
                    'ip_address': 'ipAddress',
                },
                'location_map': {
                    'ip_address': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/xml',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_location_by_wi_fi_access_point_endpoint = _Endpoint(
            settings={
                'response_type': (GeoLocationAccessPoint,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/geolocation/v1/location/byaccesspoint',
                'operation_id': 'get_location_by_wi_fi_access_point',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'mac',
                    'ssid',
                    'rsid',
                    'speed',
                    'access_point',
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
                    'mac':
                        (str,),
                    'ssid':
                        (str,),
                    'rsid':
                        (str,),
                    'speed':
                        (str,),
                    'access_point':
                        (str,),
                },
                'attribute_map': {
                    'mac': 'mac',
                    'ssid': 'ssid',
                    'rsid': 'rsid',
                    'speed': 'speed',
                    'access_point': 'accessPoint',
                },
                'location_map': {
                    'mac': 'query',
                    'ssid': 'query',
                    'rsid': 'query',
                    'speed': 'query',
                    'access_point': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/xml',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_location_by_ip_address(
        self,
        ip_address,
        **kwargs
    ):
        """Location By IP Address.  # noqa: E501

        This service accepts an IP address and returns the location coordinates corresponding to that IP address.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_location_by_ip_address(ip_address, async_req=True)
        >>> result = thread.get()

        Args:
            ip_address (str): This is the ip address of network connected device. It must be a standard IPv4 octet and a valid external address.

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
            GeoLocationIpAddr
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
        kwargs['ip_address'] = \
            ip_address
        return self.get_location_by_ip_address_endpoint.call_with_http_info(**kwargs)

    def get_location_by_wi_fi_access_point(
        self,
        **kwargs
    ):
        """Location by WiFi Access Point.  # noqa: E501

        This service accepts a WiFi access point MAC address and returns the location coordinates corresponding to that access point. Only mac or accessPoint are mandatory parameters (one of them has to be provided), rest are optional.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_location_by_wi_fi_access_point(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            mac (str): This should be the 48 bit mac address (or BSSID) of wireless access point. Accepted format is Six groups of two hexadecimal digits, separated by hyphens (-) or colons.. [optional]
            ssid (str): The service set identifier for wi-fi access point. It should be alphanumeric with maximum 32 characters.. [optional]
            rsid (str): This is the received signal strength indicator from particular wi-fi access point. It should be a number from -113 to 0 and the unit of this strength is dBm.. [optional]
            speed (str): This is the connection speed for wi-fi. It should be a number from 0 to 6930 and the unit should be Mbps.. [optional]
            access_point (str): This is the JSON based list of wifi access points in the vicinity of device to be located. This parameter is helpful in case, multiple wifi points are visible and we want to make sure that the location of device is best calculated considering all the access points location.. [optional]
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
            GeoLocationAccessPoint
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
        return self.get_location_by_wi_fi_access_point_endpoint.call_with_http_info(**kwargs)

