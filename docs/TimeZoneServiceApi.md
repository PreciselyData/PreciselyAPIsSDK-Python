# com.precisely.apis.TimeZoneServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_timezone_by_location**](TimeZoneServiceApi.md#get_batch_timezone_by_location) | **POST** /timezone/v1/timezone/bylocation | Timezone Batch by Location.
[**get_timezone_by_address**](TimeZoneServiceApi.md#get_timezone_by_address) | **GET** /timezone/v1/timezone/byaddress | Timezone By Address.
[**get_timezone_by_address_batch**](TimeZoneServiceApi.md#get_timezone_by_address_batch) | **POST** /timezone/v1/timezone/byaddress | Timezone Batch by Address.
[**get_timezone_by_location**](TimeZoneServiceApi.md#get_timezone_by_location) | **GET** /timezone/v1/timezone/bylocation | Timezone By Location.


# **get_batch_timezone_by_location**
> TimezoneResponseList get_batch_timezone_by_location(timezone_location_request)

Timezone Batch by Location.

Identifies and retrieves the local time of any location in the world for a given latitude, longitude and time. The input and retrieved time format is in milliseconds.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import time_zone_service_api
from com.precisely.apis.model.timezone_location_request import TimezoneLocationRequest
from com.precisely.apis.model.timezone_response_list import TimezoneResponseList
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
    api_instance = time_zone_service_api.TimeZoneServiceApi(api_client)
    timezone_location_request = TimezoneLocationRequest(
        location_time=[
            LocationTime(
                geometry=TimezoneGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
                timestamp="timestamp_example",
            ),
        ],
    ) # TimezoneLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Timezone Batch by Location.
        api_response = api_instance.get_batch_timezone_by_location(timezone_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TimeZoneServiceApi->get_batch_timezone_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_location_request** | [**TimezoneLocationRequest**](TimezoneLocationRequest.md)|  |

### Return type

[**TimezoneResponseList**](TimezoneResponseList.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_by_address**
> TimezoneResponse get_timezone_by_address(timestamp, address)

Timezone By Address.

Identifies and retrieves the local time of any location in the world for a given address and time. The input and retrieved time format is in milliseconds.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import time_zone_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.timezone_response import TimezoneResponse
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
    api_instance = time_zone_service_api.TimeZoneServiceApi(api_client)
    timestamp = "timestamp_example" # str | Timestamp in miliseconds.
    address = "address_example" # str | The address to be searched.
    match_mode = "Relaxed" # str | Match modes determine the leniency used to make a match between the input address and the reference data (Default is relaxed) (optional)
    country = "USA" # str | Country ISO code (Default is USA) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Timezone By Address.
        api_response = api_instance.get_timezone_by_address(timestamp, address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TimeZoneServiceApi->get_timezone_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Timezone By Address.
        api_response = api_instance.get_timezone_by_address(timestamp, address, match_mode=match_mode, country=country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TimeZoneServiceApi->get_timezone_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp in miliseconds. |
 **address** | **str**| The address to be searched. |
 **match_mode** | **str**| Match modes determine the leniency used to make a match between the input address and the reference data (Default is relaxed) | [optional]
 **country** | **str**| Country ISO code (Default is USA) | [optional]

### Return type

[**TimezoneResponse**](TimezoneResponse.md)

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

# **get_timezone_by_address_batch**
> TimezoneResponseList get_timezone_by_address_batch(timezone_address_request)

Timezone Batch by Address.

Identifies and retrieves the local time of any location in the world for a given address and time. The input and retrieved time format is in milliseconds.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import time_zone_service_api
from com.precisely.apis.model.timezone_response_list import TimezoneResponseList
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.timezone_address_request import TimezoneAddressRequest
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
    api_instance = time_zone_service_api.TimeZoneServiceApi(api_client)
    timezone_address_request = TimezoneAddressRequest(
        preferences=PreferencTimeZone(
            match_mode="match_mode_example",
        ),
        address_time=[
            AddressTime(
                timestamp="timestamp_example",
                address=Address(
                    object_id="object_id_example",
                    display_name="display_name_example",
                    street_side="street_side_example",
                    business_name="business_name_example",
                    address_line1="address_line1_example",
                    address_line2="address_line2_example",
                    address_line3="address_line3_example",
                    city="city_example",
                    state_province="state_province_example",
                    county="county_example",
                    postal_code="postal_code_example",
                    latitude="latitude_example",
                    longitude="longitude_example",
                    status="status_example",
                    urbanization_name="urbanization_name_example",
                    formatted_address="formatted_address_example",
                    main_address_line="main_address_line_example",
                    address_last_line="address_last_line_example",
                    place_name="place_name_example",
                    area_name1="area_name1_example",
                    area_name2="area_name2_example",
                    area_name3="area_name3_example",
                    area_name4="area_name4_example",
                    post_code="post_code_example",
                    post_code_ext="post_code_ext_example",
                    country="country_example",
                    address_number="address_number_example",
                    street_name="street_name_example",
                    unit_type="unit_type_example",
                    unit_value="unit_value_example",
                ),
            ),
        ],
    ) # TimezoneAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Timezone Batch by Address.
        api_response = api_instance.get_timezone_by_address_batch(timezone_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TimeZoneServiceApi->get_timezone_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_address_request** | [**TimezoneAddressRequest**](TimezoneAddressRequest.md)|  |

### Return type

[**TimezoneResponseList**](TimezoneResponseList.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_by_location**
> TimezoneResponse get_timezone_by_location(timestamp, longitude, latitude)

Timezone By Location.

Identifies and retrieves the local time of any location in the world for a given latitude, longitude and time. The input and retrieved time format is in milliseconds.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import time_zone_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.timezone_response import TimezoneResponse
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
    api_instance = time_zone_service_api.TimeZoneServiceApi(api_client)
    timestamp = "timestamp_example" # str | Timestamp in miliseconds.
    longitude = "longitude_example" # str | Longitude of the location.
    latitude = "latitude_example" # str | Latitude of the location.

    # example passing only required values which don't have defaults set
    try:
        # Timezone By Location.
        api_response = api_instance.get_timezone_by_location(timestamp, longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TimeZoneServiceApi->get_timezone_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **str**| Timestamp in miliseconds. |
 **longitude** | **str**| Longitude of the location. |
 **latitude** | **str**| Latitude of the location. |

### Return type

[**TimezoneResponse**](TimezoneResponse.md)

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

