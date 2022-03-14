# com.precisely.apis.GeocodeServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geocode**](GeocodeServiceApi.md#geocode) | **GET** /geocode/v1/{datapackBundle}/geocode | Get Forward Geocode(Basic/Premium/Advanced)
[**geocode_batch**](GeocodeServiceApi.md#geocode_batch) | **POST** /geocode/v1/{datapackBundle}/geocode | Post Forward Geocode
[**get_pb_key**](GeocodeServiceApi.md#get_pb_key) | **GET** /geocode/v1/key/byaddress | Get PreciselyID By Address
[**get_pb_keys**](GeocodeServiceApi.md#get_pb_keys) | **POST** /geocode/v1/key/byaddress | Post PreciselyID By Address
[**key_lookup**](GeocodeServiceApi.md#key_lookup) | **GET** /geocode/v1/keylookup | Get Key Lookup
[**key_lookup_batch**](GeocodeServiceApi.md#key_lookup_batch) | **POST** /geocode/v1/keylookup | Post Key Lookup
[**reverse_geocod_batch**](GeocodeServiceApi.md#reverse_geocod_batch) | **POST** /geocode/v1/{datapackBundle}/reverseGeocode | Post Reverse Geocode
[**reverse_geocode**](GeocodeServiceApi.md#reverse_geocode) | **GET** /geocode/v1/{datapackBundle}/reverseGeocode | Get Reverse Geocode(Basic/Premium/Advanced)


# **geocode**
> GeocodeServiceResponse geocode(datapack_bundle)

Get Forward Geocode(Basic/Premium/Advanced)

This service accepts an address and returns the location coordinates corresponding to that address. Premium offers the best accuracy and is a high precision geocoder leveraging Master Location Data - geocodes to Street or building level. Advanced offers advanced accuracy and geocodes to Street level.Basic offering will geocode to a Place or Postal level. Good accuracy.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.geocode_service_response import GeocodeServiceResponse
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    datapack_bundle = "premium" # str | datapackBundle
    country = "USA" # str | Country name or ISO code. (optional) if omitted the server will use the default value of "USA"
    main_address = "4750 Walnut St., Boulder CO, 80301" # str | Single line input, treated as collection of field elements. (optional) if omitted the server will use the default value of "4750 Walnut St., Boulder CO, 80301"
    match_mode = "Standard" # str | Match modes determine the leniency used to make a match between the input address and the reference data. (optional) if omitted the server will use the default value of "Standard"
    fallback_geo = "true" # str | Specifies whether to attempt to determine a geographic region centroid when an address-level geocode cannot be determined. (optional) if omitted the server will use the default value of "true"
    fallback_postal = "true" # str | Specifies whether to attempt to determine a post code centroid when an address-level geocode cannot be determined. (optional) if omitted the server will use the default value of "true"
    max_cands = "1" # str | The maximum number of candidates to return. (optional) if omitted the server will use the default value of "1"
    street_offset = "7" # str | Indicates the offset distance from the street segments to use in street-level geocoding. (optional) if omitted the server will use the default value of "7"
    street_offset_units = "METERS" # str | Specifies the unit of measurement for the street offset. (optional) if omitted the server will use the default value of "METERS"
    corner_offset = "7" # str | Specifies the distance to offset the street end points in street-level matching. (optional) if omitted the server will use the default value of "7"
    corner_offset_units = "METERS" # str | Specifies the unit of measurement for the corner offset. (optional) if omitted the server will use the default value of "METERS"
    remove_accent_marks = "false" # str | Specifies whether to Suppress accents and other diacritical marks. (optional) if omitted the server will use the default value of "false"

    # example passing only required values which don't have defaults set
    try:
        # Get Forward Geocode(Basic/Premium/Advanced)
        api_response = api_instance.geocode(datapack_bundle)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->geocode: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Forward Geocode(Basic/Premium/Advanced)
        api_response = api_instance.geocode(datapack_bundle, country=country, main_address=main_address, match_mode=match_mode, fallback_geo=fallback_geo, fallback_postal=fallback_postal, max_cands=max_cands, street_offset=street_offset, street_offset_units=street_offset_units, corner_offset=corner_offset, corner_offset_units=corner_offset_units, remove_accent_marks=remove_accent_marks)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->geocode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapack_bundle** | **str**| datapackBundle |
 **country** | **str**| Country name or ISO code. | [optional] if omitted the server will use the default value of "USA"
 **main_address** | **str**| Single line input, treated as collection of field elements. | [optional] if omitted the server will use the default value of "4750 Walnut St., Boulder CO, 80301"
 **match_mode** | **str**| Match modes determine the leniency used to make a match between the input address and the reference data. | [optional] if omitted the server will use the default value of "Standard"
 **fallback_geo** | **str**| Specifies whether to attempt to determine a geographic region centroid when an address-level geocode cannot be determined. | [optional] if omitted the server will use the default value of "true"
 **fallback_postal** | **str**| Specifies whether to attempt to determine a post code centroid when an address-level geocode cannot be determined. | [optional] if omitted the server will use the default value of "true"
 **max_cands** | **str**| The maximum number of candidates to return. | [optional] if omitted the server will use the default value of "1"
 **street_offset** | **str**| Indicates the offset distance from the street segments to use in street-level geocoding. | [optional] if omitted the server will use the default value of "7"
 **street_offset_units** | **str**| Specifies the unit of measurement for the street offset. | [optional] if omitted the server will use the default value of "METERS"
 **corner_offset** | **str**| Specifies the distance to offset the street end points in street-level matching. | [optional] if omitted the server will use the default value of "7"
 **corner_offset_units** | **str**| Specifies the unit of measurement for the corner offset. | [optional] if omitted the server will use the default value of "METERS"
 **remove_accent_marks** | **str**| Specifies whether to Suppress accents and other diacritical marks. | [optional] if omitted the server will use the default value of "false"

### Return type

[**GeocodeServiceResponse**](GeocodeServiceResponse.md)

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

# **geocode_batch**
> GeocodeServiceResponseList geocode_batch(datapack_bundle, geocode_request)

Post Forward Geocode

This is a Batch offering for geocode service. It accepts a single address or a list of addresses and returns location coordinates

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.geocode_request import GeocodeRequest
from com.precisely.apis.model.geocode_service_response_list import GeocodeServiceResponseList
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    datapack_bundle = "datapackBundle_example" # str | 
    geocode_request = GeocodeRequest(
        type="type_example",
        preferences=GeocodePreferences(
            return_all_candidate_info=True,
            fallback_to_geographic="fallback_to_geographic_example",
            fallback_to_postal="fallback_to_postal_example",
            max_returned_candidates="max_returned_candidates_example",
            distance="distance_example",
            street_offset="street_offset_example",
            corner_offset="corner_offset_example",
            match_mode="match_mode_example",
            client_locale="client_locale_example",
            client_coord_sys_name="client_coord_sys_name_example",
            distance_units="distance_units_example",
            street_offset_units="street_offset_units_example",
            corner_offset_units="corner_offset_units_example",
            must_match_fields=FieldsMatching(
                match_on_address_number=True,
                match_on_post_code1=True,
                match_on_post_code2=True,
                match_on_area_name1=True,
                match_on_area_name2=True,
                match_on_area_name3=True,
                match_on_area_name4=True,
                match_on_all_street_fields=True,
                match_on_street_name=True,
                match_on_street_type=True,
                match_on_street_directional=True,
                match_on_place_name=True,
                match_on_input_fields=True,
            ),
            return_fields_descriptor=ReturnFieldsDescriptor(
                return_all_custom_fields=True,
                return_match_descriptor=True,
                return_street_address_fields=True,
                return_unit_information=True,
                returned_custom_field_keys=[
                    "returned_custom_field_keys_example",
                ],
            ),
            output_record_type="output_record_type_example",
            custom_preferences={
                "key": {},
            },
            preferred_dictionary_orders=[
                "preferred_dictionary_orders_example",
            ],
            output_casing="output_casing_example",
            lat_long_offset="lat_long_offset_example",
            squeeze="squeeze_example",
            return_lat_long_fields="return_lat_long_fields_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
            lat_long_format="lat_long_format_example",
            default_buffer_width="default_buffer_width_example",
            return_census_fields="return_census_fields_example",
        ),
        addresses=[
            GeocodeAddress(
                object_id="object_id_example",
                main_address_line="main_address_line_example",
                address_last_line="address_last_line_example",
                place_name="place_name_example",
                area_name1="area_name1_example",
                area_name2="area_name2_example",
                area_name3="area_name3_example",
                area_name4="area_name4_example",
                post_code1="post_code1_example",
                post_code2="post_code2_example",
                country="country_example",
                address_number="address_number_example",
                street_name="street_name_example",
                unit_type="unit_type_example",
                unit_value="unit_value_example",
                custom_fields={
                    "key": {},
                },
            ),
        ],
    ) # GeocodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Forward Geocode
        api_response = api_instance.geocode_batch(datapack_bundle, geocode_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->geocode_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapack_bundle** | **str**|  |
 **geocode_request** | [**GeocodeRequest**](GeocodeRequest.md)|  |

### Return type

[**GeocodeServiceResponseList**](GeocodeServiceResponseList.md)

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

# **get_pb_key**
> PBKeyResponse get_pb_key(address)

Get PreciselyID By Address

This service accepts an address and returns the corresponding PreciselyID

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.pb_key_response import PBKeyResponse
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    address = "address_example" # str | The address to be searched.
    country = "country_example" # str | 3 letter ISO code of the country to be searched. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get PreciselyID By Address
        api_response = api_instance.get_pb_key(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->get_pb_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get PreciselyID By Address
        api_response = api_instance.get_pb_key(address, country=country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->get_pb_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |
 **country** | **str**| 3 letter ISO code of the country to be searched. | [optional]

### Return type

[**PBKeyResponse**](PBKeyResponse.md)

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

# **get_pb_keys**
> PBKeyResponseList get_pb_keys(pb_key_address_request)

Post PreciselyID By Address

This is a Batch offering for 'PreciselyID By Address' service. It accepts a single address or a list of addresses and returns the corresponding PreciselyID.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.pb_key_response_list import PBKeyResponseList
from com.precisely.apis.model.pb_key_address_request import PBKeyAddressRequest
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    pb_key_address_request = PBKeyAddressRequest(
        addresses=[
            GeocodeAddress(
                object_id="object_id_example",
                main_address_line="main_address_line_example",
                address_last_line="address_last_line_example",
                place_name="place_name_example",
                area_name1="area_name1_example",
                area_name2="area_name2_example",
                area_name3="area_name3_example",
                area_name4="area_name4_example",
                post_code1="post_code1_example",
                post_code2="post_code2_example",
                country="country_example",
                address_number="address_number_example",
                street_name="street_name_example",
                unit_type="unit_type_example",
                unit_value="unit_value_example",
                custom_fields={
                    "key": {},
                },
            ),
        ],
    ) # PBKeyAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post PreciselyID By Address
        api_response = api_instance.get_pb_keys(pb_key_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->get_pb_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pb_key_address_request** | [**PBKeyAddressRequest**](PBKeyAddressRequest.md)|  |

### Return type

[**PBKeyResponseList**](PBKeyResponseList.md)

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

# **key_lookup**
> GeocodeServiceResponse key_lookup(key, type)

Get Key Lookup

This service accepts a PreciselyID and returns the corresponding address associated with that PreciselyID.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.geocode_service_response import GeocodeServiceResponse
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    key = "key_example" # str | PreciselyID which maps to a unique address.
    type = "type_example" # str | Specifies the key type - PreciselyID and GNAF_PID for Aus.
    country = "country_example" # str | 3 letter ISO code of the country to be searched. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Key Lookup
        api_response = api_instance.key_lookup(key, type)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->key_lookup: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Key Lookup
        api_response = api_instance.key_lookup(key, type, country=country)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->key_lookup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| PreciselyID which maps to a unique address. |
 **type** | **str**| Specifies the key type - PreciselyID and GNAF_PID for Aus. |
 **country** | **str**| 3 letter ISO code of the country to be searched. | [optional]

### Return type

[**GeocodeServiceResponse**](GeocodeServiceResponse.md)

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

# **key_lookup_batch**
> GeocodeServiceResponseList key_lookup_batch(key_lookup_request)

Post Key Lookup

This service accepts batches of PreciselyID's and returns the corresponding address associated with those PreciselyID's.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.key_lookup_request import KeyLookupRequest
from com.precisely.apis.model.geocode_service_response_list import GeocodeServiceResponseList
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    key_lookup_request = KeyLookupRequest(
        type="type_example",
        preferences=GeocodePreferences(
            return_all_candidate_info=True,
            fallback_to_geographic="fallback_to_geographic_example",
            fallback_to_postal="fallback_to_postal_example",
            max_returned_candidates="max_returned_candidates_example",
            distance="distance_example",
            street_offset="street_offset_example",
            corner_offset="corner_offset_example",
            match_mode="match_mode_example",
            client_locale="client_locale_example",
            client_coord_sys_name="client_coord_sys_name_example",
            distance_units="distance_units_example",
            street_offset_units="street_offset_units_example",
            corner_offset_units="corner_offset_units_example",
            must_match_fields=FieldsMatching(
                match_on_address_number=True,
                match_on_post_code1=True,
                match_on_post_code2=True,
                match_on_area_name1=True,
                match_on_area_name2=True,
                match_on_area_name3=True,
                match_on_area_name4=True,
                match_on_all_street_fields=True,
                match_on_street_name=True,
                match_on_street_type=True,
                match_on_street_directional=True,
                match_on_place_name=True,
                match_on_input_fields=True,
            ),
            return_fields_descriptor=ReturnFieldsDescriptor(
                return_all_custom_fields=True,
                return_match_descriptor=True,
                return_street_address_fields=True,
                return_unit_information=True,
                returned_custom_field_keys=[
                    "returned_custom_field_keys_example",
                ],
            ),
            output_record_type="output_record_type_example",
            custom_preferences={
                "key": {},
            },
            preferred_dictionary_orders=[
                "preferred_dictionary_orders_example",
            ],
            output_casing="output_casing_example",
            lat_long_offset="lat_long_offset_example",
            squeeze="squeeze_example",
            return_lat_long_fields="return_lat_long_fields_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
            lat_long_format="lat_long_format_example",
            default_buffer_width="default_buffer_width_example",
            return_census_fields="return_census_fields_example",
        ),
        keys=[
            Keys(
                object_id="object_id_example",
                country="country_example",
                value="value_example",
            ),
        ],
    ) # KeyLookupRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Key Lookup
        api_response = api_instance.key_lookup_batch(key_lookup_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->key_lookup_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_lookup_request** | [**KeyLookupRequest**](KeyLookupRequest.md)|  |

### Return type

[**GeocodeServiceResponseList**](GeocodeServiceResponseList.md)

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

# **reverse_geocod_batch**
> GeocodeServiceResponseList reverse_geocod_batch(datapack_bundle, reverse_geocode_request)

Post Reverse Geocode

This is a Batch offering for geocode service. It accepts a single address or a list of addresses and returns location coordinates

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.geocode_service_response_list import GeocodeServiceResponseList
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.reverse_geocode_request import ReverseGeocodeRequest
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    datapack_bundle = "datapackBundle_example" # str | 
    reverse_geocode_request = ReverseGeocodeRequest(
        preferences=GeocodePreferences(
            return_all_candidate_info=True,
            fallback_to_geographic="fallback_to_geographic_example",
            fallback_to_postal="fallback_to_postal_example",
            max_returned_candidates="max_returned_candidates_example",
            distance="distance_example",
            street_offset="street_offset_example",
            corner_offset="corner_offset_example",
            match_mode="match_mode_example",
            client_locale="client_locale_example",
            client_coord_sys_name="client_coord_sys_name_example",
            distance_units="distance_units_example",
            street_offset_units="street_offset_units_example",
            corner_offset_units="corner_offset_units_example",
            must_match_fields=FieldsMatching(
                match_on_address_number=True,
                match_on_post_code1=True,
                match_on_post_code2=True,
                match_on_area_name1=True,
                match_on_area_name2=True,
                match_on_area_name3=True,
                match_on_area_name4=True,
                match_on_all_street_fields=True,
                match_on_street_name=True,
                match_on_street_type=True,
                match_on_street_directional=True,
                match_on_place_name=True,
                match_on_input_fields=True,
            ),
            return_fields_descriptor=ReturnFieldsDescriptor(
                return_all_custom_fields=True,
                return_match_descriptor=True,
                return_street_address_fields=True,
                return_unit_information=True,
                returned_custom_field_keys=[
                    "returned_custom_field_keys_example",
                ],
            ),
            output_record_type="output_record_type_example",
            custom_preferences={
                "key": {},
            },
            preferred_dictionary_orders=[
                "preferred_dictionary_orders_example",
            ],
            output_casing="output_casing_example",
            lat_long_offset="lat_long_offset_example",
            squeeze="squeeze_example",
            return_lat_long_fields="return_lat_long_fields_example",
            use_geo_tax_auxiliary_file="use_geo_tax_auxiliary_file_example",
            lat_long_format="lat_long_format_example",
            default_buffer_width="default_buffer_width_example",
            return_census_fields="return_census_fields_example",
        ),
        points=[
            Points(
                object_id="object_id_example",
                country="country_example",
                geometry=GeoPos(
                    type="type_example",
                    coordinates=[
                        3.14,
                    ],
                    crs=Crs(
                        type="type_example",
                        properties=Properties(
                            name="name_example",
                        ),
                    ),
                ),
            ),
        ],
    ) # ReverseGeocodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Post Reverse Geocode
        api_response = api_instance.reverse_geocod_batch(datapack_bundle, reverse_geocode_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->reverse_geocod_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapack_bundle** | **str**|  |
 **reverse_geocode_request** | [**ReverseGeocodeRequest**](ReverseGeocodeRequest.md)|  |

### Return type

[**GeocodeServiceResponseList**](GeocodeServiceResponseList.md)

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

# **reverse_geocode**
> GeocodeServiceResponse reverse_geocode(datapack_bundle, )

Get Reverse Geocode(Basic/Premium/Advanced)

This service accepts location coordinate and returns an address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import geocode_service_api
from com.precisely.apis.model.geocode_service_response import GeocodeServiceResponse
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
    api_instance = geocode_service_api.GeocodeServiceApi(api_client)
    datapack_bundle = "premium" # str | datapackBundle
    country = "country_example" # str | Country name or ISO code. (optional)
    coord_sys_name = "EPSG:4326" # str | Coordinate system to convert geometry to in format codespace:code. (optional) if omitted the server will use the default value of "EPSG:4326"
    distance = "Radius in which search is performed." # str | Radius in which search is performed. (optional) if omitted the server will use the default value of "Radius in which search is performed."
    distance_units = "METERS" # str | Unit of measurement. (optional) if omitted the server will use the default value of "METERS"

    # example passing only required values which don't have defaults set
    try:
        # Get Reverse Geocode(Basic/Premium/Advanced)
        api_response = api_instance.reverse_geocode(datapack_bundle, )
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->reverse_geocode: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Reverse Geocode(Basic/Premium/Advanced)
        api_response = api_instance.reverse_geocode(datapack_bundle, country=country, coord_sys_name=coord_sys_name, distance=distance, distance_units=distance_units)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling GeocodeServiceApi->reverse_geocode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datapack_bundle** | **str**| datapackBundle |
 **x** | **str**| Longitude of the location. | defaults to "-105.240976"
 **y** | **str**| Latitude of the location. | defaults to "40.018301"
 **country** | **str**| Country name or ISO code. | [optional]
 **coord_sys_name** | **str**| Coordinate system to convert geometry to in format codespace:code. | [optional] if omitted the server will use the default value of "EPSG:4326"
 **distance** | **str**| Radius in which search is performed. | [optional] if omitted the server will use the default value of "Radius in which search is performed."
 **distance_units** | **str**| Unit of measurement. | [optional] if omitted the server will use the default value of "METERS"

### Return type

[**GeocodeServiceResponse**](GeocodeServiceResponse.md)

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

