# com.precisely.apis.PlacesServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_category_code_metadata**](PlacesServiceApi.md#get_category_code_metadata) | **GET** /places/v1/metadata/category | Category Code Metadata.
[**get_poiby_id**](PlacesServiceApi.md#get_poiby_id) | **GET** /places/v1/poi/{id} | Points Of Interest Details By Id
[**get_pois_by_address**](PlacesServiceApi.md#get_pois_by_address) | **GET** /places/v1/poi/byaddress | Get POIs By Address.
[**get_pois_by_area**](PlacesServiceApi.md#get_pois_by_area) | **GET** /places/v1/poi/byarea | GET Points Of Interest By Area.
[**get_pois_by_geometry**](PlacesServiceApi.md#get_pois_by_geometry) | **POST** /places/v1/poi/byboundary | Points Of Interest By Boundary
[**get_pois_by_location**](PlacesServiceApi.md#get_pois_by_location) | **GET** /places/v1/poi/bylocation | Get POIs By Location.
[**get_pois_count**](PlacesServiceApi.md#get_pois_count) | **POST** /places/v1/poicount | Points Of Interest Count
[**get_sic_metadata**](PlacesServiceApi.md#get_sic_metadata) | **GET** /places/v1/metadata/sic | Get SIC Metadata
[**pois_autocomplete**](PlacesServiceApi.md#pois_autocomplete) | **GET** /places/v1/poi/autocomplete | Points Of Interest Autocomplete


# **get_category_code_metadata**
> MetadataResponse get_category_code_metadata()

Category Code Metadata.

This service returns a list of Category codes & associated metadata which can then be used as inputs for querying the Points of Interest By Address or Location methods listed above.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.metadata_response import MetadataResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    category_code = "categoryCode_example" # str | 4, 6, or 11 digits category code to filter the response. (optional)
    level = "level_example" # str | 1, 2, or 3. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Category Code Metadata.
        api_response = api_instance.get_category_code_metadata(category_code=category_code, level=level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_category_code_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_code** | **str**| 4, 6, or 11 digits category code to filter the response. | [optional]
 **level** | **str**| 1, 2, or 3. | [optional]

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_poiby_id**
> Poi get_poiby_id(id)

Points Of Interest Details By Id

This service returns complete details of a chosen point of interest by an identifier. The identifier could be selected from Autocomplete API response.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.poi import Poi
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    id = "id_example" # str | POI unique Identifier.

    # example passing only required values which don't have defaults set
    try:
        # Points Of Interest Details By Id
        api_response = api_instance.get_poiby_id(id)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_poiby_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| POI unique Identifier. |

### Return type

[**Poi**](Poi.md)

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

# **get_pois_by_address**
> PlacesResponse get_pois_by_address()

Get POIs By Address.

This service accepts an address as input and returns nearby points-of-interest places around that address. Additional input features include retrieving data by name, type, standard industrial classifications and category codes, as well as geographic filtering by radius, travel times and travel distances. Response features include JSON/XML as well as CSV download.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.places_response import PlacesResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    address = "address_example" # str | The address to be searched. (optional)
    country = "country_example" # str | Country ISO code. (optional)
    name = "name_example" # str | Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search. (optional)
    type = "type_example" # str | Filters the points of interest (POIs) by place types. (optional)
    category_code = "categoryCode_example" # str | Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. (optional)
    sic_code = "sicCode_example" # str | Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of POIs that can be retrieved (optional)
    search_radius = "searchRadius_example" # str | Radius range within which search is performed. (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Radius unit such as Feet, Kilometers, Miles or Meters (default). (optional)
    travel_time = "travelTime_example" # str | Travel time within which search is performed (POIs which can be reached within travel time). (optional)
    travel_time_unit = "travelTimeUnit_example" # str | Travel time unit such as minutes (default), hours, seconds or milliseconds. (optional)
    travel_distance = "travelDistance_example" # str | Travel distance within which search is performed (POIs which can be reached within travel distance). (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Travel distance unit such as Feet (default), Kilometers, Miles or Meters. (optional)
    travel_mode = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    sort_by = "sortBy_example" # str | Whether to sort the results based on relevance (best match) or by nearest distance from input location. (optional)
    fuzzy_on_name = "fuzzyOnName_example" # str | Whether to allow fuzzy seacrh on name input. (optional)
    page = "page_example" # str | Specifies the page number of results where page size is the value of maxCandidates input in request. (optional)
    match_mode = "matchMode_example" # str | Determine the leniency used to make a match between the input name and the reference data. (optional)
    specific_match_on = "specificMatchOn_example" # str | Specifies the field for the Specific Match Mode. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get POIs By Address.
        api_response = api_instance.get_pois_by_address(address=address, country=country, name=name, type=type, category_code=category_code, sic_code=sic_code, max_candidates=max_candidates, search_radius=search_radius, search_radius_unit=search_radius_unit, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, travel_mode=travel_mode, sort_by=sort_by, fuzzy_on_name=fuzzy_on_name, page=page, match_mode=match_mode, specific_match_on=specific_match_on)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. | [optional]
 **country** | **str**| Country ISO code. | [optional]
 **name** | **str**| Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search. | [optional]
 **type** | **str**| Filters the points of interest (POIs) by place types. | [optional]
 **category_code** | **str**| Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. | [optional]
 **sic_code** | **str**| Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values | [optional]
 **max_candidates** | **str**| Maximum number of POIs that can be retrieved | [optional]
 **search_radius** | **str**| Radius range within which search is performed. | [optional]
 **search_radius_unit** | **str**| Radius unit such as Feet, Kilometers, Miles or Meters (default). | [optional]
 **travel_time** | **str**| Travel time within which search is performed (POIs which can be reached within travel time). | [optional]
 **travel_time_unit** | **str**| Travel time unit such as minutes (default), hours, seconds or milliseconds. | [optional]
 **travel_distance** | **str**| Travel distance within which search is performed (POIs which can be reached within travel distance). | [optional]
 **travel_distance_unit** | **str**| Travel distance unit such as Feet (default), Kilometers, Miles or Meters. | [optional]
 **travel_mode** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **sort_by** | **str**| Whether to sort the results based on relevance (best match) or by nearest distance from input location. | [optional]
 **fuzzy_on_name** | **str**| Whether to allow fuzzy seacrh on name input. | [optional]
 **page** | **str**| Specifies the page number of results where page size is the value of maxCandidates input in request. | [optional]
 **match_mode** | **str**| Determine the leniency used to make a match between the input name and the reference data. | [optional]
 **specific_match_on** | **str**| Specifies the field for the Specific Match Mode. | [optional]

### Return type

[**PlacesResponse**](PlacesResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pois_by_area**
> PlacesResponse get_pois_by_area()

GET Points Of Interest By Area.

This service accepts city or postcode (alongwith country) and returns points-of-interest places within a city or postcode. Additional input features include retrieving data by name, type, standard industrial classifications and category codes, as well as geographic filtering by radius, travel times and travel distances. Response features include JSON/XML as well as CSV download.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.places_response import PlacesResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    area_name1 = "areaName1_example" # str | Specifies the largest geographical area, typically a state or province (optional)
    area_name3 = "areaName3_example" # str | Specifies a city or town name (optional)
    postcode1 = "postcode1_example" # str | Specifies the postcode(ZIP code) in the appropriate format for the country (optional)
    postcode2 = "postcode2_example" # str | Specifies the postcode(ZIP code) extension (optional)
    country = "country_example" # str | Country ISO code (optional)
    name = "name_example" # str | Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search (optional)
    type = "type_example" # str | Filters the points of interest (POIs) by place types (optional)
    category_code = "categoryCode_example" # str | Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values (optional)
    sic_code = "sicCode_example" # str | Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of POIs that can be retrieved (optional)
    fuzzy_on_name = "fuzzyOnName_example" # str | Whether to allow fuzzy seacrh on name input (optional)
    page = "page_example" # str | Specifies the page number of results where page size is the value of maxCandidates input in request (optional)
    match_mode = "matchMode_example" # str | Determine the leniency used to make a match between the input name and the reference data (optional)
    specific_match_on = "specificMatchOn_example" # str | Specifies the field for the Specific Match Mode (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET Points Of Interest By Area.
        api_response = api_instance.get_pois_by_area(area_name1=area_name1, area_name3=area_name3, postcode1=postcode1, postcode2=postcode2, country=country, name=name, type=type, category_code=category_code, sic_code=sic_code, max_candidates=max_candidates, fuzzy_on_name=fuzzy_on_name, page=page, match_mode=match_mode, specific_match_on=specific_match_on)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_by_area: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area_name1** | **str**| Specifies the largest geographical area, typically a state or province | [optional]
 **area_name3** | **str**| Specifies a city or town name | [optional]
 **postcode1** | **str**| Specifies the postcode(ZIP code) in the appropriate format for the country | [optional]
 **postcode2** | **str**| Specifies the postcode(ZIP code) extension | [optional]
 **country** | **str**| Country ISO code | [optional]
 **name** | **str**| Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search | [optional]
 **type** | **str**| Filters the points of interest (POIs) by place types | [optional]
 **category_code** | **str**| Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values | [optional]
 **sic_code** | **str**| Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values | [optional]
 **max_candidates** | **str**| Maximum number of POIs that can be retrieved | [optional]
 **fuzzy_on_name** | **str**| Whether to allow fuzzy seacrh on name input | [optional]
 **page** | **str**| Specifies the page number of results where page size is the value of maxCandidates input in request | [optional]
 **match_mode** | **str**| Determine the leniency used to make a match between the input name and the reference data | [optional]
 **specific_match_on** | **str**| Specifies the field for the Specific Match Mode | [optional]

### Return type

[**PlacesResponse**](PlacesResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pois_by_geometry**
> PlacesResponse get_pois_by_geometry(poiby_geometry_request)

Points Of Interest By Boundary

Accepts a user-defined boundary as input and returns all Points of Interest within the boundary. Additionally, user can filter the response by name, type, standard industrial classifications and category codes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.poiby_geometry_request import POIByGeometryRequest
from com.precisely.apis.model.places_response import PlacesResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    poiby_geometry_request = POIByGeometryRequest(
        name="name_example",
        type="type_example",
        category_code="category_code_example",
        sic_code="sic_code_example",
        max_candidates="max_candidates_example",
        fuzzy_on_name="fuzzy_on_name_example",
        page="page_example",
        match_mode="match_mode_example",
        specific_match_on="specific_match_on_example",
        geometry=Geometry(
            type="type_example",
            coordinates=[
                3.14,
            ],
        ),
        geometry_as_text="geometry_as_text_example",
    ) # POIByGeometryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Points Of Interest By Boundary
        api_response = api_instance.get_pois_by_geometry(poiby_geometry_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_by_geometry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poiby_geometry_request** | [**POIByGeometryRequest**](POIByGeometryRequest.md)|  |

### Return type

[**PlacesResponse**](PlacesResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pois_by_location**
> PlacesResponse get_pois_by_location(longitude, latitude)

Get POIs By Location.

This service accepts latitude/longitude as input and returns nearby points-of-interest places around that location. Additional input features include retrieving data by name, type, standard industrial classifications and category codes, as well as geographic filtering by radius, travel times and travel distances. Response features include JSON/XML as well as CSV download

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.places_response import PlacesResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location.
    latitude = "latitude_example" # str | Latitude of the location.
    name = "name_example" # str | Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search. (optional)
    type = "type_example" # str | Filters the points of interest (POIs) by place types. (optional)
    category_code = "categoryCode_example" # str | Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. (optional)
    sic_code = "sicCode_example" # str | Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of POIs that can be retrieved (optional)
    search_radius = "searchRadius_example" # str | Radius range within which search is performed. (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Radius unit such as Feet, Kilometers, Miles or Meters (default). (optional)
    travel_time = "travelTime_example" # str | Travel time within which search is performed (POIs which can be reached within travel time). (optional)
    travel_time_unit = "travelTimeUnit_example" # str | Travel time unit such as minutes (default), hours, seconds or milliseconds. (optional)
    travel_distance = "travelDistance_example" # str | Travel distance within which search is performed (POIs which can be reached within travel distance). (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Travel distance unit such as Feet (default), Kilometers, Miles or Meters. (optional)
    travel_mode = "travelMode_example" # str | Mode of commute. (optional)
    sort_by = "sortBy_example" # str | Whether to sort the results based on relevance (best match) or by nearest distance from input location. (optional)
    fuzzy_on_name = "fuzzyOnName_example" # str | Whether to allow fuzzy seacrh on name input. (optional)
    page = "page_example" # str | Specifies the page number of results where page size is the value of maxCandidates input in request. (optional)
    match_mode = "matchMode_example" # str | Determine the leniency used to make a match between the input name and the reference data. (optional)
    specific_match_on = "specificMatchOn_example" # str | Specifies the field for the Specific Match Mode. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get POIs By Location.
        api_response = api_instance.get_pois_by_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_by_location: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get POIs By Location.
        api_response = api_instance.get_pois_by_location(longitude, latitude, name=name, type=type, category_code=category_code, sic_code=sic_code, max_candidates=max_candidates, search_radius=search_radius, search_radius_unit=search_radius_unit, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, travel_mode=travel_mode, sort_by=sort_by, fuzzy_on_name=fuzzy_on_name, page=page, match_mode=match_mode, specific_match_on=specific_match_on)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. |
 **latitude** | **str**| Latitude of the location. |
 **name** | **str**| Specifies the name of the place (POI) to be searched. Also performs search on partially specified names. It requires minimum 3 characters to search. | [optional]
 **type** | **str**| Filters the points of interest (POIs) by place types. | [optional]
 **category_code** | **str**| Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. | [optional]
 **sic_code** | **str**| Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values | [optional]
 **max_candidates** | **str**| Maximum number of POIs that can be retrieved | [optional]
 **search_radius** | **str**| Radius range within which search is performed. | [optional]
 **search_radius_unit** | **str**| Radius unit such as Feet, Kilometers, Miles or Meters (default). | [optional]
 **travel_time** | **str**| Travel time within which search is performed (POIs which can be reached within travel time). | [optional]
 **travel_time_unit** | **str**| Travel time unit such as minutes (default), hours, seconds or milliseconds. | [optional]
 **travel_distance** | **str**| Travel distance within which search is performed (POIs which can be reached within travel distance). | [optional]
 **travel_distance_unit** | **str**| Travel distance unit such as Feet (default), Kilometers, Miles or Meters. | [optional]
 **travel_mode** | **str**| Mode of commute. | [optional]
 **sort_by** | **str**| Whether to sort the results based on relevance (best match) or by nearest distance from input location. | [optional]
 **fuzzy_on_name** | **str**| Whether to allow fuzzy seacrh on name input. | [optional]
 **page** | **str**| Specifies the page number of results where page size is the value of maxCandidates input in request. | [optional]
 **match_mode** | **str**| Determine the leniency used to make a match between the input name and the reference data. | [optional]
 **specific_match_on** | **str**| Specifies the field for the Specific Match Mode. | [optional]

### Return type

[**PlacesResponse**](PlacesResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pois_count**
> PoiCount get_pois_count(content_type, poi_count_request)

Points Of Interest Count

Accepts a user-defined boundary as input and returns the Count number of POIs within the boundary. Additionally, user can request the count of filtered POIs by name, type, standard industrial classifications and category codes within the given polygon.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.poi_count import PoiCount
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.poi_count_request import PoiCountRequest
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    content_type = "Content-Type_example" # str | 
    poi_count_request = PoiCountRequest(
        name="name_example",
        type="type_example",
        category_code="category_code_example",
        sic_code="sic_code_example",
        fuzzy_on_name="fuzzy_on_name_example",
        match_mode="match_mode_example",
        specific_match_on="specific_match_on_example",
        geometry=Geometry(
            type="type_example",
            coordinates=[
                3.14,
            ],
        ),
        geometry_as_text="geometry_as_text_example",
    ) # PoiCountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Points Of Interest Count
        api_response = api_instance.get_pois_count(content_type, poi_count_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_pois_count: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  |
 **poi_count_request** | [**PoiCountRequest**](PoiCountRequest.md)|  |

### Return type

[**PoiCount**](PoiCount.md)

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

# **get_sic_metadata**
> MetadataResponse get_sic_metadata()

Get SIC Metadata

This service returns a list of standard industrial classification codes & associated metadata which can then be used as inputs for querying the Points of Interest By Address or Location methods listed above.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.metadata_response import MetadataResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    sic_code = "sicCode_example" # str | 4 or 8 digits SIC code to filter the response. (optional)
    level = "level_example" # str | 1 or 2. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SIC Metadata
        api_response = api_instance.get_sic_metadata(sic_code=sic_code, level=level)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->get_sic_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sic_code** | **str**| 4 or 8 digits SIC code to filter the response. | [optional]
 **level** | **str**| 1 or 2. | [optional]

### Return type

[**MetadataResponse**](MetadataResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pois_autocomplete**
> PlacesResponse pois_autocomplete()

Points Of Interest Autocomplete

This service accepts partial text input and returns matching points of interest, sorted by relevance or distance.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import places_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.places_response import PlacesResponse
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
    api_instance = places_service__api.PlacesServiceApi(api_client)
    x_forwarded_for = "X-Forwarded-For_example" # str |  (optional)
    longitude = "longitude_example" # str | Longitude of the location. (optional)
    latitude = "latitude_example" # str | Latitude of the location. (optional)
    search_text = "searchText_example" # str | Free text which will accept a multi-word string. Combination of POI name and address is possible. (optional)
    search_on_name_only = "N" # str |  (optional) if omitted the server will use the default value of "N"
    search_radius = "searchRadius_example" # str | Radius range within which search is performed. (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Radius unit such as Feet, Kilometers, Miles or Meters (default). (optional)
    travel_time = "travelTime_example" # str | Travel time within which search is performed (POIs which can be reached within travel time). (optional)
    travel_time_unit = "travelTimeUnit_example" # str | Travel time unit such as minutes (default), hours, seconds or milliseconds. (optional)
    travel_distance = "travelDistance_example" # str | Travel distance within which search is performed (POIs which can be reached within travel distance). (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Travel distance unit such as Feet (default), Kilometers, Miles or Meters. (optional)
    travel_mode = "driving" # str | Mode of commute. (optional) if omitted the server will use the default value of "driving"
    country = "country_example" # str | Country ISO code. (optional)
    area_name1 = "areaName1_example" # str | Specifies the largest geographical area, typically a state or province. (optional)
    area_name3 = "areaName3_example" # str | Specifies a city or town name. (optional)
    postcode1 = "postcode1_example" # str | Specifies the postcode(ZIP code) in the appropriate format for the country. (optional)
    postcode2 = "postcode2_example" # str | Specifies the postcode(ZIP code) extension. (optional)
    ip_address = "ipAddress_example" # str | IP address which will be used to auto detect the location in order to serve contextually relevant results. (optional)
    auto_detect_location = "autoDetectLocation_example" # str | Specifies whether to detect client's location using IP address. If IP address(below) is not provided and autoDetectLocation is set 'True' then IP address will be picked from HTTP request automatically. (optional)
    type = "type_example" # str | Filters the points of interest (POIs) by place types. (optional)
    category_code = "categoryCode_example" # str | Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. (optional)
    sic_code = "sicCode_example" # str | Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values. (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of POIs that can be retrieved. (optional)
    sort_by = "sortBy_example" # str | sortBy (optional)
    match_mode = "matchMode_example" # str | Determine the leniency used to make a match between the input name and the reference data. (optional)
    specific_match_on = "specificMatchOn_example" # str | Specifies the field for the Specific Match Mode. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Points Of Interest Autocomplete
        api_response = api_instance.pois_autocomplete(x_forwarded_for=x_forwarded_for, longitude=longitude, latitude=latitude, search_text=search_text, search_on_name_only=search_on_name_only, search_radius=search_radius, search_radius_unit=search_radius_unit, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, travel_mode=travel_mode, country=country, area_name1=area_name1, area_name3=area_name3, postcode1=postcode1, postcode2=postcode2, ip_address=ip_address, auto_detect_location=auto_detect_location, type=type, category_code=category_code, sic_code=sic_code, max_candidates=max_candidates, sort_by=sort_by, match_mode=match_mode, specific_match_on=specific_match_on)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PlacesServiceApi->pois_autocomplete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_forwarded_for** | **str**|  | [optional]
 **longitude** | **str**| Longitude of the location. | [optional]
 **latitude** | **str**| Latitude of the location. | [optional]
 **search_text** | **str**| Free text which will accept a multi-word string. Combination of POI name and address is possible. | [optional]
 **search_on_name_only** | **str**|  | [optional] if omitted the server will use the default value of "N"
 **search_radius** | **str**| Radius range within which search is performed. | [optional]
 **search_radius_unit** | **str**| Radius unit such as Feet, Kilometers, Miles or Meters (default). | [optional]
 **travel_time** | **str**| Travel time within which search is performed (POIs which can be reached within travel time). | [optional]
 **travel_time_unit** | **str**| Travel time unit such as minutes (default), hours, seconds or milliseconds. | [optional]
 **travel_distance** | **str**| Travel distance within which search is performed (POIs which can be reached within travel distance). | [optional]
 **travel_distance_unit** | **str**| Travel distance unit such as Feet (default), Kilometers, Miles or Meters. | [optional]
 **travel_mode** | **str**| Mode of commute. | [optional] if omitted the server will use the default value of "driving"
 **country** | **str**| Country ISO code. | [optional]
 **area_name1** | **str**| Specifies the largest geographical area, typically a state or province. | [optional]
 **area_name3** | **str**| Specifies a city or town name. | [optional]
 **postcode1** | **str**| Specifies the postcode(ZIP code) in the appropriate format for the country. | [optional]
 **postcode2** | **str**| Specifies the postcode(ZIP code) extension. | [optional]
 **ip_address** | **str**| IP address which will be used to auto detect the location in order to serve contextually relevant results. | [optional]
 **auto_detect_location** | **str**| Specifies whether to detect client&#39;s location using IP address. If IP address(below) is not provided and autoDetectLocation is set &#39;True&#39; then IP address will be picked from HTTP request automatically. | [optional]
 **type** | **str**| Filters the points of interest (POIs) by place types. | [optional]
 **category_code** | **str**| Acts as a filter to narrow down and refine POI search results. The category codes are unique 4, 6, or 11 digit numeric values. | [optional]
 **sic_code** | **str**| Acts as a filter to narrow down and refine POI search results. The SIC codes are unique 4 or 8 digit numerical values. | [optional]
 **max_candidates** | **str**| Maximum number of POIs that can be retrieved. | [optional]
 **sort_by** | **str**| sortBy | [optional]
 **match_mode** | **str**| Determine the leniency used to make a match between the input name and the reference data. | [optional]
 **specific_match_on** | **str**| Specifies the field for the Specific Match Mode. | [optional]

### Return type

[**PlacesResponse**](PlacesResponse.md)

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

