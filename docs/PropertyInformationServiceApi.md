# com.precisely.apis.PropertyInformationServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_property_attributes_by_address**](PropertyInformationServiceApi.md#get_property_attributes_by_address) | **GET** /property/v2/attributes/byaddress | PropertyV2 Attributes By Address.
[**get_property_attributes_by_address_batch**](PropertyInformationServiceApi.md#get_property_attributes_by_address_batch) | **POST** /property/v2/attributes/byaddress | PropertyV2 Attributes By Address Batch.


# **get_property_attributes_by_address**
> PropertyInfoResponse get_property_attributes_by_address()

PropertyV2 Attributes By Address.

GetPropertyAttributesbyAddress Endpoint will take address as an input and will return key property attributes in response. Optionally user will have the option to filter the attributes and will pay for only returned attributes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import property_information_service_api
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.property_info_response import PropertyInfoResponse
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
    api_instance = property_information_service_api.PropertyInformationServiceApi(api_client)
    address = "address_example" # str | free form address text (optional)
    attributes = "attributes_example" # str | Case-insensitive comma separated values of property attributes. Response will contain only the input attributes. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PropertyV2 Attributes By Address.
        api_response = api_instance.get_property_attributes_by_address(address=address, attributes=attributes)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PropertyInformationServiceApi->get_property_attributes_by_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| free form address text | [optional]
 **attributes** | **str**| Case-insensitive comma separated values of property attributes. Response will contain only the input attributes. | [optional]

### Return type

[**PropertyInfoResponse**](PropertyInfoResponse.md)

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

# **get_property_attributes_by_address_batch**
> PropertyInfoResponses get_property_attributes_by_address_batch(property_info_address_request)

PropertyV2 Attributes By Address Batch.

GetPropertyAttributesbyAddressBatch Endpoint will take the list of addresses as an input and will return key property attributes for the given addresses in response. Optionally user will have the option to filter the attributes and will pay for only returned attributes.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import property_information_service_api
from com.precisely.apis.model.property_info_address_request import PropertyInfoAddressRequest
from com.precisely.apis.model.property_info_responses import PropertyInfoResponses
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
    api_instance = property_information_service_api.PropertyInformationServiceApi(api_client)
    property_info_address_request = PropertyInfoAddressRequest(
        preferences=PropertyInfoPreferences(
            attributes="attributes_example",
        ),
        addresses=[
            MatchedAddress(
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
    ) # PropertyInfoAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # PropertyV2 Attributes By Address Batch.
        api_response = api_instance.get_property_attributes_by_address_batch(property_info_address_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PropertyInformationServiceApi->get_property_attributes_by_address_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_info_address_request** | [**PropertyInfoAddressRequest**](PropertyInfoAddressRequest.md)|  |

### Return type

[**PropertyInfoResponses**](PropertyInfoResponses.md)

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

