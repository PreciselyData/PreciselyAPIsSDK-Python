# com.precisely.apis.TypeaheadServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_v2**](TypeaheadServiceApi.md#search_v2) | **GET** /typeahead/v1/locations | Typeahead Search


# **search_v2**
> TypeaheadLocations search_v2(search_text)

Typeahead Search

Performs search to retrieve list of places by input text and location vicinity.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import typeahead_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.typeahead_locations import TypeaheadLocations
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
    api_instance = typeahead_service_api.TypeaheadServiceApi(api_client)
    search_text = "searchText_example" # str | The input to be searched.
    latitude = "latitude_example" # str | Latitude of the location. We need to make sure that either Lat/Lng or Country is provided to API (optional)
    longitude = "longitude_example" # str | Longitude of the location. We need to make sure that either Lat/Lng or Country is provided to API (optional)
    search_radius = "searchRadius_example" # str | Radius range within which search is performed. (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Radius unit such as Feet, Kilometers, Miles or Meters. (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of POIs that can be retrieved. (optional)
    country = "country_example" # str | Country ISO code. We need to make sure that either Lat/Lng or Country is provided to API (optional)
    match_on_address_number = "matchOnAddressNumber_example" # str | Option so that we force api to match on address number (optional)
    auto_detect_location = "autoDetectLocation_example" # str | Option to allow API to detect origin of API request automatically (optional)
    ip_address = "ipAddress_example" # str |  (optional)
    area_name1 = "areaName1_example" # str | State province of the input to be searched (optional)
    area_name3 = "areaName3_example" # str | City of the input to be searched (optional)
    post_code = "postCode_example" # str | Postal Code of the input to be searched (optional)
    return_admin_areas_only = "returnAdminAreasOnly_example" # str | if value set 'Y' then it will only do a matching on postcode or areaName1, areaName2, areaName3 and areaName4 fields in the data (optional)
    include_ranges_details = "includeRangesDetails_example" # str | if value set 'Y' then display all unit info of ranges, if value set 'N' then don't show ranges (optional)
    search_type = "searchType_example" # str | Preference to control search type of interactive requests. (optional)
    search_on_address_number = "searchOnAddressNumber_example" # str | Preference to search on address number. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Typeahead Search
        api_response = api_instance.search_v2(search_text)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TypeaheadServiceApi->search_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Typeahead Search
        api_response = api_instance.search_v2(search_text, latitude=latitude, longitude=longitude, search_radius=search_radius, search_radius_unit=search_radius_unit, max_candidates=max_candidates, country=country, match_on_address_number=match_on_address_number, auto_detect_location=auto_detect_location, ip_address=ip_address, area_name1=area_name1, area_name3=area_name3, post_code=post_code, return_admin_areas_only=return_admin_areas_only, include_ranges_details=include_ranges_details, search_type=search_type, search_on_address_number=search_on_address_number)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling TypeaheadServiceApi->search_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_text** | **str**| The input to be searched. |
 **latitude** | **str**| Latitude of the location. We need to make sure that either Lat/Lng or Country is provided to API | [optional]
 **longitude** | **str**| Longitude of the location. We need to make sure that either Lat/Lng or Country is provided to API | [optional]
 **search_radius** | **str**| Radius range within which search is performed. | [optional]
 **search_radius_unit** | **str**| Radius unit such as Feet, Kilometers, Miles or Meters. | [optional]
 **max_candidates** | **str**| Maximum number of POIs that can be retrieved. | [optional]
 **country** | **str**| Country ISO code. We need to make sure that either Lat/Lng or Country is provided to API | [optional]
 **match_on_address_number** | **str**| Option so that we force api to match on address number | [optional]
 **auto_detect_location** | **str**| Option to allow API to detect origin of API request automatically | [optional]
 **ip_address** | **str**|  | [optional]
 **area_name1** | **str**| State province of the input to be searched | [optional]
 **area_name3** | **str**| City of the input to be searched | [optional]
 **post_code** | **str**| Postal Code of the input to be searched | [optional]
 **return_admin_areas_only** | **str**| if value set &#39;Y&#39; then it will only do a matching on postcode or areaName1, areaName2, areaName3 and areaName4 fields in the data | [optional]
 **include_ranges_details** | **str**| if value set &#39;Y&#39; then display all unit info of ranges, if value set &#39;N&#39; then don&#39;t show ranges | [optional]
 **search_type** | **str**| Preference to control search type of interactive requests. | [optional]
 **search_on_address_number** | **str**| Preference to search on address number. | [optional]

### Return type

[**TypeaheadLocations**](TypeaheadLocations.md)

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

