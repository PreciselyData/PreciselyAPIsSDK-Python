# com.precisely.apis.SchoolsServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schools_by_address**](SchoolsServiceApi.md#get_schools_by_address) | **GET** /schools/v1/school/byaddress | Search Nearby Schools by Address


# **get_schools_by_address**
> SchoolsNearByResponse get_schools_by_address(address)

Search Nearby Schools by Address

Search Nearby Schools by Address

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import schools_service_api
from com.precisely.apis.model.schools_near_by_response import SchoolsNearByResponse
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
    api_instance = schools_service_api.SchoolsServiceApi(api_client)
    address = "address_example" # str | free form address text
    ed_level = "edLevel_example" # str | Single digit code for education level applicable values are P -> primary, M -> Middle, H -> High, O -> Mixed Grades for public school type andE -> Elementary , S -> Secondary , O -> Others mixed grades for private schools  (optional)
    school_type = "schoolType_example" # str | Single digit code for schoolTypes applicable values are PRI and PUB (optional)
    school_sub_type = "schoolSubType_example" # str | Single digit code for schoolSubType Applicable values are C, M, A, R, I, L, P, V, U, S (i.e. Charter, Magnet, Alternative, Regular, Indian, Military, Reportable Program, Vocational, Unknown, Special Education) (optional)
    gender = "gender_example" # str | Single digit code for gender Applicable values are C, F, M (Coed, All Females, All Males) Applicable for Private Schools Only (optional)
    assigned_schools_only = "assignedSchoolsOnly_example" # str | Single digit code for assignedSchoolOnly applicable values are  Y/N  (optional)
    district_schools_only = "districtSchoolsOnly_example" # str | Single digit code for districtSchoolOnly applicable values are Y/N  (optional)
    search_radius = "searchRadius_example" # str | Search Radius within which schools are searched (optional)
    search_radius_unit = "searchRadiusUnit_example" # str | Search Radius unit applicable values are feet,kilometers,miles,meters (optional)
    travel_time = "travelTime_example" # str | Travel Time based on ‘travelMode’ within which schools are searched. (optional)
    travel_time_unit = "travelTimeUnit_example" # str | Travel Time unit applicable values are minutes,hours,seconds,milliseconds  (optional)
    travel_distance = "travelDistance_example" # str | Travel Distance based on ‘travelMode’ within which schools are searched. (optional)
    travel_distance_unit = "travelDistanceUnit_example" # str | Travel distanceUnit applicable values are feet,kilometers,miles,meters (optional)
    travel_mode = "travelMode_example" # str | Travel mode Required when travelDistance or travelTime is specified. Accepted values are walking,driving (optional)
    max_candidates = "maxCandidates_example" # str | Max result to search  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Nearby Schools by Address
        api_response = api_instance.get_schools_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling SchoolsServiceApi->get_schools_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Nearby Schools by Address
        api_response = api_instance.get_schools_by_address(address, ed_level=ed_level, school_type=school_type, school_sub_type=school_sub_type, gender=gender, assigned_schools_only=assigned_schools_only, district_schools_only=district_schools_only, search_radius=search_radius, search_radius_unit=search_radius_unit, travel_time=travel_time, travel_time_unit=travel_time_unit, travel_distance=travel_distance, travel_distance_unit=travel_distance_unit, travel_mode=travel_mode, max_candidates=max_candidates)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling SchoolsServiceApi->get_schools_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| free form address text |
 **ed_level** | **str**| Single digit code for education level applicable values are P -&gt; primary, M -&gt; Middle, H -&gt; High, O -&gt; Mixed Grades for public school type andE -&gt; Elementary , S -&gt; Secondary , O -&gt; Others mixed grades for private schools  | [optional]
 **school_type** | **str**| Single digit code for schoolTypes applicable values are PRI and PUB | [optional]
 **school_sub_type** | **str**| Single digit code for schoolSubType Applicable values are C, M, A, R, I, L, P, V, U, S (i.e. Charter, Magnet, Alternative, Regular, Indian, Military, Reportable Program, Vocational, Unknown, Special Education) | [optional]
 **gender** | **str**| Single digit code for gender Applicable values are C, F, M (Coed, All Females, All Males) Applicable for Private Schools Only | [optional]
 **assigned_schools_only** | **str**| Single digit code for assignedSchoolOnly applicable values are  Y/N  | [optional]
 **district_schools_only** | **str**| Single digit code for districtSchoolOnly applicable values are Y/N  | [optional]
 **search_radius** | **str**| Search Radius within which schools are searched | [optional]
 **search_radius_unit** | **str**| Search Radius unit applicable values are feet,kilometers,miles,meters | [optional]
 **travel_time** | **str**| Travel Time based on ‘travelMode’ within which schools are searched. | [optional]
 **travel_time_unit** | **str**| Travel Time unit applicable values are minutes,hours,seconds,milliseconds  | [optional]
 **travel_distance** | **str**| Travel Distance based on ‘travelMode’ within which schools are searched. | [optional]
 **travel_distance_unit** | **str**| Travel distanceUnit applicable values are feet,kilometers,miles,meters | [optional]
 **travel_mode** | **str**| Travel mode Required when travelDistance or travelTime is specified. Accepted values are walking,driving | [optional]
 **max_candidates** | **str**| Max result to search  | [optional]

### Return type

[**SchoolsNearByResponse**](SchoolsNearByResponse.md)

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

