# com.precisely.apis.RisksServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_crime_risk_by_address**](RisksServiceApi.md#get_crime_risk_by_address) | **GET** /risks/v1/crime/byaddress | Get Crime Risk By Address
[**get_crime_risk_by_address_batch**](RisksServiceApi.md#get_crime_risk_by_address_batch) | **POST** /risks/v1/crime/byaddress | Post Crime Risk By Address
[**get_crime_risk_by_location**](RisksServiceApi.md#get_crime_risk_by_location) | **GET** /risks/v1/crime/bylocation | Get Crime Risk By  Location
[**get_crime_risk_by_location_batch**](RisksServiceApi.md#get_crime_risk_by_location_batch) | **POST** /risks/v1/crime/bylocation | Post Crime Risk By Location
[**get_distance_to_coast_by_address**](RisksServiceApi.md#get_distance_to_coast_by_address) | **GET** /risks/v1/shoreline/distancetofloodhazard/byaddress | Get Distance To Flood Hazard By Address
[**get_distance_to_coast_by_address_batch**](RisksServiceApi.md#get_distance_to_coast_by_address_batch) | **POST** /risks/v1/shoreline/distancetofloodhazard/byaddress | Post Distance To Flood Hazard By Address
[**get_distance_to_coast_by_location**](RisksServiceApi.md#get_distance_to_coast_by_location) | **GET** /risks/v1/shoreline/distancetofloodhazard/bylocation | Get Distance To Flood Hazard By Location
[**get_distance_to_coast_by_location_batch**](RisksServiceApi.md#get_distance_to_coast_by_location_batch) | **POST** /risks/v1/shoreline/distancetofloodhazard/bylocation | Post Distance To Flood Hazard By Location
[**get_earthquake_history**](RisksServiceApi.md#get_earthquake_history) | **GET** /risks/v1/earthquakehistory | Earthquake History
[**get_earthquake_risk_by_address**](RisksServiceApi.md#get_earthquake_risk_by_address) | **GET** /risks/v1/earthquake/byaddress | Get Earthquake Risk By Address
[**get_earthquake_risk_by_address_batch**](RisksServiceApi.md#get_earthquake_risk_by_address_batch) | **POST** /risks/v1/earthquake/byaddress | Post Earthquake Risk By Address
[**get_earthquake_risk_by_location**](RisksServiceApi.md#get_earthquake_risk_by_location) | **GET** /risks/v1/earthquake/bylocation | Get Earthquake Risk By Location
[**get_earthquake_risk_by_location_batch**](RisksServiceApi.md#get_earthquake_risk_by_location_batch) | **POST** /risks/v1/earthquake/bylocation | Post Earthquake Risk By Location
[**get_fire_history**](RisksServiceApi.md#get_fire_history) | **GET** /risks/v1/firehistory | Get Fire History
[**get_fire_history_v2**](RisksServiceApi.md#get_fire_history_v2) | **GET** /risks/v2/firehistory | Get Fire History
[**get_fire_risk_by_address**](RisksServiceApi.md#get_fire_risk_by_address) | **GET** /risks/v1/fire/byaddress | Get Fire Risk By Address
[**get_fire_risk_by_address_batch**](RisksServiceApi.md#get_fire_risk_by_address_batch) | **POST** /risks/v1/fire/byaddress | Post Fire Risk By Address
[**get_fire_risk_by_location**](RisksServiceApi.md#get_fire_risk_by_location) | **GET** /risks/v1/fire/bylocation | Get Fire Risk By Location
[**get_fire_risk_by_location_batch**](RisksServiceApi.md#get_fire_risk_by_location_batch) | **POST** /risks/v1/fire/bylocation | Post Fire Risk By Location
[**get_fire_risk_v2_by_address**](RisksServiceApi.md#get_fire_risk_v2_by_address) | **GET** /risks/v2/fire/byaddress | Get Fire Risk By Address
[**get_fire_risk_v2_by_address_batch**](RisksServiceApi.md#get_fire_risk_v2_by_address_batch) | **POST** /risks/v2/fire/byaddress | Post Fire Risk By Address
[**get_fire_risk_v2_by_location**](RisksServiceApi.md#get_fire_risk_v2_by_location) | **GET** /risks/v2/fire/bylocation | Get Fire Risk By Location
[**get_fire_risk_v2_by_location_batch**](RisksServiceApi.md#get_fire_risk_v2_by_location_batch) | **POST** /risks/v2/fire/bylocation | Post Fire Risk By Location
[**get_fire_station_by_address**](RisksServiceApi.md#get_fire_station_by_address) | **GET** /risks/v1/firestation/byaddress | Get Fire Station By Address
[**get_fire_station_by_location**](RisksServiceApi.md#get_fire_station_by_location) | **GET** /risks/v1/firestation/bylocation | Get Fire Station By Location
[**get_flood_risk_by_address**](RisksServiceApi.md#get_flood_risk_by_address) | **GET** /risks/v1/flood/byaddress | Get Flood Risk By Address
[**get_flood_risk_by_address_batch**](RisksServiceApi.md#get_flood_risk_by_address_batch) | **POST** /risks/v1/flood/byaddress | Post Flood Risk By Address
[**get_flood_risk_by_location**](RisksServiceApi.md#get_flood_risk_by_location) | **GET** /risks/v1/flood/bylocation | Get Flood Risk By Location
[**get_flood_risk_by_location_batch**](RisksServiceApi.md#get_flood_risk_by_location_batch) | **POST** /risks/v1/flood/bylocation | Post Flood Risk By Location


# **get_crime_risk_by_address**
> CrimeRiskResponse get_crime_risk_by_address(address)

Get Crime Risk By Address

Accepts addresses as input and Returns local crime indexes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.crime_risk_response import CrimeRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | free form address text
    type = "type_example" # str | this is crime type; valid values are following 11 crime types with 'all' as default (more than one can also be given as comma separated types) (optional)
    include_geometry = "includeGeometry_example" # str | Y or N (default is N) - if it is Y, then geometry will be part of response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Crime Risk By Address
        api_response = api_instance.get_crime_risk_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Crime Risk By Address
        api_response = api_instance.get_crime_risk_by_address(address, type=type, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| free form address text |
 **type** | **str**| this is crime type; valid values are following 11 crime types with &#39;all&#39; as default (more than one can also be given as comma separated types) | [optional]
 **include_geometry** | **str**| Y or N (default is N) - if it is Y, then geometry will be part of response | [optional]

### Return type

[**CrimeRiskResponse**](CrimeRiskResponse.md)

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

# **get_crime_risk_by_address_batch**
> CrimeRiskResponseList get_crime_risk_by_address_batch(crime_risk_by_address_batch_request)

Post Crime Risk By Address

This is a Batch offering for 'Crime Risk By Address' service. It accepts a single address or a list of addresses and retrieve local crime indexes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.crime_risk_by_address_batch_request import CrimeRiskByAddressBatchRequest
from com.precisely.apis.model.crime_risk_response_list import CrimeRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    crime_risk_by_address_batch_request = CrimeRiskByAddressBatchRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=CrimeRiskPreferences(
            include_geometry="include_geometry_example",
            type="type_example",
        ),
    ) # CrimeRiskByAddressBatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Crime Risk By Address
        api_response = api_instance.get_crime_risk_by_address_batch(crime_risk_by_address_batch_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_risk_by_address_batch_request** | [**CrimeRiskByAddressBatchRequest**](CrimeRiskByAddressBatchRequest.md)|  |

### Return type

[**CrimeRiskResponseList**](CrimeRiskResponseList.md)

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

# **get_crime_risk_by_location**
> CrimeRiskResponse get_crime_risk_by_location(longitude, latitude)

Get Crime Risk By  Location

Accepts latitude/longitude as input and returns and Returns local crime indexes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.crime_risk_response import CrimeRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | The longitude of the location
    latitude = "latitude_example" # str | The latitude of the location
    type = "type_example" # str | this is crime type; valid values are following 11 crime types with 'all' as default (more than one can also be given as comma separated types) (optional)
    include_geometry = "includeGeometry_example" # str | Y or N (default is N) - if it is Y, then geometry will be part of response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Crime Risk By  Location
        api_response = api_instance.get_crime_risk_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Crime Risk By  Location
        api_response = api_instance.get_crime_risk_by_location(longitude, latitude, type=type, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| The longitude of the location |
 **latitude** | **str**| The latitude of the location |
 **type** | **str**| this is crime type; valid values are following 11 crime types with &#39;all&#39; as default (more than one can also be given as comma separated types) | [optional]
 **include_geometry** | **str**| Y or N (default is N) - if it is Y, then geometry will be part of response | [optional]

### Return type

[**CrimeRiskResponse**](CrimeRiskResponse.md)

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

# **get_crime_risk_by_location_batch**
> CrimeRiskResponseList get_crime_risk_by_location_batch(crime_risk_by_location_batch_request)

Post Crime Risk By Location

This is a Batch offering for 'Crime Risk By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve local crime indexes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.crime_risk_response_list import CrimeRiskResponseList
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.crime_risk_by_location_batch_request import CrimeRiskByLocationBatchRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    crime_risk_by_location_batch_request = CrimeRiskByLocationBatchRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=CrimeRiskPreferences(
            include_geometry="include_geometry_example",
            type="type_example",
        ),
    ) # CrimeRiskByLocationBatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Crime Risk By Location
        api_response = api_instance.get_crime_risk_by_location_batch(crime_risk_by_location_batch_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_crime_risk_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crime_risk_by_location_batch_request** | [**CrimeRiskByLocationBatchRequest**](CrimeRiskByLocationBatchRequest.md)|  |

### Return type

[**CrimeRiskResponseList**](CrimeRiskResponseList.md)

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

# **get_distance_to_coast_by_address**
> WaterBodyResponse get_distance_to_coast_by_address()

Get Distance To Flood Hazard By Address

Accepts addresses as input and Returns the distance from nearest water bodies along with body name and location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.water_body_response import WaterBodyResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | The address of the location (optional)
    max_candidates = "maxCandidates_example" # str | This specifies the value of maxCandidates (optional)
    water_body_type = "waterBodyType_example" # str | This specifies the value of waterBodyType (optional)
    search_distance = "searchDistance_example" # str | This specifies the search distance (optional)
    search_distance_unit = "searchDistanceUnit_example" # str | miles (default value),feet, kilometers, meters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Distance To Flood Hazard By Address
        api_response = api_instance.get_distance_to_coast_by_address(address=address, max_candidates=max_candidates, water_body_type=water_body_type, search_distance=search_distance, search_distance_unit=search_distance_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_distance_to_coast_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address of the location | [optional]
 **max_candidates** | **str**| This specifies the value of maxCandidates | [optional]
 **water_body_type** | **str**| This specifies the value of waterBodyType | [optional]
 **search_distance** | **str**| This specifies the search distance | [optional]
 **search_distance_unit** | **str**| miles (default value),feet, kilometers, meters | [optional]

### Return type

[**WaterBodyResponse**](WaterBodyResponse.md)

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

# **get_distance_to_coast_by_address_batch**
> DistanceToFloodHazardResponse get_distance_to_coast_by_address_batch(distance_to_flood_hazard_address_request)

Post Distance To Flood Hazard By Address

This is a Batch offering for 'Distance To Flood Hazard By Address' service. It accepts a single address or a list of addresses and retrieve the distance from nearest water bodies along with body name and location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.distance_to_flood_hazard_response import DistanceToFloodHazardResponse
from com.precisely.apis.model.distance_to_flood_hazard_address_request import DistanceToFloodHazardAddressRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    distance_to_flood_hazard_address_request = DistanceToFloodHazardAddressRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=FloodHazardPreferences(
            water_body_type="water_body_type_example",
            max_candidates="max_candidates_example",
            search_distance="search_distance_example",
            search_distance_unit="search_distance_unit_example",
        ),
    ) # DistanceToFloodHazardAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Distance To Flood Hazard By Address
        api_response = api_instance.get_distance_to_coast_by_address_batch(distance_to_flood_hazard_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_distance_to_coast_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distance_to_flood_hazard_address_request** | [**DistanceToFloodHazardAddressRequest**](DistanceToFloodHazardAddressRequest.md)|  |

### Return type

[**DistanceToFloodHazardResponse**](DistanceToFloodHazardResponse.md)

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

# **get_distance_to_coast_by_location**
> WaterBodyResponse get_distance_to_coast_by_location()

Get Distance To Flood Hazard By Location

Accepts latitude & longitude as input and Returns the distance from nearest water bodies along with body name and location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.water_body_response import WaterBodyResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | The longitude of the location (optional)
    latitude = "latitude_example" # str | The latitude of the location (optional)
    max_candidates = "maxCandidates_example" # str | This specifies the value of maxCandidates (optional)
    water_body_type = "waterBodyType_example" # str | This specifies the value of waterBodyType (optional)
    search_distance = "searchDistance_example" # str | This specifies the search distance (optional)
    search_distance_unit = "searchDistanceUnit_example" # str | miles (default value),feet, kilometers, meters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Distance To Flood Hazard By Location
        api_response = api_instance.get_distance_to_coast_by_location(longitude=longitude, latitude=latitude, max_candidates=max_candidates, water_body_type=water_body_type, search_distance=search_distance, search_distance_unit=search_distance_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_distance_to_coast_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| The longitude of the location | [optional]
 **latitude** | **str**| The latitude of the location | [optional]
 **max_candidates** | **str**| This specifies the value of maxCandidates | [optional]
 **water_body_type** | **str**| This specifies the value of waterBodyType | [optional]
 **search_distance** | **str**| This specifies the search distance | [optional]
 **search_distance_unit** | **str**| miles (default value),feet, kilometers, meters | [optional]

### Return type

[**WaterBodyResponse**](WaterBodyResponse.md)

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

# **get_distance_to_coast_by_location_batch**
> DistanceToFloodHazardResponse get_distance_to_coast_by_location_batch(distance_to_flood_hazard_location_request)

Post Distance To Flood Hazard By Location

This is a Batch offering for 'Distance To Flood Hazard By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve the distance from nearest water bodies along with body name and location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.distance_to_flood_hazard_response import DistanceToFloodHazardResponse
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.distance_to_flood_hazard_location_request import DistanceToFloodHazardLocationRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    distance_to_flood_hazard_location_request = DistanceToFloodHazardLocationRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=FloodHazardPreferences(
            water_body_type="water_body_type_example",
            max_candidates="max_candidates_example",
            search_distance="search_distance_example",
            search_distance_unit="search_distance_unit_example",
        ),
    ) # DistanceToFloodHazardLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Distance To Flood Hazard By Location
        api_response = api_instance.get_distance_to_coast_by_location_batch(distance_to_flood_hazard_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_distance_to_coast_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distance_to_flood_hazard_location_request** | [**DistanceToFloodHazardLocationRequest**](DistanceToFloodHazardLocationRequest.md)|  |

### Return type

[**DistanceToFloodHazardResponse**](DistanceToFloodHazardResponse.md)

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

# **get_earthquake_history**
> EarthquakeHistory get_earthquake_history(post_code)

Earthquake History

Accepts postcode as input and Returns historical earthquake details for a particular postcode.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.earthquake_history import EarthquakeHistory
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    post_code = "postCode_example" # str | 5 digit Postal code to search
    start_date = "startDate_example" # str | Start time in milliseconds(UTC) (optional)
    end_date = "endDate_example" # str | End time in milliseconds(UTC) (optional)
    min_magnitude = "minMagnitude_example" # str | Minimum richter scale magnitude (optional)
    max_magnitude = "maxMagnitude_example" # str | Maximum Richter scale magnitude (optional)
    max_candidates = "maxCandidates_example" # str | Maximum response events (optional)

    # example passing only required values which don't have defaults set
    try:
        # Earthquake History
        api_response = api_instance.get_earthquake_history(post_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Earthquake History
        api_response = api_instance.get_earthquake_history(post_code, start_date=start_date, end_date=end_date, min_magnitude=min_magnitude, max_magnitude=max_magnitude, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_code** | **str**| 5 digit Postal code to search |
 **start_date** | **str**| Start time in milliseconds(UTC) | [optional]
 **end_date** | **str**| End time in milliseconds(UTC) | [optional]
 **min_magnitude** | **str**| Minimum richter scale magnitude | [optional]
 **max_magnitude** | **str**| Maximum Richter scale magnitude | [optional]
 **max_candidates** | **str**| Maximum response events | [optional]

### Return type

[**EarthquakeHistory**](EarthquakeHistory.md)

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

# **get_earthquake_risk_by_address**
> EarthquakeRiskResponse get_earthquake_risk_by_address(address)

Get Earthquake Risk By Address

Accepts addresses as input and Returns counts of earthquakes for various richter measurements and values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.earthquake_risk_response import EarthquakeRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | free form address text
    richter_value = "richterValue_example" # str | all (default value), R0, R1, R2, R3, R4, R5, R6, R7, R0_GE, R1_GE, R2_GE, R3_GE, R4_GE, R5_GE, R6_GE, R7_GE (optional)
    include_geometry = "includeGeometry_example" # str | Y or N (default is N) - if it is Y, then geometry will be part of response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Earthquake Risk By Address
        api_response = api_instance.get_earthquake_risk_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Earthquake Risk By Address
        api_response = api_instance.get_earthquake_risk_by_address(address, richter_value=richter_value, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| free form address text |
 **richter_value** | **str**| all (default value), R0, R1, R2, R3, R4, R5, R6, R7, R0_GE, R1_GE, R2_GE, R3_GE, R4_GE, R5_GE, R6_GE, R7_GE | [optional]
 **include_geometry** | **str**| Y or N (default is N) - if it is Y, then geometry will be part of response | [optional]

### Return type

[**EarthquakeRiskResponse**](EarthquakeRiskResponse.md)

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

# **get_earthquake_risk_by_address_batch**
> EarthquakeRiskResponseList get_earthquake_risk_by_address_batch(earthquake_risk_by_address_request)

Post Earthquake Risk By Address

This is a Batch offering for 'Earthquake Risk By Address' service. It accepts a single address or a list of addresses and retrieve counts of earthquakes for various richter measurements and values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.earthquake_risk_by_address_request import EarthquakeRiskByAddressRequest
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.earthquake_risk_response_list import EarthquakeRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    earthquake_risk_by_address_request = EarthquakeRiskByAddressRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # EarthquakeRiskByAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Earthquake Risk By Address
        api_response = api_instance.get_earthquake_risk_by_address_batch(earthquake_risk_by_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earthquake_risk_by_address_request** | [**EarthquakeRiskByAddressRequest**](EarthquakeRiskByAddressRequest.md)|  |

### Return type

[**EarthquakeRiskResponseList**](EarthquakeRiskResponseList.md)

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

# **get_earthquake_risk_by_location**
> EarthquakeRiskResponse get_earthquake_risk_by_location(longitude, latitude)

Get Earthquake Risk By Location

Accepts latitude & longitude as input and Returns counts of earthquakes for various richter measurements and values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.earthquake_risk_response import EarthquakeRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | The longitude of the location
    latitude = "latitude_example" # str | The latitude of the location
    richter_value = "richterValue_example" # str | all (default value), R0, R1, R2, R3, R4, R5, R6, R7, R0_GE, R1_GE, R2_GE, R3_GE, R4_GE, R5_GE, R6_GE, R7_GE (optional)
    include_geometry = "includeGeometry_example" # str | Y or N (default is N) - if it is Y, then geometry will be part of response (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Earthquake Risk By Location
        api_response = api_instance.get_earthquake_risk_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Earthquake Risk By Location
        api_response = api_instance.get_earthquake_risk_by_location(longitude, latitude, richter_value=richter_value, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| The longitude of the location |
 **latitude** | **str**| The latitude of the location |
 **richter_value** | **str**| all (default value), R0, R1, R2, R3, R4, R5, R6, R7, R0_GE, R1_GE, R2_GE, R3_GE, R4_GE, R5_GE, R6_GE, R7_GE | [optional]
 **include_geometry** | **str**| Y or N (default is N) - if it is Y, then geometry will be part of response | [optional]

### Return type

[**EarthquakeRiskResponse**](EarthquakeRiskResponse.md)

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

# **get_earthquake_risk_by_location_batch**
> EarthquakeRiskResponseList get_earthquake_risk_by_location_batch(earthquake_risk_by_location_request)

Post Earthquake Risk By Location

This is a Batch offering for 'Earthquake Risk By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve counts of earthquakes for various richter measurements and values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.earthquake_risk_by_location_request import EarthquakeRiskByLocationRequest
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.earthquake_risk_response_list import EarthquakeRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    earthquake_risk_by_location_request = EarthquakeRiskByLocationRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # EarthquakeRiskByLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Earthquake Risk By Location
        api_response = api_instance.get_earthquake_risk_by_location_batch(earthquake_risk_by_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_earthquake_risk_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earthquake_risk_by_location_request** | [**EarthquakeRiskByLocationRequest**](EarthquakeRiskByLocationRequest.md)|  |

### Return type

[**EarthquakeRiskResponseList**](EarthquakeRiskResponseList.md)

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

# **get_fire_history**
> FireHistory get_fire_history(post_code)

Get Fire History

Accepts postcode as input and Returns fire event details for a particular postcode.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.fire_history import FireHistory
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    post_code = "postCode_example" # str | 5 digit Postal code to search
    start_date = "startDate_example" # str | Start time in milliseconds(UTC) (optional)
    end_date = "endDate_example" # str | End time in milliseconds(UTC) (optional)
    max_candidates = "maxCandidates_example" # str | Maximum response events (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire History
        api_response = api_instance.get_fire_history(post_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire History
        api_response = api_instance.get_fire_history(post_code, start_date=start_date, end_date=end_date, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_code** | **str**| 5 digit Postal code to search |
 **start_date** | **str**| Start time in milliseconds(UTC) | [optional]
 **end_date** | **str**| End time in milliseconds(UTC) | [optional]
 **max_candidates** | **str**| Maximum response events | [optional]

### Return type

[**FireHistory**](FireHistory.md)

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

# **get_fire_history_v2**
> FireHistoryV2 get_fire_history_v2(post_code)

Get Fire History

Accepts postcode as input and Returns fire event details for a particular postcode.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.fire_history_v2 import FireHistoryV2
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    post_code = "postCode_example" # str | 5 digit Postal code to search
    start_date = "startDate_example" # str | Start time in milliseconds(UTC) (optional)
    end_date = "endDate_example" # str | End time in milliseconds(UTC) (optional)
    max_candidates = "maxCandidates_example" # str | Maximum response events (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire History
        api_response = api_instance.get_fire_history_v2(post_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_history_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire History
        api_response = api_instance.get_fire_history_v2(post_code, start_date=start_date, end_date=end_date, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_history_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_code** | **str**| 5 digit Postal code to search |
 **start_date** | **str**| Start time in milliseconds(UTC) | [optional]
 **end_date** | **str**| End time in milliseconds(UTC) | [optional]
 **max_candidates** | **str**| Maximum response events | [optional]

### Return type

[**FireHistoryV2**](FireHistoryV2.md)

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

# **get_fire_risk_by_address**
> FireRiskResponse get_fire_risk_by_address(address)

Get Fire Risk By Address

Accepts addresses as input and Returns fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_response import FireRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | Free form address text
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry default is N (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Risk By Address
        api_response = api_instance.get_fire_risk_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Risk By Address
        api_response = api_instance.get_fire_risk_by_address(address, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Free form address text |
 **include_geometry** | **str**| Flag to return Geometry default is N | [optional]

### Return type

[**FireRiskResponse**](FireRiskResponse.md)

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

# **get_fire_risk_by_address_batch**
> FireRiskResponseList get_fire_risk_by_address_batch(fire_risk_by_address_request)

Post Fire Risk By Address

This is a Batch offering for 'Fire Risk By Address' service. It accepts a single address or a list of addresses and retrieve fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_by_address_request import FireRiskByAddressRequest
from com.precisely.apis.model.fire_risk_response_list import FireRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    fire_risk_by_address_request = FireRiskByAddressRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FireRiskByAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Fire Risk By Address
        api_response = api_instance.get_fire_risk_by_address_batch(fire_risk_by_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_risk_by_address_request** | [**FireRiskByAddressRequest**](FireRiskByAddressRequest.md)|  |

### Return type

[**FireRiskResponseList**](FireRiskResponseList.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fire_risk_by_location**
> FireRiskResponse get_fire_risk_by_location(longitude, latitude)

Get Fire Risk By Location

Accepts latitude & longitude as input and Returns fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_response import FireRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of Location
    latitude = "latitude_example" # str | Latitude of Location
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry default is N (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Risk By Location
        api_response = api_instance.get_fire_risk_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Risk By Location
        api_response = api_instance.get_fire_risk_by_location(longitude, latitude, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of Location |
 **latitude** | **str**| Latitude of Location |
 **include_geometry** | **str**| Flag to return Geometry default is N | [optional]

### Return type

[**FireRiskResponse**](FireRiskResponse.md)

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

# **get_fire_risk_by_location_batch**
> FireRiskResponseList get_fire_risk_by_location_batch(fire_risk_by_location_request)

Post Fire Risk By Location

This is a Batch offering for 'Fire Risk By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_by_location_request import FireRiskByLocationRequest
from com.precisely.apis.model.fire_risk_response_list import FireRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    fire_risk_by_location_request = FireRiskByLocationRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FireRiskByLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Fire Risk By Location
        api_response = api_instance.get_fire_risk_by_location_batch(fire_risk_by_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_risk_by_location_request** | [**FireRiskByLocationRequest**](FireRiskByLocationRequest.md)|  |

### Return type

[**FireRiskResponseList**](FireRiskResponseList.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fire_risk_v2_by_address**
> FireRiskV2Response get_fire_risk_v2_by_address(address)

Get Fire Risk By Address

Accepts addresses as input and Returns fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_v2_response import FireRiskV2Response
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | Free form address text
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry default is N (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Risk By Address
        api_response = api_instance.get_fire_risk_v2_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Risk By Address
        api_response = api_instance.get_fire_risk_v2_by_address(address, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Free form address text |
 **include_geometry** | **str**| Flag to return Geometry default is N | [optional]

### Return type

[**FireRiskV2Response**](FireRiskV2Response.md)

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

# **get_fire_risk_v2_by_address_batch**
> FireRiskV2ResponseList get_fire_risk_v2_by_address_batch(fire_risk_by_address_request)

Post Fire Risk By Address

This is a Batch offering for 'Fire Risk By Address' service. It accepts a single address or a list of addresses and retrieve fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_v2_response_list import FireRiskV2ResponseList
from com.precisely.apis.model.fire_risk_by_address_request import FireRiskByAddressRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    fire_risk_by_address_request = FireRiskByAddressRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FireRiskByAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Fire Risk By Address
        api_response = api_instance.get_fire_risk_v2_by_address_batch(fire_risk_by_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_risk_by_address_request** | [**FireRiskByAddressRequest**](FireRiskByAddressRequest.md)|  |

### Return type

[**FireRiskV2ResponseList**](FireRiskV2ResponseList.md)

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

# **get_fire_risk_v2_by_location**
> FireRiskV2Response get_fire_risk_v2_by_location(longitude, latitude)

Get Fire Risk By Location

Accepts latitude & longitude as input and Returns fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_v2_response import FireRiskV2Response
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of Location
    latitude = "latitude_example" # str | Latitude of Location
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry default is N (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Risk By Location
        api_response = api_instance.get_fire_risk_v2_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Risk By Location
        api_response = api_instance.get_fire_risk_v2_by_location(longitude, latitude, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of Location |
 **latitude** | **str**| Latitude of Location |
 **include_geometry** | **str**| Flag to return Geometry default is N | [optional]

### Return type

[**FireRiskV2Response**](FireRiskV2Response.md)

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

# **get_fire_risk_v2_by_location_batch**
> FireRiskV2ResponseList get_fire_risk_v2_by_location_batch(fire_risk_by_location_request)

Post Fire Risk By Location

This is a Batch offering for 'Fire Risk By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve fire risk data by risk types.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.fire_risk_v2_response_list import FireRiskV2ResponseList
from com.precisely.apis.model.fire_risk_by_location_request import FireRiskByLocationRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    fire_risk_by_location_request = FireRiskByLocationRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=RiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FireRiskByLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Fire Risk By Location
        api_response = api_instance.get_fire_risk_v2_by_location_batch(fire_risk_by_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_risk_v2_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fire_risk_by_location_request** | [**FireRiskByLocationRequest**](FireRiskByLocationRequest.md)|  |

### Return type

[**FireRiskV2ResponseList**](FireRiskV2ResponseList.md)

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

# **get_fire_station_by_address**
> FireStations get_fire_station_by_address(address)

Get Fire Station By Address

Accepts addresses as input and Returns nearest fire stations.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.fire_stations import FireStations
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | Free Address
    max_candidates = "maxCandidates_example" # str | Specifies the maximum number of fire stations that this service retrieves. The default value is 3 and maximum value is 5. The retrieved results are traveldistance sorted from the input location. (optional)
    travel_time = "travelTime_example" # str | Max travel time from input location to fire station. Maximum allowed is 2 hours (optional)
    travel_time_unit = "travelTimeUnit_example" # str | minutes (default), hours, seconds, milliseconds (optional)
    travel_distance = "travelDistance_example" # str | Max travel distance from input location to fire station. Maximum allowed is 50 miles (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Feet (default), Kilometers, Miles, Meters (optional)
    sort_by = "sortBy_example" # str | time (default), distance (optional)
    historic_traffic_time_bucket = "historicTrafficTimeBucket_example" # str | Historic traffic time slab (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Station By Address
        api_response = api_instance.get_fire_station_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_station_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Station By Address
        api_response = api_instance.get_fire_station_by_address(address, max_candidates=max_candidates, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, sort_by=sort_by, historic_traffic_time_bucket=historic_traffic_time_bucket)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_station_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Free Address |
 **max_candidates** | **str**| Specifies the maximum number of fire stations that this service retrieves. The default value is 3 and maximum value is 5. The retrieved results are traveldistance sorted from the input location. | [optional]
 **travel_time** | **str**| Max travel time from input location to fire station. Maximum allowed is 2 hours | [optional]
 **travel_time_unit** | **str**| minutes (default), hours, seconds, milliseconds | [optional]
 **travel_distance** | **str**| Max travel distance from input location to fire station. Maximum allowed is 50 miles | [optional]
 **travel_distance_unit** | **str**| Feet (default), Kilometers, Miles, Meters | [optional]
 **sort_by** | **str**| time (default), distance | [optional]
 **historic_traffic_time_bucket** | **str**| Historic traffic time slab | [optional]

### Return type

[**FireStations**](FireStations.md)

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

# **get_fire_station_by_location**
> FireStations get_fire_station_by_location(longitude, latitude)

Get Fire Station By Location

Accepts latitude & longitude as input and Returns nearest fire stations.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.fire_stations import FireStations
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of Location
    latitude = "latitude_example" # str | Latitude of Location
    max_candidates = "maxCandidates_example" # str | Specifies the maximum number of fire stations that this service retrieves. The default value is 3 and maximum value is 5. The retrieved results are traveldistance sorted from the input location. (optional)
    travel_time = "travelTime_example" # str | Max travel time from input location to fire station. Maximum allowed is 2 hours (optional)
    travel_time_unit = "travelTimeUnit_example" # str | minutes (default), hours, seconds, milliseconds (optional)
    travel_distance = "travelDistance_example" # str | Max travel distance from input location to fire station. Maximum allowed is 50 miles (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Feet (default), Kilometers, Miles, Meters (optional)
    sort_by = "sortBy_example" # str | time (default), distance (optional)
    historic_traffic_time_bucket = "historicTrafficTimeBucket_example" # str | Historic traffic time slab (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fire Station By Location
        api_response = api_instance.get_fire_station_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_station_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fire Station By Location
        api_response = api_instance.get_fire_station_by_location(longitude, latitude, max_candidates=max_candidates, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, sort_by=sort_by, historic_traffic_time_bucket=historic_traffic_time_bucket)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_fire_station_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of Location |
 **latitude** | **str**| Latitude of Location |
 **max_candidates** | **str**| Specifies the maximum number of fire stations that this service retrieves. The default value is 3 and maximum value is 5. The retrieved results are traveldistance sorted from the input location. | [optional]
 **travel_time** | **str**| Max travel time from input location to fire station. Maximum allowed is 2 hours | [optional]
 **travel_time_unit** | **str**| minutes (default), hours, seconds, milliseconds | [optional]
 **travel_distance** | **str**| Max travel distance from input location to fire station. Maximum allowed is 50 miles | [optional]
 **travel_distance_unit** | **str**| Feet (default), Kilometers, Miles, Meters | [optional]
 **sort_by** | **str**| time (default), distance | [optional]
 **historic_traffic_time_bucket** | **str**| Historic traffic time slab | [optional]

### Return type

[**FireStations**](FireStations.md)

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

# **get_flood_risk_by_address**
> FloodRiskResponse get_flood_risk_by_address(address)

Get Flood Risk By Address

Accepts addresses as input and Returns flood risk data for flood zones and base flood elevation values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.flood_risk_response import FloodRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    address = "address_example" # str | Free text Address
    include_zone_desc = "includeZoneDesc_example" # str | Flag to return zone description (optional)
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Flood Risk By Address
        api_response = api_instance.get_flood_risk_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Flood Risk By Address
        api_response = api_instance.get_flood_risk_by_address(address, include_zone_desc=include_zone_desc, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Free text Address |
 **include_zone_desc** | **str**| Flag to return zone description | [optional]
 **include_geometry** | **str**| Flag to return Geometry | [optional]

### Return type

[**FloodRiskResponse**](FloodRiskResponse.md)

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

# **get_flood_risk_by_address_batch**
> FloodRiskResponseList get_flood_risk_by_address_batch(flood_risk_by_address_request)

Post Flood Risk By Address

This is a Batch offering for 'Flood Risk By Address' service. It accepts a single address or a list of addresses and retrieve flood risk data for flood zones and base flood elevation values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.flood_risk_response_list import FloodRiskResponseList
from com.precisely.apis.model.flood_risk_by_address_request import FloodRiskByAddressRequest
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    flood_risk_by_address_request = FloodRiskByAddressRequest(
        addresses=[
            RiskAddress(
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
        ],
        preferences=FloodRiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FloodRiskByAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Flood Risk By Address
        api_response = api_instance.get_flood_risk_by_address_batch(flood_risk_by_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flood_risk_by_address_request** | [**FloodRiskByAddressRequest**](FloodRiskByAddressRequest.md)|  |

### Return type

[**FloodRiskResponseList**](FloodRiskResponseList.md)

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

# **get_flood_risk_by_location**
> FloodRiskResponse get_flood_risk_by_location(longitude, latitude)

Get Flood Risk By Location

Accepts latitude & longitude as input and Returns flood risk data for flood zones and base flood elevation values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.flood_risk_response import FloodRiskResponse
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of Location
    latitude = "latitude_example" # str | Latitude of Location
    include_zone_desc = "includeZoneDesc_example" # str | Flag to return zone description (optional)
    include_geometry = "includeGeometry_example" # str | Flag to return Geometry (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Flood Risk By Location
        api_response = api_instance.get_flood_risk_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Flood Risk By Location
        api_response = api_instance.get_flood_risk_by_location(longitude, latitude, include_zone_desc=include_zone_desc, include_geometry=include_geometry)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of Location |
 **latitude** | **str**| Latitude of Location |
 **include_zone_desc** | **str**| Flag to return zone description | [optional]
 **include_geometry** | **str**| Flag to return Geometry | [optional]

### Return type

[**FloodRiskResponse**](FloodRiskResponse.md)

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

# **get_flood_risk_by_location_batch**
> FloodRiskResponseList get_flood_risk_by_location_batch(flood_risk_by_location_request)

Post Flood Risk By Location

This is a Batch offering for 'Flood Risk By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve flood risk data for flood zones and base flood elevation values.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import risks_service_api
from com.precisely.apis.model.flood_risk_by_location_request import FloodRiskByLocationRequest
from com.precisely.apis.model.flood_risk_response_list import FloodRiskResponseList
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
    api_instance = risks_service_api.RisksServiceApi(api_client)
    flood_risk_by_location_request = FloodRiskByLocationRequest(
        locations=[
            RiskLocations(
                geometry=RiskGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=FloodRiskPreferences(
            include_geometry="include_geometry_example",
            include_zone_desc="include_zone_desc_example",
            richter_value="richter_value_example",
        ),
    ) # FloodRiskByLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Flood Risk By Location
        api_response = api_instance.get_flood_risk_by_location_batch(flood_risk_by_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RisksServiceApi->get_flood_risk_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flood_risk_by_location_request** | [**FloodRiskByLocationRequest**](FloodRiskByLocationRequest.md)|  |

### Return type

[**FloodRiskResponseList**](FloodRiskResponseList.md)

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

