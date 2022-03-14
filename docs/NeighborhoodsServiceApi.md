# com.precisely.apis.NeighborhoodsServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_place_by_location**](NeighborhoodsServiceApi.md#get_place_by_location) | **GET** /neighborhoods/v1/place/bylocation | Place By Location.


# **get_place_by_location**
> NeighborhoodsResponse get_place_by_location()

Place By Location.

Identifies and retrieves the nearest neighborhood around a specific location. This service accepts latitude & longitude as input and returns a place name.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import neighborhoods_service__api
from com.precisely.apis.model.neighborhoods_response import NeighborhoodsResponse
from com.precisely.apis.model.error_info import ErrorInfo
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
    api_instance = neighborhoods_service__api.NeighborhoodsServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location. (optional)
    latitude = "latitude_example" # str | Latitude of the location. (optional)
    level_hint = "levelHint_example" # str | Numeric code of geographic hierarchy level which is classified at six levels.Allowed values 1,2,3,4,5,6 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Place By Location.
        api_response = api_instance.get_place_by_location(longitude=longitude, latitude=latitude, level_hint=level_hint)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling NeighborhoodsServiceApi->get_place_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. | [optional]
 **latitude** | **str**| Latitude of the location. | [optional]
 **level_hint** | **str**| Numeric code of geographic hierarchy level which is classified at six levels.Allowed values 1,2,3,4,5,6 | [optional]

### Return type

[**NeighborhoodsResponse**](NeighborhoodsResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

