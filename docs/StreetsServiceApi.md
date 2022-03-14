# com.precisely.apis.StreetsServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_intersection_by_address**](StreetsServiceApi.md#get_intersection_by_address) | **GET** /streets/v1/intersection/byaddress | Nearest Intesection By Address.
[**get_intersection_by_location**](StreetsServiceApi.md#get_intersection_by_location) | **GET** /streets/v1/intersection/bylocation | Nearest Intesection By Location.
[**get_nearest_speed_limit**](StreetsServiceApi.md#get_nearest_speed_limit) | **GET** /streets/v1/speedlimit | Nearest Speedlimit.


# **get_intersection_by_address**
> IntersectionResponse get_intersection_by_address()

Nearest Intesection By Address.

This service accepts an address as input and returns the Nearest Intersection.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import streets_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.intersection_response import IntersectionResponse
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
    api_instance = streets_service_api.StreetsServiceApi(api_client)
    address = "address_example" # str | Address (optional)
    road_class = "roadClass_example" # str | Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All (optional)
    drive_time = "driveTime_example" # str | Returns Intersection in specified drive time (optional)
    drive_time_unit = "driveTimeUnit_example" # str | Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes (optional)
    search_radius = "searchRadius_example" # str | Search radius within which user wants to search, default is 50 miles (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Search radius unit, allowed values are (feet, meter, kilometers and miles) (optional)
    historic_speed = "historicSpeed_example" # str | Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT) (optional)
    max_candidates = "maxCandidates_example" # str | max candidates to be returned default is 1 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Nearest Intesection By Address.
        api_response = api_instance.get_intersection_by_address(address=address, road_class=road_class, drive_time=drive_time, drive_time_unit=drive_time_unit, search_radius=search_radius, search_radius_unit=search_radius_unit, historic_speed=historic_speed, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling StreetsServiceApi->get_intersection_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | [optional]
 **road_class** | **str**| Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All | [optional]
 **drive_time** | **str**| Returns Intersection in specified drive time | [optional]
 **drive_time_unit** | **str**| Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes | [optional]
 **search_radius** | **str**| Search radius within which user wants to search, default is 50 miles | [optional]
 **search_radius_unit** | **str**| Search radius unit, allowed values are (feet, meter, kilometers and miles) | [optional]
 **historic_speed** | **str**| Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT) | [optional]
 **max_candidates** | **str**| max candidates to be returned default is 1 | [optional]

### Return type

[**IntersectionResponse**](IntersectionResponse.md)

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

# **get_intersection_by_location**
> IntersectionResponse get_intersection_by_location()

Nearest Intesection By Location.

This service accepts latitude/longitude as input and returns the Nearest Intersection.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import streets_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.intersection_response import IntersectionResponse
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
    api_instance = streets_service_api.StreetsServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location. (optional)
    latitude = "latitude_example" # str | Latitude of the location. (optional)
    road_class = "roadClass_example" # str | Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All (optional)
    drive_time = "driveTime_example" # str | Returns Intersection in specified drive time (optional)
    drive_time_unit = "driveTimeUnit_example" # str | Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes (optional)
    search_radius = "searchRadius_example" # str | Search radius within which user wants to search, default is 50 miles (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Search radius unit, allowed values are (feet, meter, kilometers and miles) (optional)
    historic_speed = "historicSpeed_example" # str | Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT) (optional)
    max_candidates = "maxCandidates_example" # str | max candidates to be returned default is 1 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Nearest Intesection By Location.
        api_response = api_instance.get_intersection_by_location(longitude=longitude, latitude=latitude, road_class=road_class, drive_time=drive_time, drive_time_unit=drive_time_unit, search_radius=search_radius, search_radius_unit=search_radius_unit, historic_speed=historic_speed, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling StreetsServiceApi->get_intersection_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. | [optional]
 **latitude** | **str**| Latitude of the location. | [optional]
 **road_class** | **str**| Filters roads with specified class, allowed values are (Major, Secondary, Other and All), default is All | [optional]
 **drive_time** | **str**| Returns Intersection in specified drive time | [optional]
 **drive_time_unit** | **str**| Drive time unit, allowed values are (hours, minutes, seconds and milliseconds), default is minutes | [optional]
 **search_radius** | **str**| Search radius within which user wants to search, default is 50 miles | [optional]
 **search_radius_unit** | **str**| Search radius unit, allowed values are (feet, meter, kilometers and miles) | [optional]
 **historic_speed** | **str**| Traffic flow in peak time, allowed values are (AMPEAK,PMPEAK,OFFPEAK,NIGHT) | [optional]
 **max_candidates** | **str**| max candidates to be returned default is 1 | [optional]

### Return type

[**IntersectionResponse**](IntersectionResponse.md)

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

# **get_nearest_speed_limit**
> SpeedLimit get_nearest_speed_limit()

Nearest Speedlimit.

This service accepts point coordinates of a path as input and returns the posted speed limit of the road segment on which this path will snap.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import streets_service_api
from com.precisely.apis.model.speed_limit import SpeedLimit
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
    api_instance = streets_service_api.StreetsServiceApi(api_client)
    path = "path_example" # str | Accepts multiple points which will be snapped to the nearest road segment. Longitude and Latitude will be comma separated (longitude,latitude) and Point Coordinates will be separated by semi-colon(;) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Nearest Speedlimit.
        api_response = api_instance.get_nearest_speed_limit(path=path)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling StreetsServiceApi->get_nearest_speed_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Accepts multiple points which will be snapped to the nearest road segment. Longitude and Latitude will be comma separated (longitude,latitude) and Point Coordinates will be separated by semi-colon(;) | [optional]

### Return type

[**SpeedLimit**](SpeedLimit.md)

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

