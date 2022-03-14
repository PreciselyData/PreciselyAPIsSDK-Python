# com.precisely.apis.GeolocationServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_location_by_ip_address**](GeolocationServiceApi.md#get_location_by_ip_address) | **GET** /geolocation/v1/location/byipaddress | Location By IP Address.
[**get_location_by_wi_fi_access_point**](GeolocationServiceApi.md#get_location_by_wi_fi_access_point) | **GET** /geolocation/v1/location/byaccesspoint | Location by WiFi Access Point.


# **get_location_by_ip_address**
> GeoLocationIpAddr get_location_by_ip_address(ip_address)

Location By IP Address.

This service accepts an IP address and returns the location coordinates corresponding to that IP address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geolocation_service_api
from com.precisely.apis.model.geo_location_ip_addr import GeoLocationIpAddr
from pprint import pprint
# Defining the host is optional and defaults to https://api.precisely.com
# See configuration.py for a list of all supported configuration parameters.
configuration = com.precisely.apis.Configuration(
    host = "https://api.precisely.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2Password
configuration = com.precisely.apis.Configuration(
    host = "https://api.precisely.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with com.precisely.apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geolocation_service_api.GeolocationServiceApi(api_client)
    ip_address = "ipAddress_example" # str | This is the ip address of network connected device. It must be a standard IPv4 octet and a valid external address.

    # example passing only required values which don't have defaults set
    try:
        # Location By IP Address.
        api_response = api_instance.get_location_by_ip_address(ip_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeolocationServiceApi->get_location_by_ip_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| This is the ip address of network connected device. It must be a standard IPv4 octet and a valid external address. |

### Return type

[**GeoLocationIpAddr**](GeoLocationIpAddr.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_by_wi_fi_access_point**
> GeoLocationAccessPoint get_location_by_wi_fi_access_point()

Location by WiFi Access Point.

This service accepts a WiFi access point MAC address and returns the location coordinates corresponding to that access point. Only mac or accessPoint are mandatory parameters (one of them has to be provided), rest are optional.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geolocation_service_api
from com.precisely.apis.model.geo_location_access_point import GeoLocationAccessPoint
from pprint import pprint
# Defining the host is optional and defaults to https://api.precisely.com
# See configuration.py for a list of all supported configuration parameters.
configuration = com.precisely.apis.Configuration(
    host = "https://api.precisely.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2Password
configuration = com.precisely.apis.Configuration(
    host = "https://api.precisely.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with com.precisely.apis.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geolocation_service_api.GeolocationServiceApi(api_client)
    mac = "mac_example" # str | This should be the 48 bit mac address (or BSSID) of wireless access point. Accepted format is Six groups of two hexadecimal digits, separated by hyphens (-) or colons. (optional)
    ssid = "ssid_example" # str | The service set identifier for wi-fi access point. It should be alphanumeric with maximum 32 characters. (optional)
    rsid = "rsid_example" # str | This is the received signal strength indicator from particular wi-fi access point. It should be a number from -113 to 0 and the unit of this strength is dBm. (optional)
    speed = "speed_example" # str | This is the connection speed for wi-fi. It should be a number from 0 to 6930 and the unit should be Mbps. (optional)
    access_point = "accessPoint_example" # str | This is the JSON based list of wifi access points in the vicinity of device to be located. This parameter is helpful in case, multiple wifi points are visible and we want to make sure that the location of device is best calculated considering all the access points location. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Location by WiFi Access Point.
        api_response = api_instance.get_location_by_wi_fi_access_point(mac=mac, ssid=ssid, rsid=rsid, speed=speed, access_point=access_point)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeolocationServiceApi->get_location_by_wi_fi_access_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac** | **str**| This should be the 48 bit mac address (or BSSID) of wireless access point. Accepted format is Six groups of two hexadecimal digits, separated by hyphens (-) or colons. | [optional]
 **ssid** | **str**| The service set identifier for wi-fi access point. It should be alphanumeric with maximum 32 characters. | [optional]
 **rsid** | **str**| This is the received signal strength indicator from particular wi-fi access point. It should be a number from -113 to 0 and the unit of this strength is dBm. | [optional]
 **speed** | **str**| This is the connection speed for wi-fi. It should be a number from 0 to 6930 and the unit should be Mbps. | [optional]
 **access_point** | **str**| This is the JSON based list of wifi access points in the vicinity of device to be located. This parameter is helpful in case, multiple wifi points are visible and we want to make sure that the location of device is best calculated considering all the access points location. | [optional]

### Return type

[**GeoLocationAccessPoint**](GeoLocationAccessPoint.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

