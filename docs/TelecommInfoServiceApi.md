# com.precisely.apis.TelecommInfoServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rate_center_by_address**](TelecommInfoServiceApi.md#get_rate_center_by_address) | **GET** /telecomm/v1/ratecenter/byaddress | Rate Center By Address.
[**get_rate_center_by_location**](TelecommInfoServiceApi.md#get_rate_center_by_location) | **GET** /telecomm/v1/ratecenter/bylocation | Rate Center By Location.


# **get_rate_center_by_address**
> RateCenterResponse get_rate_center_by_address()

Rate Center By Address.

Accepts addresses as input and returns Incumbent Local Exchange Carrier (ILEC) doing-business-as names.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import telecomm_info_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.rate_center_response import RateCenterResponse
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
    api_instance = telecomm_info_service_api.TelecommInfoServiceApi(api_client)
    address = "address_example" # str | The address to be searched (optional)
    country = "country_example" # str | 3 letter ISO code of the country to be searched. Allowed values USA,CAN (optional)
    area_code_info = "areaCodeInfo_example" # str | Specifies whether area code information will be part of response.Allowed values True,False. (optional)
    level = "level_example" # str | Level (basic/detail).Allowed values detail,basic. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rate Center By Address.
        api_response = api_instance.get_rate_center_by_address(address=address, country=country, area_code_info=area_code_info, level=level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TelecommInfoServiceApi->get_rate_center_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched | [optional]
 **country** | **str**| 3 letter ISO code of the country to be searched. Allowed values USA,CAN | [optional]
 **area_code_info** | **str**| Specifies whether area code information will be part of response.Allowed values True,False. | [optional]
 **level** | **str**| Level (basic/detail).Allowed values detail,basic. | [optional]

### Return type

[**RateCenterResponse**](RateCenterResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_center_by_location**
> RateCenterResponse get_rate_center_by_location()

Rate Center By Location.

Accepts latitude & longitude as input and returns Incumbent Local Exchange Carrier (ILEC) doing-business-as names.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import telecomm_info_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.rate_center_response import RateCenterResponse
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
    api_instance = telecomm_info_service_api.TelecommInfoServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location (optional)
    latitude = "latitude_example" # str | Latitude of the location (optional)
    area_code_info = "areaCodeInfo_example" # str | Specifies whether area code information will be part of response.Allowed values True,False. (optional)
    level = "level_example" # str | Level (basic/detail).Allowed values detail,basic. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rate Center By Location.
        api_response = api_instance.get_rate_center_by_location(longitude=longitude, latitude=latitude, area_code_info=area_code_info, level=level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TelecommInfoServiceApi->get_rate_center_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location | [optional]
 **latitude** | **str**| Latitude of the location | [optional]
 **area_code_info** | **str**| Specifies whether area code information will be part of response.Allowed values True,False. | [optional]
 **level** | **str**| Level (basic/detail).Allowed values detail,basic. | [optional]

### Return type

[**RateCenterResponse**](RateCenterResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

