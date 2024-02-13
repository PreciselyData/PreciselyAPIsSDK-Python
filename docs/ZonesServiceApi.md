# com.precisely.apis.ZonesServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_basic_boundary_by_address**](ZonesServiceApi.md#get_basic_boundary_by_address) | **GET** /zones/v1/basicboundary/byaddress | Gets Basic Boundary by Address.
[**get_basic_boundary_by_location**](ZonesServiceApi.md#get_basic_boundary_by_location) | **GET** /zones/v1/basicboundary/bylocation | Gets Basic Boundary by Location.
[**get_poi_boundary_by_address**](ZonesServiceApi.md#get_poi_boundary_by_address) | **GET** /zones/v1/poiboundary/byaddress | Gets Point of Interests Boundary by Address.
[**get_poi_boundary_by_address_batch**](ZonesServiceApi.md#get_poi_boundary_by_address_batch) | **POST** /zones/v1/poiboundary/byaddress | Batch method for getting Point of Interests Boundary by Address.
[**get_poi_boundary_by_location**](ZonesServiceApi.md#get_poi_boundary_by_location) | **GET** /zones/v1/poiboundary/bylocation | Get Point of Interests Boundary by Location.
[**get_poi_boundary_by_location_batch**](ZonesServiceApi.md#get_poi_boundary_by_location_batch) | **POST** /zones/v1/poiboundary/bylocation | Batch method for getting Point of Interests Boundary by Location.
[**get_travel_boundary_by_distance**](ZonesServiceApi.md#get_travel_boundary_by_distance) | **GET** /zones/v1/travelboundary/bydistance | Get TravelBoundary By Distance.
[**get_travel_boundary_by_time**](ZonesServiceApi.md#get_travel_boundary_by_time) | **GET** /zones/v1/travelboundary/bytime | Get TravelBoundary By Time.


# **get_basic_boundary_by_address**
> BasicBoundary get_basic_boundary_by_address(address)

Gets Basic Boundary by Address.

Gets Basic Boundary by Address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.basic_boundary import BasicBoundary
from com.precisely.apis.model.error_info1 import ErrorInfo1
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    address = "address_example" # str | Address around which Basic Boundary is requested
    country = "country_example" # str | Three digit ISO country code (optional)
    distance = "distance_example" # str |  (optional)
    distance_unit = "distanceUnit_example" # str |  (optional)
    resolution = "resolution_example" # str | This is resolution of the buffer. Curves generated in buffer are approximated by line segments and it is measured in segments per circle. The higher the resolution, the smoother the curves of the buffer but more points would be required in the boundary geometry. Number greater than 0 and in multiple of 4. If not in 4, then it is approximated to nearest multiple of 4. (optional)
    response_srs = "responseSrs_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Basic Boundary by Address.
        api_response = api_instance.get_basic_boundary_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_basic_boundary_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Basic Boundary by Address.
        api_response = api_instance.get_basic_boundary_by_address(address, country=country, distance=distance, distance_unit=distance_unit, resolution=resolution, response_srs=response_srs)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_basic_boundary_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address around which Basic Boundary is requested |
 **country** | **str**| Three digit ISO country code | [optional]
 **distance** | **str**|  | [optional]
 **distance_unit** | **str**|  | [optional]
 **resolution** | **str**| This is resolution of the buffer. Curves generated in buffer are approximated by line segments and it is measured in segments per circle. The higher the resolution, the smoother the curves of the buffer but more points would be required in the boundary geometry. Number greater than 0 and in multiple of 4. If not in 4, then it is approximated to nearest multiple of 4. | [optional]
 **response_srs** | **str**|  | [optional]

### Return type

[**BasicBoundary**](BasicBoundary.md)

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

# **get_basic_boundary_by_location**
> BasicBoundary get_basic_boundary_by_location(latitude, longitude, distance)

Gets Basic Boundary by Location.

Gets Basic Boundary by Location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.basic_boundary import BasicBoundary
from com.precisely.apis.model.error_info1 import ErrorInfo1
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    latitude = "latitude_example" # str | Latitude around which Basic Boundary is requested
    longitude = "longitude_example" # str | Longitude around which Basic Boundary is requested
    distance = "distance_example" # str | This is width of the buffer (in a complete circular buffer, it would be radius of the buffer). This has to be a positive number.
    distance_unit = "distanceUnit_example" # str |  (optional)
    resolution = "resolution_example" # str | This is resolution of the buffer. Curves generated in buffer are approximated by line segments and it is measured in segments per circle. The higher the resolution, the smoother the curves of the buffer but more points would be required in the boundary geometry. Number greater than 0 and in multiple of 4. If not in 4, then it is approximated to nearest multiple of 4. (optional)
    response_srs = "responseSrs_example" # str |  (optional)
    srs_name = "srsName_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Basic Boundary by Location.
        api_response = api_instance.get_basic_boundary_by_location(latitude, longitude, distance)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_basic_boundary_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Basic Boundary by Location.
        api_response = api_instance.get_basic_boundary_by_location(latitude, longitude, distance, distance_unit=distance_unit, resolution=resolution, response_srs=response_srs, srs_name=srs_name)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_basic_boundary_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **str**| Latitude around which Basic Boundary is requested |
 **longitude** | **str**| Longitude around which Basic Boundary is requested |
 **distance** | **str**| This is width of the buffer (in a complete circular buffer, it would be radius of the buffer). This has to be a positive number. |
 **distance_unit** | **str**|  | [optional]
 **resolution** | **str**| This is resolution of the buffer. Curves generated in buffer are approximated by line segments and it is measured in segments per circle. The higher the resolution, the smoother the curves of the buffer but more points would be required in the boundary geometry. Number greater than 0 and in multiple of 4. If not in 4, then it is approximated to nearest multiple of 4. | [optional]
 **response_srs** | **str**|  | [optional]
 **srs_name** | **str**|  | [optional]

### Return type

[**BasicBoundary**](BasicBoundary.md)

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

# **get_poi_boundary_by_address**
> PoiBoundary get_poi_boundary_by_address(address)

Gets Point of Interests Boundary by Address.

Gets Point of Interests Boundary by Address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.poi_boundary import PoiBoundary
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    address = "address_example" # str | Address around which POI Boundary is requested
    category_code = "categoryCode_example" # str | Specific Category/Categories Codes for the desired POIs. Accepts a mix of 4 digit (Top Category), 6 digit (Second-Level Category) and 11 digit (Low-Level Category) Category Codes. (optional)
    sic_code = "sicCode_example" # str | Specify starting digits or full sic code to filter the response (optional)
    naics_code = "naicsCode_example" # str | Will accept naicsCode to filter POIs in results. Max 10 allowed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets Point of Interests Boundary by Address.
        api_response = api_instance.get_poi_boundary_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Point of Interests Boundary by Address.
        api_response = api_instance.get_poi_boundary_by_address(address, category_code=category_code, sic_code=sic_code, naics_code=naics_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address around which POI Boundary is requested |
 **category_code** | **str**| Specific Category/Categories Codes for the desired POIs. Accepts a mix of 4 digit (Top Category), 6 digit (Second-Level Category) and 11 digit (Low-Level Category) Category Codes. | [optional]
 **sic_code** | **str**| Specify starting digits or full sic code to filter the response | [optional]
 **naics_code** | **str**| Will accept naicsCode to filter POIs in results. Max 10 allowed. | [optional]

### Return type

[**PoiBoundary**](PoiBoundary.md)

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

# **get_poi_boundary_by_address_batch**
> POIBoundaryResponse get_poi_boundary_by_address_batch(poi_boundary_address_request)

Batch method for getting Point of Interests Boundary by Address.

Batch method for getting Point of Interests Boundary by Address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.poi_boundary_address_request import POIBoundaryAddressRequest
from com.precisely.apis.model.poi_boundary_response import POIBoundaryResponse
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    poi_boundary_address_request = POIBoundaryAddressRequest(
        addresses=[
            ZonesAddress(
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
        preferences=POIBoundaryPreferences(
            category_code="category_code_example",
            sic_code="sic_code_example",
            naics_code="naics_code_example",
        ),
    ) # POIBoundaryAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch method for getting Point of Interests Boundary by Address.
        api_response = api_instance.get_poi_boundary_by_address_batch(poi_boundary_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poi_boundary_address_request** | [**POIBoundaryAddressRequest**](POIBoundaryAddressRequest.md)|  |

### Return type

[**POIBoundaryResponse**](POIBoundaryResponse.md)

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

# **get_poi_boundary_by_location**
> PoiBoundary get_poi_boundary_by_location(latitude, longitude)

Get Point of Interests Boundary by Location.

Get Point of Interests Boundary by Location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.poi_boundary import PoiBoundary
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    latitude = "latitude_example" # str | Latitude around which POI Boundary is requested
    longitude = "longitude_example" # str | Longitude around which POI Boundary is requested
    category_code = "categoryCode_example" # str | Specific Category/Categories Codes for the desired POIs. Accepts a mix of 4 digit (Top Category), 6 digit (Second-Level Category) and 11 digit (Low-Level Category) Category Codes (optional)
    sic_code = "sicCode_example" # str | Specify starting digits or full sic code to filter the response (optional)
    naics_code = "naicsCode_example" # str | Will accept naicsCode to filter POIs in results. Max 10 allowed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Point of Interests Boundary by Location.
        api_response = api_instance.get_poi_boundary_by_location(latitude, longitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Point of Interests Boundary by Location.
        api_response = api_instance.get_poi_boundary_by_location(latitude, longitude, category_code=category_code, sic_code=sic_code, naics_code=naics_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latitude** | **str**| Latitude around which POI Boundary is requested |
 **longitude** | **str**| Longitude around which POI Boundary is requested |
 **category_code** | **str**| Specific Category/Categories Codes for the desired POIs. Accepts a mix of 4 digit (Top Category), 6 digit (Second-Level Category) and 11 digit (Low-Level Category) Category Codes | [optional]
 **sic_code** | **str**| Specify starting digits or full sic code to filter the response | [optional]
 **naics_code** | **str**| Will accept naicsCode to filter POIs in results. Max 10 allowed. | [optional]

### Return type

[**PoiBoundary**](PoiBoundary.md)

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

# **get_poi_boundary_by_location_batch**
> POIBoundaryResponse get_poi_boundary_by_location_batch(poi_boundary_location_request)

Batch method for getting Point of Interests Boundary by Location.

Batch method for getting Point of Interests Boundary by Location.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.poi_boundary_response import POIBoundaryResponse
from com.precisely.apis.model.poi_boundary_location_request import POIBoundaryLocationRequest
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    poi_boundary_location_request = POIBoundaryLocationRequest(
        locations=[
            POIBoundaryLocations(
                geometry=ZonesGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
        preferences=POIBoundaryPreferences(
            category_code="category_code_example",
            sic_code="sic_code_example",
            naics_code="naics_code_example",
        ),
    ) # POIBoundaryLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch method for getting Point of Interests Boundary by Location.
        api_response = api_instance.get_poi_boundary_by_location_batch(poi_boundary_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_poi_boundary_by_location_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poi_boundary_location_request** | [**POIBoundaryLocationRequest**](POIBoundaryLocationRequest.md)|  |

### Return type

[**POIBoundaryResponse**](POIBoundaryResponse.md)

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

# **get_travel_boundary_by_distance**
> TravelBoundaries get_travel_boundary_by_distance()

Get TravelBoundary By Distance.

Returns the travel boundary based on travel distance.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.travel_boundaries import TravelBoundaries
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    point = "point_example" # str | Starting point from where the travel boundary is calculated. Point in Lat,Long,coordsys format (optional)
    address = "address_example" # str | Address around which Basic Boundary is requested. (optional)
    costs = "costs_example" # str | Travel time used to calculate the travel boundary. (optional)
    cost_unit = "costUnit_example" # str | Travel time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). (optional)
    db = "db_example" # str | Mode of commute. (optional)
    country = "country_example" # str | 3 character ISO code or country name. (optional)
    max_offroad_distance = "maxOffroadDistance_example" # str | Maximum distance to allow travel off the road network. (optional)
    max_offroad_distance_unit = "maxOffroadDistanceUnit_example" # str | MaxOffroad Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional)
    destination_srs = "destinationSrs_example" # str | Desired coordinate system of the travel boundary. (optional)
    major_roads = "true" # str | Whether to include all roads in the calculation or just major roads. (optional) if omitted the server will use the default value of "true"
    return_holes = "returnHoles_example" # str | Whether to return holes, which are areas within the larger boundary that cannot be reached within the desired time (optional)
    return_islands = "returnIslands_example" # str | Whether to return islands, which are small areas outside the main boundary that can be reached within the desired time (optional)
    simplification_factor = "simplificationFactor_example" # str | Number between 0.0 and 1.0 where 0.0 is very simple and 1.0 means the most complex (optional)
    banding_style = "bandingStyle_example" # str | Style of banding to be used in the result (optional)
    historic_traffic_time_bucket = "historicTrafficTimeBucket_example" # str | Whether routing calculation uses the historic traffic speeds (optional)
    default_ambient_speed = "defaultAmbientSpeed_example" # str | The speed to travel when going off a network road to find the travel boundary (for all road types). (optional)
    ambient_speed_unit = "ambientSpeedUnit_example" # str | The unit of measure to use to calculate the ambient speed. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TravelBoundary By Distance.
        api_response = api_instance.get_travel_boundary_by_distance(point=point, address=address, costs=costs, cost_unit=cost_unit, db=db, country=country, max_offroad_distance=max_offroad_distance, max_offroad_distance_unit=max_offroad_distance_unit, destination_srs=destination_srs, major_roads=major_roads, return_holes=return_holes, return_islands=return_islands, simplification_factor=simplification_factor, banding_style=banding_style, historic_traffic_time_bucket=historic_traffic_time_bucket, default_ambient_speed=default_ambient_speed, ambient_speed_unit=ambient_speed_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_travel_boundary_by_distance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**| Starting point from where the travel boundary is calculated. Point in Lat,Long,coordsys format | [optional]
 **address** | **str**| Address around which Basic Boundary is requested. | [optional]
 **costs** | **str**| Travel time used to calculate the travel boundary. | [optional]
 **cost_unit** | **str**| Travel time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). | [optional]
 **db** | **str**| Mode of commute. | [optional]
 **country** | **str**| 3 character ISO code or country name. | [optional]
 **max_offroad_distance** | **str**| Maximum distance to allow travel off the road network. | [optional]
 **max_offroad_distance_unit** | **str**| MaxOffroad Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional]
 **destination_srs** | **str**| Desired coordinate system of the travel boundary. | [optional]
 **major_roads** | **str**| Whether to include all roads in the calculation or just major roads. | [optional] if omitted the server will use the default value of "true"
 **return_holes** | **str**| Whether to return holes, which are areas within the larger boundary that cannot be reached within the desired time | [optional]
 **return_islands** | **str**| Whether to return islands, which are small areas outside the main boundary that can be reached within the desired time | [optional]
 **simplification_factor** | **str**| Number between 0.0 and 1.0 where 0.0 is very simple and 1.0 means the most complex | [optional]
 **banding_style** | **str**| Style of banding to be used in the result | [optional]
 **historic_traffic_time_bucket** | **str**| Whether routing calculation uses the historic traffic speeds | [optional]
 **default_ambient_speed** | **str**| The speed to travel when going off a network road to find the travel boundary (for all road types). | [optional]
 **ambient_speed_unit** | **str**| The unit of measure to use to calculate the ambient speed. | [optional]

### Return type

[**TravelBoundaries**](TravelBoundaries.md)

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

# **get_travel_boundary_by_time**
> TravelBoundaries get_travel_boundary_by_time()

Get TravelBoundary By Time.

Travel boundary based on travel time.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import zones_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.travel_boundaries import TravelBoundaries
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
    api_instance = zones_service_api.ZonesServiceApi(api_client)
    point = "point_example" # str | Starting point from where the travel boundary is calculated. Point in Lat,Long,coordsys format (optional)
    address = "address_example" # str | Starting address from where the travel boundary is calculated. (optional)
    costs = "costs_example" # str | Travel time used to calculate the travel boundary. (optional)
    cost_unit = "costUnit_example" # str | Travel time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). (optional)
    db = "db_example" # str | Mode of commute. (optional)
    country = "country_example" # str | 3 character ISO code or country name. (optional)
    max_offroad_distance = "maxOffroadDistance_example" # str | Maximum distance to allow travel off the road network. (optional)
    max_offroad_distance_unit = "maxOffroadDistanceUnit_example" # str | MaxOffroad Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional)
    destination_srs = "destinationSrs_example" # str | Desired coordinate system of the travel boundary. (optional)
    major_roads = "true" # str | Whether to include all roads in the calculation or just major roads. (optional) if omitted the server will use the default value of "true"
    return_holes = "returnHoles_example" # str | Whether to return holes, which are areas within the larger boundary that cannot be reached within the desired time (optional)
    return_islands = "returnIslands_example" # str | Whether to return islands, which are small areas outside the main boundary that can be reached within the desired time (optional)
    simplification_factor = "simplificationFactor_example" # str | Number between 0.0 and 1.0 where 0.0 is very simple and 1.0 means the most complex (optional)
    banding_style = "bandingStyle_example" # str | Style of banding to be used in the result (optional)
    historic_traffic_time_bucket = "historicTrafficTimeBucket_example" # str | Whether routing calculation uses the historic traffic speeds (optional)
    default_ambient_speed = "defaultAmbientSpeed_example" # str | The speed to travel when going off a network road to find the travel boundary (for all road types). (optional)
    ambient_speed_unit = "ambientSpeedUnit_example" # str | The unit of measure to use to calculate the ambient speed. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TravelBoundary By Time.
        api_response = api_instance.get_travel_boundary_by_time(point=point, address=address, costs=costs, cost_unit=cost_unit, db=db, country=country, max_offroad_distance=max_offroad_distance, max_offroad_distance_unit=max_offroad_distance_unit, destination_srs=destination_srs, major_roads=major_roads, return_holes=return_holes, return_islands=return_islands, simplification_factor=simplification_factor, banding_style=banding_style, historic_traffic_time_bucket=historic_traffic_time_bucket, default_ambient_speed=default_ambient_speed, ambient_speed_unit=ambient_speed_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling ZonesServiceApi->get_travel_boundary_by_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**| Starting point from where the travel boundary is calculated. Point in Lat,Long,coordsys format | [optional]
 **address** | **str**| Starting address from where the travel boundary is calculated. | [optional]
 **costs** | **str**| Travel time used to calculate the travel boundary. | [optional]
 **cost_unit** | **str**| Travel time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). | [optional]
 **db** | **str**| Mode of commute. | [optional]
 **country** | **str**| 3 character ISO code or country name. | [optional]
 **max_offroad_distance** | **str**| Maximum distance to allow travel off the road network. | [optional]
 **max_offroad_distance_unit** | **str**| MaxOffroad Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional]
 **destination_srs** | **str**| Desired coordinate system of the travel boundary. | [optional]
 **major_roads** | **str**| Whether to include all roads in the calculation or just major roads. | [optional] if omitted the server will use the default value of "true"
 **return_holes** | **str**| Whether to return holes, which are areas within the larger boundary that cannot be reached within the desired time | [optional]
 **return_islands** | **str**| Whether to return islands, which are small areas outside the main boundary that can be reached within the desired time | [optional]
 **simplification_factor** | **str**| Number between 0.0 and 1.0 where 0.0 is very simple and 1.0 means the most complex | [optional]
 **banding_style** | **str**| Style of banding to be used in the result | [optional]
 **historic_traffic_time_bucket** | **str**| Whether routing calculation uses the historic traffic speeds | [optional]
 **default_ambient_speed** | **str**| The speed to travel when going off a network road to find the travel boundary (for all road types). | [optional]
 **ambient_speed_unit** | **str**| The unit of measure to use to calculate the ambient speed. | [optional]

### Return type

[**TravelBoundaries**](TravelBoundaries.md)

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

