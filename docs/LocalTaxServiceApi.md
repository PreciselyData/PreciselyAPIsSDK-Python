# com.precisely.apis.LocalTaxServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_tax_by_address**](LocalTaxServiceApi.md#get_batch_tax_by_address) | **POST** /localtax/v1/tax/{taxRateTypeId}/byaddress | Post Tax By Address
[**get_batch_tax_by_location**](LocalTaxServiceApi.md#get_batch_tax_by_location) | **POST** /localtax/v1/tax/{taxRateTypeId}/bylocation | Post Tax By Location
[**get_batch_tax_rate_by_address**](LocalTaxServiceApi.md#get_batch_tax_rate_by_address) | **POST** /localtax/v1/taxrate/{taxRateTypeId}/byaddress | Post Taxrate By Address
[**get_batch_tax_rate_by_location**](LocalTaxServiceApi.md#get_batch_tax_rate_by_location) | **POST** /localtax/v1/taxrate/{taxRateTypeId}/bylocation | Post Taxrate By Location
[**get_ipd_tax_by_address**](LocalTaxServiceApi.md#get_ipd_tax_by_address) | **GET** /localtax/v1/taxdistrict/ipd/byaddress | Get IPD Tax by Address
[**get_ipd_tax_by_address_batch**](LocalTaxServiceApi.md#get_ipd_tax_by_address_batch) | **POST** /localtax/v1/taxdistrict/ipd/byaddress | Get IPD Tax for batch requests.
[**get_specific_tax_by_address**](LocalTaxServiceApi.md#get_specific_tax_by_address) | **GET** /localtax/v1/tax/{taxRateTypeId}/byaddress | Get Tax By Address
[**get_specific_tax_by_location**](LocalTaxServiceApi.md#get_specific_tax_by_location) | **GET** /localtax/v1/tax/{taxRateTypeId}/bylocation | Get Tax By Location
[**get_specific_tax_rate_by_address**](LocalTaxServiceApi.md#get_specific_tax_rate_by_address) | **GET** /localtax/v1/taxrate/{taxRateTypeId}/byaddress | Get Taxrate By Address
[**get_specific_tax_rate_by_location**](LocalTaxServiceApi.md#get_specific_tax_rate_by_location) | **GET** /localtax/v1/taxrate/{taxRateTypeId}/bylocation | Get Taxrate By Location


# **get_batch_tax_by_address**
> TaxResponses get_batch_tax_by_address(tax_rate_type_id, tax_address_request)

Post Tax By Address

This is a Batch offering for 'Tax By Address' service. It accepts a single address, purchase amount or a list of addresses, purchase amounts and retrieve applicable taxes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_responses import TaxResponses
from com.precisely.apis.model.tax_address_request import TaxAddressRequest
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | 
    tax_address_request = TaxAddressRequest(
        preferences=LocalTaxPreferences(
            custom_preferences={
                "key": {},
            },
            default_buffer_width="default_buffer_width_example",
            distance_units="distance_units_example",
            fallback_to_geographic="fallback_to_geographic_example",
            lat_long_format="lat_long_format_example",
            lat_long_offset="lat_long_offset_example",
            match_mode="match_mode_example",
            output_casing="output_casing_example",
            return_census_fields="return_census_fields_example",
            return_lat_long_fields="return_lat_long_fields_example",
            squeeze="squeeze_example",
            tax_ratetype_id="tax_ratetype_id_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
        ),
        tax_addresses=[
            TaxAddress(
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
                post_code1="post_code1_example",
                post_code_ext="post_code_ext_example",
                country="country_example",
                address_number="address_number_example",
                street_name="street_name_example",
                unit_type="unit_type_example",
                unit_value="unit_value_example",
                distance_units="distance_units_example",
                buffer_width="buffer_width_example",
                user_buffer_width="user_buffer_width_example",
                purchase_amount="purchase_amount_example",
            ),
        ],
    ) # TaxAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Tax By Address
        api_response = api_instance.get_batch_tax_by_address(tax_rate_type_id, tax_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_batch_tax_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**|  |
 **tax_address_request** | [**TaxAddressRequest**](TaxAddressRequest.md)|  |

### Return type

[**TaxResponses**](TaxResponses.md)

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

# **get_batch_tax_by_location**
> TaxResponses get_batch_tax_by_location(tax_rate_type_id, tax_location_request)

Post Tax By Location

This is a Batch offering for 'Tax By Location' service. It accepts a single location coordinate, purchase amount or a list of location coordinates, purchase amounts and retrieve applicable tax.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_responses import TaxResponses
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.tax_location_request import TaxLocationRequest
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | 
    tax_location_request = TaxLocationRequest(
        preferences=LocalTaxPreferences(
            custom_preferences={
                "key": {},
            },
            default_buffer_width="default_buffer_width_example",
            distance_units="distance_units_example",
            fallback_to_geographic="fallback_to_geographic_example",
            lat_long_format="lat_long_format_example",
            lat_long_offset="lat_long_offset_example",
            match_mode="match_mode_example",
            output_casing="output_casing_example",
            return_census_fields="return_census_fields_example",
            return_lat_long_fields="return_lat_long_fields_example",
            squeeze="squeeze_example",
            tax_ratetype_id="tax_ratetype_id_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
        ),
        locations=[
            TaxLocations(
                geometry=TaxGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
    ) # TaxLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Tax By Location
        api_response = api_instance.get_batch_tax_by_location(tax_rate_type_id, tax_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_batch_tax_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**|  |
 **tax_location_request** | [**TaxLocationRequest**](TaxLocationRequest.md)|  |

### Return type

[**TaxResponses**](TaxResponses.md)

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

# **get_batch_tax_rate_by_address**
> TaxResponses get_batch_tax_rate_by_address(tax_rate_type_id, tax_rate_address_request)

Post Taxrate By Address

This is a Batch offering for 'Taxrate By Address' service. It accepts a single address or a list of addresses and retrieve applicable tax rates.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_responses import TaxResponses
from com.precisely.apis.model.tax_rate_address_request import TaxRateAddressRequest
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | 
    tax_rate_address_request = TaxRateAddressRequest(
        preferences=LocalTaxPreferences(
            custom_preferences={
                "key": {},
            },
            default_buffer_width="default_buffer_width_example",
            distance_units="distance_units_example",
            fallback_to_geographic="fallback_to_geographic_example",
            lat_long_format="lat_long_format_example",
            lat_long_offset="lat_long_offset_example",
            match_mode="match_mode_example",
            output_casing="output_casing_example",
            return_census_fields="return_census_fields_example",
            return_lat_long_fields="return_lat_long_fields_example",
            squeeze="squeeze_example",
            tax_ratetype_id="tax_ratetype_id_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
        ),
        tax_rate_addresses=[
            TaxRateAddress(
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
                post_code1="post_code1_example",
                post_code_ext="post_code_ext_example",
                country="country_example",
                address_number="address_number_example",
                street_name="street_name_example",
                unit_type="unit_type_example",
                unit_value="unit_value_example",
                distance_units="distance_units_example",
                buffer_width="buffer_width_example",
                user_buffer_width="user_buffer_width_example",
            ),
        ],
    ) # TaxRateAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Taxrate By Address
        api_response = api_instance.get_batch_tax_rate_by_address(tax_rate_type_id, tax_rate_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_batch_tax_rate_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**|  |
 **tax_rate_address_request** | [**TaxRateAddressRequest**](TaxRateAddressRequest.md)|  |

### Return type

[**TaxResponses**](TaxResponses.md)

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

# **get_batch_tax_rate_by_location**
> TaxResponses get_batch_tax_rate_by_location(tax_rate_type_id, tax_rate_location_request)

Post Taxrate By Location

This is a Batch offering for 'Taxrate By Location' service. It accepts a single location coordinate or a list of location coordinates and retrieve applicable tax rates.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_responses import TaxResponses
from com.precisely.apis.model.tax_rate_location_request import TaxRateLocationRequest
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | 
    tax_rate_location_request = TaxRateLocationRequest(
        preferences=LocalTaxPreferences(
            custom_preferences={
                "key": {},
            },
            default_buffer_width="default_buffer_width_example",
            distance_units="distance_units_example",
            fallback_to_geographic="fallback_to_geographic_example",
            lat_long_format="lat_long_format_example",
            lat_long_offset="lat_long_offset_example",
            match_mode="match_mode_example",
            output_casing="output_casing_example",
            return_census_fields="return_census_fields_example",
            return_lat_long_fields="return_lat_long_fields_example",
            squeeze="squeeze_example",
            tax_ratetype_id="tax_ratetype_id_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
        ),
        locations=[
            TaxLocations(
                geometry=TaxGeometry(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                ),
                purchase_amount="purchase_amount_example",
                object_id="object_id_example",
            ),
        ],
    ) # TaxRateLocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Taxrate By Location
        api_response = api_instance.get_batch_tax_rate_by_location(tax_rate_type_id, tax_rate_location_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_batch_tax_rate_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**|  |
 **tax_rate_location_request** | [**TaxRateLocationRequest**](TaxRateLocationRequest.md)|  |

### Return type

[**TaxResponses**](TaxResponses.md)

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

# **get_ipd_tax_by_address**
> TaxDistrictResponse get_ipd_tax_by_address(address)

Get IPD Tax by Address

Retrieves IPD (Insurance Premium District) tax rates applicable to a specific address. This service accepts address as input and returns one or many IPD tax rate details for that region in which address falls.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.tax_district_response import TaxDistrictResponse
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    address = "address_example" # str | The address to be searched.
    return_lat_long_fields = "returnLatLongFields_example" # str | Y or N (default is N) - Returns Latitude Longitude Fields. (optional)
    lat_long_format = "latLongFormat_example" # str | (default is Decimal) - Returns Desired Latitude Longitude Format. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get IPD Tax by Address
        api_response = api_instance.get_ipd_tax_by_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_ipd_tax_by_address: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get IPD Tax by Address
        api_response = api_instance.get_ipd_tax_by_address(address, return_lat_long_fields=return_lat_long_fields, lat_long_format=lat_long_format)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_ipd_tax_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |
 **return_lat_long_fields** | **str**| Y or N (default is N) - Returns Latitude Longitude Fields. | [optional]
 **lat_long_format** | **str**| (default is Decimal) - Returns Desired Latitude Longitude Format. | [optional]

### Return type

[**TaxDistrictResponse**](TaxDistrictResponse.md)

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

# **get_ipd_tax_by_address_batch**
> TaxDistrictResponseList get_ipd_tax_by_address_batch(ipd_tax_by_address_batch_request)

Get IPD Tax for batch requests.

This is a Batch offering for 'IPD Tax rates By Address'. It accepts multiple addresses as parameters along with geocoding and matching preferences and returns one or many IPD tax rate details for each address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.ipd_tax_by_address_batch_request import IPDTaxByAddressBatchRequest
from com.precisely.apis.model.tax_district_response_list import TaxDistrictResponseList
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    ipd_tax_by_address_batch_request = IPDTaxByAddressBatchRequest(
        addresses=[
            TaxRateMatchedAddress(
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
                post_code1="post_code1_example",
                post_code_ext="post_code_ext_example",
                country="country_example",
                address_number="address_number_example",
                street_name="street_name_example",
                unit_type="unit_type_example",
                unit_value="unit_value_example",
            ),
        ],
        preferences=LocalTaxPreferences(
            custom_preferences={
                "key": {},
            },
            default_buffer_width="default_buffer_width_example",
            distance_units="distance_units_example",
            fallback_to_geographic="fallback_to_geographic_example",
            lat_long_format="lat_long_format_example",
            lat_long_offset="lat_long_offset_example",
            match_mode="match_mode_example",
            output_casing="output_casing_example",
            return_census_fields="return_census_fields_example",
            return_lat_long_fields="return_lat_long_fields_example",
            squeeze="squeeze_example",
            tax_ratetype_id="tax_ratetype_id_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
        ),
    ) # IPDTaxByAddressBatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get IPD Tax for batch requests.
        api_response = api_instance.get_ipd_tax_by_address_batch(ipd_tax_by_address_batch_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_ipd_tax_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipd_tax_by_address_batch_request** | [**IPDTaxByAddressBatchRequest**](IPDTaxByAddressBatchRequest.md)|  |

### Return type

[**TaxDistrictResponseList**](TaxDistrictResponseList.md)

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

# **get_specific_tax_by_address**
> TaxRateResponse get_specific_tax_by_address(tax_rate_type_id, address, purchase_amount)

Get Tax By Address

This service calculates and returns taxes applicable at a specific address. Address, purchase amount and supported tax rate type are inputs to the service.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_rate_response import TaxRateResponse
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | The tax rate id
    address = "address_example" # str | The address to be searched.
    purchase_amount = "purchaseAmount_example" # str | The amount on which tax to be calculated

    # example passing only required values which don't have defaults set
    try:
        # Get Tax By Address
        api_response = api_instance.get_specific_tax_by_address(tax_rate_type_id, address, purchase_amount)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_specific_tax_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**| The tax rate id |
 **address** | **str**| The address to be searched. |
 **purchase_amount** | **str**| The amount on which tax to be calculated |

### Return type

[**TaxRateResponse**](TaxRateResponse.md)

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

# **get_specific_tax_by_location**
> TaxRateResponse get_specific_tax_by_location(tax_rate_type_id, latitude, longitude, purchase_amount)

Get Tax By Location

This service calculates and returns tax applicable at a specific location. Longitude, latitude, purchase amount and supported tax rate type are inputs to the service.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_rate_response import TaxRateResponse
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | The tax rate id
    latitude = "latitude_example" # str | Latitude of the location
    longitude = "longitude_example" # str | Longitude of the location
    purchase_amount = "purchaseAmount_example" # str | The amount on which tax to be calculated

    # example passing only required values which don't have defaults set
    try:
        # Get Tax By Location
        api_response = api_instance.get_specific_tax_by_location(tax_rate_type_id, latitude, longitude, purchase_amount)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_specific_tax_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**| The tax rate id |
 **latitude** | **str**| Latitude of the location |
 **longitude** | **str**| Longitude of the location |
 **purchase_amount** | **str**| The amount on which tax to be calculated |

### Return type

[**TaxRateResponse**](TaxRateResponse.md)

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

# **get_specific_tax_rate_by_address**
> TaxRateResponse get_specific_tax_rate_by_address(tax_rate_type_id, address)

Get Taxrate By Address

Retrieves tax rates applicable to a specific address. This service accepts address and supported tax rate type as inputs to retrieve applicable tax rates.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_rate_response import TaxRateResponse
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | The tax rate id
    address = "address_example" # str | The address to be searched.

    # example passing only required values which don't have defaults set
    try:
        # Get Taxrate By Address
        api_response = api_instance.get_specific_tax_rate_by_address(tax_rate_type_id, address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_specific_tax_rate_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**| The tax rate id |
 **address** | **str**| The address to be searched. |

### Return type

[**TaxRateResponse**](TaxRateResponse.md)

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

# **get_specific_tax_rate_by_location**
> TaxRateResponse get_specific_tax_rate_by_location(tax_rate_type_id, latitude, longitude)

Get Taxrate By Location

Retrieves tax rates applicable to a specific location. This service accepts longitude, latitude and supported tax rate type as inputs to retrieve applicable tax rates.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import local_tax_service_api
from com.precisely.apis.model.tax_rate_response import TaxRateResponse
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
    api_instance = local_tax_service_api.LocalTaxServiceApi(api_client)
    tax_rate_type_id = "taxRateTypeId_example" # str | The tax rate id
    latitude = "latitude_example" # str | Latitude of the location
    longitude = "longitude_example" # str | Longitude of the location

    # example passing only required values which don't have defaults set
    try:
        # Get Taxrate By Location
        api_response = api_instance.get_specific_tax_rate_by_location(tax_rate_type_id, latitude, longitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling LocalTaxServiceApi->get_specific_tax_rate_by_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_type_id** | **str**| The tax rate id |
 **latitude** | **str**| Latitude of the location |
 **longitude** | **str**| Longitude of the location |

### Return type

[**TaxRateResponse**](TaxRateResponse.md)

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

