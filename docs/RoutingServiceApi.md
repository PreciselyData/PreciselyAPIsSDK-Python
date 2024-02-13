# com.precisely.apis.RoutingServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_route_by_address**](RoutingServiceApi.md#get_route_by_address) | **GET** /routing/v1/route/byaddress | Gets Route By Address.
[**get_route_by_location**](RoutingServiceApi.md#get_route_by_location) | **GET** /routing/v1/route/bylocation | Gets Route By Location.
[**get_travel_cost_matrix_by_address**](RoutingServiceApi.md#get_travel_cost_matrix_by_address) | **GET** /routing/v1/travelcostmatrix/byaddress | Get Cost Matrix By Address.
[**get_travel_cost_matrix_by_location**](RoutingServiceApi.md#get_travel_cost_matrix_by_location) | **GET** /routing/v1/travelcostmatrix/bylocation | Get Cost Matrix By Location.


# **get_route_by_address**
> RouteResponse get_route_by_address()

Gets Route By Address.

Accepts addresses as input and Returns Point-to-Point and Multi-Point travel directions by various travel modes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import routing_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.route_response import RouteResponse
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
    api_instance = routing_service_api.RoutingServiceApi(api_client)
    start_address = "startAddress_example" # str | Starting address of the route. (optional)
    end_address = "endAddress_example" # str | Ending address of the route. (optional)
    db = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    country = "USA" # str | Three digit ISO country code. (optional) if omitted the server will use the default value of "USA"
    intermediate_addresses = "intermediateAddresses_example" # str | List of intermediate points of the route. (optional)
    return_intermediate_points = "false" # str | return intermediate points (optional) if omitted the server will use the default value of "false"
    oip = "false" # str | Specifies whether waypoints need to be optimized. (optional) if omitted the server will use the default value of "false"
    destination_srs = "destinationSrs_example" # str | Specifies the desired coordinate system of the returned route. (optional)
    optimize_by = "time" # str | Specifies whether the route should be optimized by time or distance. (optional) if omitted the server will use the default value of "time"
    return_distance = "true" # str | Specifies whether distance needs to be part of direction information in response. (optional) if omitted the server will use the default value of "true"
    distance_unit = "m" # str | Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional) if omitted the server will use the default value of "m"
    return_time = "true" # str | Specifies whether time needs to be part of direction information in response. (optional) if omitted the server will use the default value of "true"
    time_unit = "min" # str | Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond) (optional) if omitted the server will use the default value of "min"
    language = "language_example" # str | Specifies the language of travel directions. (optional)
    directions_style = "None" # str | Specifies whether route directions text is to be returned in the response and in what detail (Normal or Terse). (optional) if omitted the server will use the default value of "None"
    segment_geometry_style = "none" # str | Specifies whether the route geometry is to be returned in the response and in what detail (End or All). (optional) if omitted the server will use the default value of "none"
    primary_name_only = "false" # str | If true then only the primary street name is returned otherwise all the names for a street. (optional) if omitted the server will use the default value of "false"
    major_roads = "false" # str | Whether to include all roads in route calculation or just major roads. (optional) if omitted the server will use the default value of "false"
    historic_traffic_time_bucket = "None" # str | Specifies whether routing calculation uses the historic traffic speeds. (optional) if omitted the server will use the default value of "None"
    return_direction_geometry = "false" # str | Whether to include geometry associated with each route instruction in response. (optional) if omitted the server will use the default value of "false"
    use_cvr = "N" # str | This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. (optional) if omitted the server will use the default value of "N"
    loosening_barrier_restrictions = "Y" # str | Specifies that barriers will be removed when determining the route. (optional) if omitted the server will use the default value of "Y"
    vehicle_type = "ALL" # str | vehicle type. (optional) if omitted the server will use the default value of "ALL"
    weight = "" # str | Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    weight_unit = "kg" # str | The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). (optional) if omitted the server will use the default value of "kg"
    height = "" # str | Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    height_unit = "ft" # str | The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    length = "" # str | Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    length_unit = "ft" # str | The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    width = "" # str | Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    width_unit = "ft" # str | The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Route By Address.
        api_response = api_instance.get_route_by_address(start_address=start_address, end_address=end_address, db=db, country=country, intermediate_addresses=intermediate_addresses, return_intermediate_points=return_intermediate_points, oip=oip, destination_srs=destination_srs, optimize_by=optimize_by, return_distance=return_distance, distance_unit=distance_unit, return_time=return_time, time_unit=time_unit, language=language, directions_style=directions_style, segment_geometry_style=segment_geometry_style, primary_name_only=primary_name_only, major_roads=major_roads, historic_traffic_time_bucket=historic_traffic_time_bucket, return_direction_geometry=return_direction_geometry, use_cvr=use_cvr, loosening_barrier_restrictions=loosening_barrier_restrictions, vehicle_type=vehicle_type, weight=weight, weight_unit=weight_unit, height=height, height_unit=height_unit, length=length, length_unit=length_unit, width=width, width_unit=width_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RoutingServiceApi->get_route_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_address** | **str**| Starting address of the route. | [optional]
 **end_address** | **str**| Ending address of the route. | [optional]
 **db** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **country** | **str**| Three digit ISO country code. | [optional] if omitted the server will use the default value of "USA"
 **intermediate_addresses** | **str**| List of intermediate points of the route. | [optional]
 **return_intermediate_points** | **str**| return intermediate points | [optional] if omitted the server will use the default value of "false"
 **oip** | **str**| Specifies whether waypoints need to be optimized. | [optional] if omitted the server will use the default value of "false"
 **destination_srs** | **str**| Specifies the desired coordinate system of the returned route. | [optional]
 **optimize_by** | **str**| Specifies whether the route should be optimized by time or distance. | [optional] if omitted the server will use the default value of "time"
 **return_distance** | **str**| Specifies whether distance needs to be part of direction information in response. | [optional] if omitted the server will use the default value of "true"
 **distance_unit** | **str**| Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional] if omitted the server will use the default value of "m"
 **return_time** | **str**| Specifies whether time needs to be part of direction information in response. | [optional] if omitted the server will use the default value of "true"
 **time_unit** | **str**| Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond) | [optional] if omitted the server will use the default value of "min"
 **language** | **str**| Specifies the language of travel directions. | [optional]
 **directions_style** | **str**| Specifies whether route directions text is to be returned in the response and in what detail (Normal or Terse). | [optional] if omitted the server will use the default value of "None"
 **segment_geometry_style** | **str**| Specifies whether the route geometry is to be returned in the response and in what detail (End or All). | [optional] if omitted the server will use the default value of "none"
 **primary_name_only** | **str**| If true then only the primary street name is returned otherwise all the names for a street. | [optional] if omitted the server will use the default value of "false"
 **major_roads** | **str**| Whether to include all roads in route calculation or just major roads. | [optional] if omitted the server will use the default value of "false"
 **historic_traffic_time_bucket** | **str**| Specifies whether routing calculation uses the historic traffic speeds. | [optional] if omitted the server will use the default value of "None"
 **return_direction_geometry** | **str**| Whether to include geometry associated with each route instruction in response. | [optional] if omitted the server will use the default value of "false"
 **use_cvr** | **str**| This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. | [optional] if omitted the server will use the default value of "N"
 **loosening_barrier_restrictions** | **str**| Specifies that barriers will be removed when determining the route. | [optional] if omitted the server will use the default value of "Y"
 **vehicle_type** | **str**| vehicle type. | [optional] if omitted the server will use the default value of "ALL"
 **weight** | **str**| Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **weight_unit** | **str**| The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). | [optional] if omitted the server will use the default value of "kg"
 **height** | **str**| Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **height_unit** | **str**| The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **length** | **str**| Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **length_unit** | **str**| The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **width** | **str**| Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **width_unit** | **str**| The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"

### Return type

[**RouteResponse**](RouteResponse.md)

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

# **get_route_by_location**
> RouteResponse get_route_by_location()

Gets Route By Location.

Accepts latitude & longitude as input and Returns Point-to-Point and Multi-Point travel directions by various travel modes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import routing_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.route_response import RouteResponse
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
    api_instance = routing_service_api.RoutingServiceApi(api_client)
    start_point = "startPoint_example" # str | Start Point in 'Lat,Long,coordsys' format. (optional)
    end_point = "endPoint_example" # str | End Point in 'Lat,Long,coordsys' format. (optional)
    db = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    intermediate_points = "intermediatePoints_example" # str | List of intermediate points of the route. (optional)
    return_intermediate_points = "false" # str | returnIntermediatePoints route. (optional) if omitted the server will use the default value of "false"
    oip = "false" # str | Specifies whether waypoints need to be optimized. (optional) if omitted the server will use the default value of "false"
    destination_srs = "destinationSrs_example" # str | Specifies the desired coordinate system of the returned route. (optional)
    optimize_by = "time" # str | Specifies whether the route should be optimized by time or distance. (optional) if omitted the server will use the default value of "time"
    return_distance = "true" # str | Specifies whether distance needs to be part of direction information in response. (optional) if omitted the server will use the default value of "true"
    distance_unit = "m" # str | Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional) if omitted the server will use the default value of "m"
    return_time = "true" # str | Specifies whether time needs to be part of direction information in response. (optional) if omitted the server will use the default value of "true"
    time_unit = "min" # str | Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond) (optional) if omitted the server will use the default value of "min"
    language = "language_example" # str | Specifies the language of travel directions. (optional)
    directions_style = "None" # str | Specifies whether route directions text is to be returned in the response and in what detail (Normal or Terse). (optional) if omitted the server will use the default value of "None"
    segment_geometry_style = "none" # str | Specifies whether the route geometry is to be returned in the response and in what detail (End or All). (optional) if omitted the server will use the default value of "none"
    primary_name_only = "false" # str | If true then only the primary street name is returned otherwise all the names for a street. (optional) if omitted the server will use the default value of "false"
    major_roads = "false" # str | Whether to include all roads in route calculation or just major roads. (optional) if omitted the server will use the default value of "false"
    historic_traffic_time_bucket = "None" # str | Specifies whether routing calculation uses the historic traffic speeds. (optional) if omitted the server will use the default value of "None"
    return_direction_geometry = "false" # str | Whether to include geometry associated with each route instruction in response. (optional) if omitted the server will use the default value of "false"
    use_cvr = "N" # str | This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. (optional) if omitted the server will use the default value of "N"
    loosening_barrier_restrictions = "Y" # str | Specifies that barriers will be removed when determining the route. (optional) if omitted the server will use the default value of "Y"
    vehicle_type = "ALL" # str | vehicle type. (optional) if omitted the server will use the default value of "ALL"
    weight = "" # str | Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    weight_unit = "kg" # str | The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). (optional) if omitted the server will use the default value of "kg"
    height = "" # str | Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    height_unit = "ft" # str | The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    length = "" # str | Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    length_unit = "ft" # str | The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    width = "" # str | Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    width_unit = "ft" # str | The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Route By Location.
        api_response = api_instance.get_route_by_location(start_point=start_point, end_point=end_point, db=db, intermediate_points=intermediate_points, return_intermediate_points=return_intermediate_points, oip=oip, destination_srs=destination_srs, optimize_by=optimize_by, return_distance=return_distance, distance_unit=distance_unit, return_time=return_time, time_unit=time_unit, language=language, directions_style=directions_style, segment_geometry_style=segment_geometry_style, primary_name_only=primary_name_only, major_roads=major_roads, historic_traffic_time_bucket=historic_traffic_time_bucket, return_direction_geometry=return_direction_geometry, use_cvr=use_cvr, loosening_barrier_restrictions=loosening_barrier_restrictions, vehicle_type=vehicle_type, weight=weight, weight_unit=weight_unit, height=height, height_unit=height_unit, length=length, length_unit=length_unit, width=width, width_unit=width_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RoutingServiceApi->get_route_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_point** | **str**| Start Point in &#39;Lat,Long,coordsys&#39; format. | [optional]
 **end_point** | **str**| End Point in &#39;Lat,Long,coordsys&#39; format. | [optional]
 **db** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **intermediate_points** | **str**| List of intermediate points of the route. | [optional]
 **return_intermediate_points** | **str**| returnIntermediatePoints route. | [optional] if omitted the server will use the default value of "false"
 **oip** | **str**| Specifies whether waypoints need to be optimized. | [optional] if omitted the server will use the default value of "false"
 **destination_srs** | **str**| Specifies the desired coordinate system of the returned route. | [optional]
 **optimize_by** | **str**| Specifies whether the route should be optimized by time or distance. | [optional] if omitted the server will use the default value of "time"
 **return_distance** | **str**| Specifies whether distance needs to be part of direction information in response. | [optional] if omitted the server will use the default value of "true"
 **distance_unit** | **str**| Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional] if omitted the server will use the default value of "m"
 **return_time** | **str**| Specifies whether time needs to be part of direction information in response. | [optional] if omitted the server will use the default value of "true"
 **time_unit** | **str**| Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond) | [optional] if omitted the server will use the default value of "min"
 **language** | **str**| Specifies the language of travel directions. | [optional]
 **directions_style** | **str**| Specifies whether route directions text is to be returned in the response and in what detail (Normal or Terse). | [optional] if omitted the server will use the default value of "None"
 **segment_geometry_style** | **str**| Specifies whether the route geometry is to be returned in the response and in what detail (End or All). | [optional] if omitted the server will use the default value of "none"
 **primary_name_only** | **str**| If true then only the primary street name is returned otherwise all the names for a street. | [optional] if omitted the server will use the default value of "false"
 **major_roads** | **str**| Whether to include all roads in route calculation or just major roads. | [optional] if omitted the server will use the default value of "false"
 **historic_traffic_time_bucket** | **str**| Specifies whether routing calculation uses the historic traffic speeds. | [optional] if omitted the server will use the default value of "None"
 **return_direction_geometry** | **str**| Whether to include geometry associated with each route instruction in response. | [optional] if omitted the server will use the default value of "false"
 **use_cvr** | **str**| This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. | [optional] if omitted the server will use the default value of "N"
 **loosening_barrier_restrictions** | **str**| Specifies that barriers will be removed when determining the route. | [optional] if omitted the server will use the default value of "Y"
 **vehicle_type** | **str**| vehicle type. | [optional] if omitted the server will use the default value of "ALL"
 **weight** | **str**| Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **weight_unit** | **str**| The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). | [optional] if omitted the server will use the default value of "kg"
 **height** | **str**| Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **height_unit** | **str**| The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **length** | **str**| Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **length_unit** | **str**| The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **width** | **str**| Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **width_unit** | **str**| The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"

### Return type

[**RouteResponse**](RouteResponse.md)

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

# **get_travel_cost_matrix_by_address**
> TravelCostMatrixResponse get_travel_cost_matrix_by_address()

Get Cost Matrix By Address.

Accepts addresses as input and Returns travel distances and times for multiple origins to multiple destinations by various travel modes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import routing_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.travel_cost_matrix_response import TravelCostMatrixResponse
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
    api_instance = routing_service_api.RoutingServiceApi(api_client)
    start_addresses = "startAddresses_example" # str | Start locations in text based addresses. (optional)
    end_addresses = "endAddresses_example" # str | End locations in text based addresses. (optional)
    country = "USA" # str | 3 Digit ISO country code. (optional) if omitted the server will use the default value of "USA"
    db = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    optimize_by = "time" # str | Specifies whether routes should be optimized by time or distance. (optional) if omitted the server will use the default value of "time"
    return_distance = "true" # str | Specifies whether distance needs to be returned in response. (optional) if omitted the server will use the default value of "true"
    destination_srs = "destinationSrs_example" # str | Specifies the desired coordinate system of returned routes. (optional)
    distance_unit = "m" # str | Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional) if omitted the server will use the default value of "m"
    return_time = "true" # str | Specifies whether time needs to be returned in response. (optional) if omitted the server will use the default value of "true"
    time_unit = "min" # str | Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). (optional) if omitted the server will use the default value of "min"
    major_roads = "false" # str | Whether to include all roads in routes calculation or just major roads. (optional) if omitted the server will use the default value of "false"
    return_optimal_routes_only = "true" # str | Specifies whether to return only the optimized route for each start and end point combination. (optional) if omitted the server will use the default value of "true"
    historic_traffic_time_bucket = "None" # str | Specifies whether routing calculation uses the historic traffic speeds. (optional) if omitted the server will use the default value of "None"
    use_cvr = "N" # str | This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. (optional) if omitted the server will use the default value of "N"
    loosening_barrier_restrictions = "Y" # str | Specifies that barriers will be removed when determining the route. (optional) if omitted the server will use the default value of "Y"
    vehicle_type = "ALL" # str | vehicle type. (optional) if omitted the server will use the default value of "ALL"
    weight = "" # str | Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    weight_unit = "kg" # str | The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). (optional) if omitted the server will use the default value of "kg"
    height = "" # str | Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    height_unit = "ft" # str | The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    length = "" # str | Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    length_unit = "ft" # str | The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    width = "" # str | Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    width_unit = "ft" # str | The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Cost Matrix By Address.
        api_response = api_instance.get_travel_cost_matrix_by_address(start_addresses=start_addresses, end_addresses=end_addresses, country=country, db=db, optimize_by=optimize_by, return_distance=return_distance, destination_srs=destination_srs, distance_unit=distance_unit, return_time=return_time, time_unit=time_unit, major_roads=major_roads, return_optimal_routes_only=return_optimal_routes_only, historic_traffic_time_bucket=historic_traffic_time_bucket, use_cvr=use_cvr, loosening_barrier_restrictions=loosening_barrier_restrictions, vehicle_type=vehicle_type, weight=weight, weight_unit=weight_unit, height=height, height_unit=height_unit, length=length, length_unit=length_unit, width=width, width_unit=width_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RoutingServiceApi->get_travel_cost_matrix_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_addresses** | **str**| Start locations in text based addresses. | [optional]
 **end_addresses** | **str**| End locations in text based addresses. | [optional]
 **country** | **str**| 3 Digit ISO country code. | [optional] if omitted the server will use the default value of "USA"
 **db** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **optimize_by** | **str**| Specifies whether routes should be optimized by time or distance. | [optional] if omitted the server will use the default value of "time"
 **return_distance** | **str**| Specifies whether distance needs to be returned in response. | [optional] if omitted the server will use the default value of "true"
 **destination_srs** | **str**| Specifies the desired coordinate system of returned routes. | [optional]
 **distance_unit** | **str**| Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional] if omitted the server will use the default value of "m"
 **return_time** | **str**| Specifies whether time needs to be returned in response. | [optional] if omitted the server will use the default value of "true"
 **time_unit** | **str**| Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). | [optional] if omitted the server will use the default value of "min"
 **major_roads** | **str**| Whether to include all roads in routes calculation or just major roads. | [optional] if omitted the server will use the default value of "false"
 **return_optimal_routes_only** | **str**| Specifies whether to return only the optimized route for each start and end point combination. | [optional] if omitted the server will use the default value of "true"
 **historic_traffic_time_bucket** | **str**| Specifies whether routing calculation uses the historic traffic speeds. | [optional] if omitted the server will use the default value of "None"
 **use_cvr** | **str**| This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. | [optional] if omitted the server will use the default value of "N"
 **loosening_barrier_restrictions** | **str**| Specifies that barriers will be removed when determining the route. | [optional] if omitted the server will use the default value of "Y"
 **vehicle_type** | **str**| vehicle type. | [optional] if omitted the server will use the default value of "ALL"
 **weight** | **str**| Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **weight_unit** | **str**| The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). | [optional] if omitted the server will use the default value of "kg"
 **height** | **str**| Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **height_unit** | **str**| The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **length** | **str**| Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **length_unit** | **str**| The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **width** | **str**| Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **width_unit** | **str**| The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"

### Return type

[**TravelCostMatrixResponse**](TravelCostMatrixResponse.md)

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

# **get_travel_cost_matrix_by_location**
> TravelCostMatrixResponse get_travel_cost_matrix_by_location()

Get Cost Matrix By Location.

Accepts latitude & longitude as input and Returns travel distances and times for multiple origins to multiple destinations by various travel modes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import routing_service_api
from com.precisely.apis.model.error_info1 import ErrorInfo1
from com.precisely.apis.model.travel_cost_matrix_response import TravelCostMatrixResponse
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
    api_instance = routing_service_api.RoutingServiceApi(api_client)
    start_points = "startPoints_example" # str | The address to be searched. (optional)
    end_points = "endPoints_example" # str | The address to be searched. (optional)
    db = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    optimize_by = "time" # str | Specifies whether routes should be optimized by time or distance. (optional) if omitted the server will use the default value of "time"
    return_distance = "true" # str | Specifies whether distance needs to be returned in response. (optional) if omitted the server will use the default value of "true"
    destination_srs = "epsg:4326" # str | Specifies the desired coordinate system of returned routes. (optional) if omitted the server will use the default value of "epsg:4326"
    distance_unit = "m" # str | Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). (optional) if omitted the server will use the default value of "m"
    return_time = "true" # str | Specifies whether time needs to be returned in response. (optional) if omitted the server will use the default value of "true"
    time_unit = "min" # str | Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). (optional) if omitted the server will use the default value of "min"
    major_roads = "false" # str | Whether to include all roads in routes calculation or just major roads. (optional) if omitted the server will use the default value of "false"
    return_optimal_routes_only = "true" # str | Specifies whether to return only the optimized route for each start and end point combination. (optional) if omitted the server will use the default value of "true"
    historic_traffic_time_bucket = "None" # str | Specifies whether routing calculation uses the historic traffic speeds. (optional) if omitted the server will use the default value of "None"
    use_cvr = "N" # str | This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. (optional) if omitted the server will use the default value of "N"
    loosening_barrier_restrictions = "Y" # str | Specifies that barriers will be removed when determining the route. (optional) if omitted the server will use the default value of "Y"
    vehicle_type = "ALL" # str | vehicle type. (optional) if omitted the server will use the default value of "ALL"
    weight = "" # str | Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    weight_unit = "kg" # str | The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). (optional) if omitted the server will use the default value of "kg"
    height = "" # str | Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    height_unit = "ft" # str | The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    length = "" # str | Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    length_unit = "ft" # str | The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"
    width = "" # str | Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. (optional) if omitted the server will use the default value of ""
    width_unit = "ft" # str | The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). (optional) if omitted the server will use the default value of "ft"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Cost Matrix By Location.
        api_response = api_instance.get_travel_cost_matrix_by_location(start_points=start_points, end_points=end_points, db=db, optimize_by=optimize_by, return_distance=return_distance, destination_srs=destination_srs, distance_unit=distance_unit, return_time=return_time, time_unit=time_unit, major_roads=major_roads, return_optimal_routes_only=return_optimal_routes_only, historic_traffic_time_bucket=historic_traffic_time_bucket, use_cvr=use_cvr, loosening_barrier_restrictions=loosening_barrier_restrictions, vehicle_type=vehicle_type, weight=weight, weight_unit=weight_unit, height=height, height_unit=height_unit, length=length, length_unit=length_unit, width=width, width_unit=width_unit)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling RoutingServiceApi->get_travel_cost_matrix_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_points** | **str**| The address to be searched. | [optional]
 **end_points** | **str**| The address to be searched. | [optional]
 **db** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **optimize_by** | **str**| Specifies whether routes should be optimized by time or distance. | [optional] if omitted the server will use the default value of "time"
 **return_distance** | **str**| Specifies whether distance needs to be returned in response. | [optional] if omitted the server will use the default value of "true"
 **destination_srs** | **str**| Specifies the desired coordinate system of returned routes. | [optional] if omitted the server will use the default value of "epsg:4326"
 **distance_unit** | **str**| Return Distance Unit such as ft(Foot), km(Kilometer), mi(Mile), m(Meter) or yd(Yard). | [optional] if omitted the server will use the default value of "m"
 **return_time** | **str**| Specifies whether time needs to be returned in response. | [optional] if omitted the server will use the default value of "true"
 **time_unit** | **str**| Return time unit such as min(Minute), h(Hour), s(Second) or msec(Millisecond). | [optional] if omitted the server will use the default value of "min"
 **major_roads** | **str**| Whether to include all roads in routes calculation or just major roads. | [optional] if omitted the server will use the default value of "false"
 **return_optimal_routes_only** | **str**| Specifies whether to return only the optimized route for each start and end point combination. | [optional] if omitted the server will use the default value of "true"
 **historic_traffic_time_bucket** | **str**| Specifies whether routing calculation uses the historic traffic speeds. | [optional] if omitted the server will use the default value of "None"
 **use_cvr** | **str**| This parameter will enable/disable CVR (Commercial Vehicle Restrictions) capability in our APIs. | [optional] if omitted the server will use the default value of "N"
 **loosening_barrier_restrictions** | **str**| Specifies that barriers will be removed when determining the route. | [optional] if omitted the server will use the default value of "Y"
 **vehicle_type** | **str**| vehicle type. | [optional] if omitted the server will use the default value of "ALL"
 **weight** | **str**| Specifies the maximum weight of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **weight_unit** | **str**| The unit of weight eg. kg(kilogram), lb(pound), mt(metric ton), t(ton). | [optional] if omitted the server will use the default value of "kg"
 **height** | **str**| Specifies the maximum height of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **height_unit** | **str**| The unit of height e.g m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **length** | **str**| Specifies the maximum length of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **length_unit** | **str**| The unit of length eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"
 **width** | **str**| Specifies the maximum width of a vehicle. Any vehicles over this value will be restricted when determining the route. | [optional] if omitted the server will use the default value of ""
 **width_unit** | **str**| The unit of width eg. m(meter), km(kilometer), yd(yard), ft(foot), mi(mile). | [optional] if omitted the server will use the default value of "ft"

### Return type

[**TravelCostMatrixResponse**](TravelCostMatrixResponse.md)

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

