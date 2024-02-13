# com.precisely.apis.DemographicsServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_demographics_advanced**](DemographicsServiceApi.md#get_demographics_advanced) | **POST** /demographics-segmentation/v1/advanced/demographics | Demographics Advanced Endpoint
[**get_demographics_basic**](DemographicsServiceApi.md#get_demographics_basic) | **GET** /demographics-segmentation/v1/basic/demographics | Demographics Basic
[**get_demographics_by_address**](DemographicsServiceApi.md#get_demographics_by_address) | **GET** /demographics-segmentation/v1/demographics/byaddress | Demographics By Address.
[**get_demographics_by_boundary_ids**](DemographicsServiceApi.md#get_demographics_by_boundary_ids) | **GET** /demographics-segmentation/v1/demographics/byboundaryids | Demographics By Boundaryids.
[**get_demographics_by_location**](DemographicsServiceApi.md#get_demographics_by_location) | **GET** /demographics-segmentation/v1/demographics/bylocation | Demographics By Location.
[**get_segmentation_by_address**](DemographicsServiceApi.md#get_segmentation_by_address) | **GET** /demographics-segmentation/v1/segmentation/byaddress | Segmentation By Address.
[**get_segmentation_by_location**](DemographicsServiceApi.md#get_segmentation_by_location) | **GET** /demographics-segmentation/v1/segmentation/bylocation | Segmentation By Location.


# **get_demographics_advanced**
> Demographics get_demographics_advanced(demographics_advanced_request)

Demographics Advanced Endpoint

Demographics Advanced Endpoint will return the aggregated values of the selected demographics variables of the regions falling inside a user provided geometry or travel time/distance boundaries. All the intersecting demographic boundaries will be snapped completely, and user will have option to request these boundaries in response.  

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.demographics_advanced_request import DemographicsAdvancedRequest
from com.precisely.apis.model.demographics import Demographics
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    demographics_advanced_request = DemographicsAdvancedRequest(
        preferences=DemographicsAdvancedPreferences(
            profile="profile_example",
            filter="filter_example",
            include_geometry="include_geometry_example",
        ),
        geometry=DemographicsGeometry(
            type="type_example",
            crs=DemographicsGeometryCRC(
                type="type_example",
                properties=GeometryProperties(
                    name="name_example",
                ),
            ),
            coordinates={},
        ),
        geometry_as_text="geometry_as_text_example",
    ) # DemographicsAdvancedRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Demographics Advanced Endpoint
        api_response = api_instance.get_demographics_advanced(demographics_advanced_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_advanced: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **demographics_advanced_request** | [**DemographicsAdvancedRequest**](DemographicsAdvancedRequest.md)|  |

### Return type

[**Demographics**](Demographics.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_demographics_basic**
> Demographics get_demographics_basic()

Demographics Basic

Demographics Basic Endpoint will return the aggregated values of the selected demographics variables of the regions falling inside the search radius. All the intersecting demographic boundaries will be snapped completely and user will have option to request these boundaries in response.  

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.demographics import Demographics
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    address = "address_example" # str | Address to be searched (optional)
    longitude = "longitude_example" # str | Longitude of the location (optional)
    latitude = "latitude_example" # str | Latitude of the location (optional)
    search_radius = "searchRadius_example" # str | Radius within which demographics details are required. Max. value is 52800 Feet or 10 miles (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Radius unit such as Feet, Kilometers, Miles or Meters  (optional)
    travel_time = "travelTime_example" # str | Travel Time based on ‘travelMode’ within which demographics details are required. Max. value is 1 hour. (optional)
    travel_time_unit = "travelTimeUnit_example" # str | minutes,hours,seconds,milliseconds. Default is meters.Default is minutes. (optional)
    travel_distance = "travelDistance_example" # str | Travel Distance based on ‘travelMode’ within which demographics details are required. Max. value is 10 miles. (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | feet,kilometers,miles,meters.  Default is feet. (optional)
    travel_mode = "travelMode_example" # str | Default is driving. (optional)
    country = "country_example" # str | 3 digit ISO country code (Used in case address is mentioned). (optional)
    profile = "profile_example" # str | Applicable on ranged variables. Returns top sorted result based on the input value. (optional)
    filter = "filter_example" # str | If Y, demographic boundaries are returned in response. (optional)
    include_geometry = "includeGeometry_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Demographics Basic
        api_response = api_instance.get_demographics_basic(address=address, longitude=longitude, latitude=latitude, search_radius=search_radius, search_radius_unit=search_radius_unit, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, travel_mode=travel_mode, country=country, profile=profile, filter=filter, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_basic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address to be searched | [optional]
 **longitude** | **str**| Longitude of the location | [optional]
 **latitude** | **str**| Latitude of the location | [optional]
 **search_radius** | **str**| Radius within which demographics details are required. Max. value is 52800 Feet or 10 miles | [optional]
 **search_radius_unit** | **str**| Radius unit such as Feet, Kilometers, Miles or Meters  | [optional]
 **travel_time** | **str**| Travel Time based on ‘travelMode’ within which demographics details are required. Max. value is 1 hour. | [optional]
 **travel_time_unit** | **str**| minutes,hours,seconds,milliseconds. Default is meters.Default is minutes. | [optional]
 **travel_distance** | **str**| Travel Distance based on ‘travelMode’ within which demographics details are required. Max. value is 10 miles. | [optional]
 **travel_distance_unit** | **str**| feet,kilometers,miles,meters.  Default is feet. | [optional]
 **travel_mode** | **str**| Default is driving. | [optional]
 **country** | **str**| 3 digit ISO country code (Used in case address is mentioned). | [optional]
 **profile** | **str**| Applicable on ranged variables. Returns top sorted result based on the input value. | [optional]
 **filter** | **str**| If Y, demographic boundaries are returned in response. | [optional]
 **include_geometry** | **str**|  | [optional]

### Return type

[**Demographics**](Demographics.md)

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

# **get_demographics_by_address**
> Demographics get_demographics_by_address(address)

Demographics By Address.

Provides the demographic details around a specified address. GeoLife 'byaddress' service accepts address as an input to return a specific population segment's age group, ethnicity, income, purchasing behaviour, commuter patterns and more.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.demographics import Demographics
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    address = "address_example" # str | The address to be searched.
    country = "country_example" # str | 3 letter ISO code of the country to be searched.Allowed values USA,CAN,GBR,AUS. (optional)
    profile = "profile_example" # str | Retrieves the sorted demographic data on the basis of pre-defined profiles that can display the top 3 or top 5 results (by location) either in ascending or descending order.Allowed values Top5Ascending,Top5Descending,Top3Ascending,Top3Descending (optional)
    filter = "filter_example" # str | The 'filter' parameter retrieves the demographic data based upon specified input themes. (optional)
    value_format = "valueFormat_example" # str | The 'valueFormat' parameter is applicable for few ranged variables where percent & count both are available and filter response based on the input value. (optional)
    variable_level = "variableLevel_example" # str | The 'variableLevel' retrieves demographic facts in response based on the input value (optional)

    # example passing only required values which don't have defaults set
    try:
        # Demographics By Address.
        api_response = api_instance.get_demographics_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Demographics By Address.
        api_response = api_instance.get_demographics_by_address(address, country=country, profile=profile, filter=filter, value_format=value_format, variable_level=variable_level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |
 **country** | **str**| 3 letter ISO code of the country to be searched.Allowed values USA,CAN,GBR,AUS. | [optional]
 **profile** | **str**| Retrieves the sorted demographic data on the basis of pre-defined profiles that can display the top 3 or top 5 results (by location) either in ascending or descending order.Allowed values Top5Ascending,Top5Descending,Top3Ascending,Top3Descending | [optional]
 **filter** | **str**| The &#39;filter&#39; parameter retrieves the demographic data based upon specified input themes. | [optional]
 **value_format** | **str**| The &#39;valueFormat&#39; parameter is applicable for few ranged variables where percent &amp; count both are available and filter response based on the input value. | [optional]
 **variable_level** | **str**| The &#39;variableLevel&#39; retrieves demographic facts in response based on the input value | [optional]

### Return type

[**Demographics**](Demographics.md)

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

# **get_demographics_by_boundary_ids**
> Demographics get_demographics_by_boundary_ids()

Demographics By Boundaryids.

This endpoint will allow the user to request demographics details by census boundary id. Multiple comma separated boundary ids will be accepted. 

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.demographics import Demographics
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    boundary_ids = "boundaryIds_example" # str | Accepts comma separated multiple boundary ids. (optional)
    profile = "profile_example" # str | Applicable on ranged variables. Returns top sorted result based on the input value. (optional)
    filter = "filter_example" # str | Accept the comma separated theme names and filter response based on value. Maximum 10 can be provided. (optional)
    value_format = "valueFormat_example" # str | Applicable for few ranged variables where percent & count both are available and filter response based on the input value. (optional)
    variable_level = "variableLevel_example" # str | Retrieves demographic facts in response based on the input value. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Demographics By Boundaryids.
        api_response = api_instance.get_demographics_by_boundary_ids(boundary_ids=boundary_ids, profile=profile, filter=filter, value_format=value_format, variable_level=variable_level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_by_boundary_ids: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boundary_ids** | **str**| Accepts comma separated multiple boundary ids. | [optional]
 **profile** | **str**| Applicable on ranged variables. Returns top sorted result based on the input value. | [optional]
 **filter** | **str**| Accept the comma separated theme names and filter response based on value. Maximum 10 can be provided. | [optional]
 **value_format** | **str**| Applicable for few ranged variables where percent &amp; count both are available and filter response based on the input value. | [optional]
 **variable_level** | **str**| Retrieves demographic facts in response based on the input value. | [optional]

### Return type

[**Demographics**](Demographics.md)

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

# **get_demographics_by_location**
> Demographics get_demographics_by_location()

Demographics By Location.

Provides the demographic details around a specified location. GeoLife 'bylocation' service accepts longitude and latitude as an input to return a specific population segment's age group, ethnicity, income, purchasing behaviour, commuter patterns and more.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.demographics import Demographics
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location. (optional)
    latitude = "latitude_example" # str | Latitude of the location. (optional)
    profile = "profile_example" # str | Retrieves the sorted demographic data on the basis of pre-defined profiles that can display the top 3 or top 5 results (by location) either in ascending or descending order.Allowed values Top5Ascending,Top5Descending,Top3Ascending,Top3Descending (optional)
    filter = "filter_example" # str | The 'filter' parameter retrieves the demographic data based upon specified input themes. (optional)
    value_format = "valueFormat_example" # str | The 'valueFormat' parameter is applicable for few ranged variables where percent & count both are available and filter response based on the input value. (optional)
    variable_level = "variableLevel_example" # str | The 'variableLevel' retrieves demographic facts in response based on the input value (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Demographics By Location.
        api_response = api_instance.get_demographics_by_location(longitude=longitude, latitude=latitude, profile=profile, filter=filter, value_format=value_format, variable_level=variable_level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_demographics_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. | [optional]
 **latitude** | **str**| Latitude of the location. | [optional]
 **profile** | **str**| Retrieves the sorted demographic data on the basis of pre-defined profiles that can display the top 3 or top 5 results (by location) either in ascending or descending order.Allowed values Top5Ascending,Top5Descending,Top3Ascending,Top3Descending | [optional]
 **filter** | **str**| The &#39;filter&#39; parameter retrieves the demographic data based upon specified input themes. | [optional]
 **value_format** | **str**| The &#39;valueFormat&#39; parameter is applicable for few ranged variables where percent &amp; count both are available and filter response based on the input value. | [optional]
 **variable_level** | **str**| The &#39;variableLevel&#39; retrieves demographic facts in response based on the input value | [optional]

### Return type

[**Demographics**](Demographics.md)

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

# **get_segmentation_by_address**
> Segmentation get_segmentation_by_address(address)

Segmentation By Address.

Provides the segmentation details around a specified address. GeoLife 'Segmentation by Address' service accepts address as an input to return the lifestyle characteristics of households in terms of their family status, children characteristics, income behaviors, financial preferences and interests.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.segmentation import Segmentation
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    address = "address_example" # str | The address to be searched.
    country = "country_example" # str | 3 letter ISO code of the country to be searched.Allowed values USA,CAN,GBR,FRA,ITA,AUS,DEU. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Segmentation By Address.
        api_response = api_instance.get_segmentation_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_segmentation_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Segmentation By Address.
        api_response = api_instance.get_segmentation_by_address(address, country=country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_segmentation_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |
 **country** | **str**| 3 letter ISO code of the country to be searched.Allowed values USA,CAN,GBR,FRA,ITA,AUS,DEU. | [optional]

### Return type

[**Segmentation**](Segmentation.md)

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

# **get_segmentation_by_location**
> Segmentation get_segmentation_by_location(longitude, latitude)

Segmentation By Location.

Provides the segmentation details around a specified location. GeoLife 'segmentation bylocation' service accepts longitude and latitude as an input to return the lifestyle characteristics of households in terms of their family status, children characteristics, income behaviors, financial preferences and interests.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import demographics_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.segmentation import Segmentation
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
    api_instance = demographics_service_api.DemographicsServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location.
    latitude = "latitude_example" # str | Latitude of the location.

    # example passing only required values which don't have defaults set
    try:
        # Segmentation By Location.
        api_response = api_instance.get_segmentation_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling DemographicsServiceApi->get_segmentation_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. |
 **latitude** | **str**| Latitude of the location. |

### Return type

[**Segmentation**](Segmentation.md)

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

