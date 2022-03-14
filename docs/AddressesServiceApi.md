# com.precisely.apis.AddressesServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_addresses_count_by_boundary_name**](AddressesServiceApi.md#get_addresses_count_by_boundary_name) | **GET** /addresses/v1/addresscount/byboundaryname | Addresses Count by Boundary Name.
[**get_addresses_countby_boundary**](AddressesServiceApi.md#get_addresses_countby_boundary) | **POST** /addresses/v1/addresscount/byboundary | Addresses count by Boundary.
[**get_addressesby_boundary**](AddressesServiceApi.md#get_addressesby_boundary) | **POST** /addresses/v1/address/byboundary | Addresses by Boundary.
[**get_addressesby_boundary_name**](AddressesServiceApi.md#get_addressesby_boundary_name) | **GET** /addresses/v1/address/byboundaryname | Addresses by Boundary Name.


# **get_addresses_count_by_boundary_name**
> AddressesCount get_addresses_count_by_boundary_name(country)

Addresses Count by Boundary Name.

This service accepts zip code, neighborhood, county, or city names, and returns the total number of addresses associated with these names.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import addresses_service__api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.addresses_count import AddressesCount
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
    api_instance = addresses_service__api.AddressesServiceApi(api_client)
    country = "country_example" # str | Name of country. Acceptable values are CAN, USA.
    area_name1 = "areaName1_example" # str | Specifies the largest geographical area, typically a state or province. (optional)
    area_name2 = "areaName2_example" # str | Specifies the secondary geographic area, typically a county or district. (optional)
    area_name3 = "areaName3_example" # str | Specifies a city or town name. (optional)
    area_name4 = "areaName4_example" # str | Specifies a city subdivision or locality/neighborhood. (optional)
    post_code = "postCode_example" # str | Specifies the postcode (ZIP code) in the appropriate format for the country. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Addresses Count by Boundary Name.
        api_response = api_instance.get_addresses_count_by_boundary_name(country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addresses_count_by_boundary_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Addresses Count by Boundary Name.
        api_response = api_instance.get_addresses_count_by_boundary_name(country, area_name1=area_name1, area_name2=area_name2, area_name3=area_name3, area_name4=area_name4, post_code=post_code)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addresses_count_by_boundary_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Name of country. Acceptable values are CAN, USA. |
 **area_name1** | **str**| Specifies the largest geographical area, typically a state or province. | [optional]
 **area_name2** | **str**| Specifies the secondary geographic area, typically a county or district. | [optional]
 **area_name3** | **str**| Specifies a city or town name. | [optional]
 **area_name4** | **str**| Specifies a city subdivision or locality/neighborhood. | [optional]
 **post_code** | **str**| Specifies the postcode (ZIP code) in the appropriate format for the country. | [optional]

### Return type

[**AddressesCount**](AddressesCount.md)

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

# **get_addresses_countby_boundary**
> AddressesCount get_addresses_countby_boundary(addresses_by_boundary_request)

Addresses count by Boundary.

This service accepts custom geographic boundaries or drive time & drive distance, returns the total number of addresses within these boundaries.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import addresses_service__api
from com.precisely.apis.model.addresses_by_boundary_request import AddressesByBoundaryRequest
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.addresses_count import AddressesCount
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
    api_instance = addresses_service__api.AddressesServiceApi(api_client)
    addresses_by_boundary_request = AddressesByBoundaryRequest(
        preferences=AddressesPreferences(
            max_candidates="max_candidates_example",
            page="page_example",
        ),
        geometry=Geometry(
            type="type_example",
            coordinates=[
                3.14,
            ],
        ),
        geometry_as_text="geometry_as_text_example",
        latitude=3.14,
        longitude=3.14,
        travel_time="travel_time_example",
        travel_time_unit="travel_time_unit_example",
        travel_distance="travel_distance_example",
        travel_distance_unit="travel_distance_unit_example",
        travel_mode="travel_mode_example",
    ) # AddressesByBoundaryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Addresses count by Boundary.
        api_response = api_instance.get_addresses_countby_boundary(addresses_by_boundary_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addresses_countby_boundary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addresses_by_boundary_request** | [**AddressesByBoundaryRequest**](AddressesByBoundaryRequest.md)|  |

### Return type

[**AddressesCount**](AddressesCount.md)

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

# **get_addressesby_boundary**
> AddressesResponse get_addressesby_boundary(addresses_by_boundary_request)

Addresses by Boundary.

This service accepts custom geographic boundaries or drive time & drive distance, returns all known & valid addresses within these boundaries.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import addresses_service__api
from com.precisely.apis.model.addresses_by_boundary_request import AddressesByBoundaryRequest
from com.precisely.apis.model.addresses_response import AddressesResponse
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
    api_instance = addresses_service__api.AddressesServiceApi(api_client)
    addresses_by_boundary_request = AddressesByBoundaryRequest(
        preferences=AddressesPreferences(
            max_candidates="max_candidates_example",
            page="page_example",
        ),
        geometry=Geometry(
            type="type_example",
            coordinates=[
                3.14,
            ],
        ),
        geometry_as_text="geometry_as_text_example",
        latitude=3.14,
        longitude=3.14,
        travel_time="travel_time_example",
        travel_time_unit="travel_time_unit_example",
        travel_distance="travel_distance_example",
        travel_distance_unit="travel_distance_unit_example",
        travel_mode="travel_mode_example",
    ) # AddressesByBoundaryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Addresses by Boundary.
        api_response = api_instance.get_addressesby_boundary(addresses_by_boundary_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addressesby_boundary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addresses_by_boundary_request** | [**AddressesByBoundaryRequest**](AddressesByBoundaryRequest.md)|  |

### Return type

[**AddressesResponse**](AddressesResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml, text/csv


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_addressesby_boundary_name**
> AddressesResponse get_addressesby_boundary_name(country)

Addresses by Boundary Name.

This service accepts zip code, neighborhood, county, or city names, and returns all known & valid addresses associated with these names.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import addresses_service__api
from com.precisely.apis.model.addresses_response import AddressesResponse
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
    api_instance = addresses_service__api.AddressesServiceApi(api_client)
    country = "country_example" # str | Name of country. Acceptable values are CAN, USA.
    area_name1 = "areaName1_example" # str | Specifies the largest geographical area, typically a state or province. (optional)
    area_name2 = "areaName2_example" # str | Specifies the secondary geographic area, typically a county or district. (optional)
    area_name3 = "areaName3_example" # str | Specifies a city or town name. (optional)
    area_name4 = "areaName4_example" # str | Specifies a city subdivision or locality/neighborhood. (optional)
    post_code = "postCode_example" # str | Specifies the postcode (ZIP code) in the appropriate format for the country. (optional)
    max_candidates = "maxCandidates_example" # str | Maximum number of addresses to be returned in response. Max. value is 100 for XML/JSON, and 2000 for CSV. (optional)
    page = "page_example" # str | Response will indicate the page number. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Addresses by Boundary Name.
        api_response = api_instance.get_addressesby_boundary_name(country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addressesby_boundary_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Addresses by Boundary Name.
        api_response = api_instance.get_addressesby_boundary_name(country, area_name1=area_name1, area_name2=area_name2, area_name3=area_name3, area_name4=area_name4, post_code=post_code, max_candidates=max_candidates, page=page)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressesServiceApi->get_addressesby_boundary_name: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Name of country. Acceptable values are CAN, USA. |
 **area_name1** | **str**| Specifies the largest geographical area, typically a state or province. | [optional]
 **area_name2** | **str**| Specifies the secondary geographic area, typically a county or district. | [optional]
 **area_name3** | **str**| Specifies a city or town name. | [optional]
 **area_name4** | **str**| Specifies a city subdivision or locality/neighborhood. | [optional]
 **post_code** | **str**| Specifies the postcode (ZIP code) in the appropriate format for the country. | [optional]
 **max_candidates** | **str**| Maximum number of addresses to be returned in response. Max. value is 100 for XML/JSON, and 2000 for CSV. | [optional]
 **page** | **str**| Response will indicate the page number. | [optional]

### Return type

[**AddressesResponse**](AddressesResponse.md)

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

