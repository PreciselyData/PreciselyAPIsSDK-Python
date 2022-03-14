# com.precisely.apis.AddressVerificationServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_city_state_province**](AddressVerificationServiceApi.md#get_city_state_province) | **POST** /addressverification/v1/getcitystateprovince/results.json | GetCityStateProvince
[**get_postal_codes**](AddressVerificationServiceApi.md#get_postal_codes) | **POST** /addressverification/v1/getpostalcodes/results.json | GetPostalCodes
[**validate_mailing_address**](AddressVerificationServiceApi.md#validate_mailing_address) | **POST** /addressverification/v1/validatemailingaddress/results.json | ValidateMailingAddress
[**validate_mailing_address_premium**](AddressVerificationServiceApi.md#validate_mailing_address_premium) | **POST** /addressverification/v1/validatemailingaddresspremium/results.json | ValidateMailingAddressPremium
[**validate_mailing_address_pro**](AddressVerificationServiceApi.md#validate_mailing_address_pro) | **POST** /addressverification/v1/validatemailingaddresspro/results.json | ValidateMailingAddressPro
[**validate_mailing_address_uscan**](AddressVerificationServiceApi.md#validate_mailing_address_uscan) | **POST** /addressverification/v1/validatemailingaddressuscan/results.json | ValidateMailingAddressUSCAN


# **get_city_state_province**
> GetCityStateProvinceAPIResponse get_city_state_province(input_address)

GetCityStateProvince

GetCityStateProvince returns a city and state/province for a given input postal code for U.S. and Canadian addresses.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.get_city_state_province_api_response import GetCityStateProvinceAPIResponse
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.get_city_state_province_api_request import GetCityStateProvinceAPIRequest
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = GetCityStateProvinceAPIRequest(
        options=GetCityStateProvinceAPIOptions(
            output_vanity_city="N",
            perform_canadian_processing="Y",
            maximum_results="10",
            perform_us_processing="Y",
        ),
        input=GetCityStateProvinceAPIInput(
            row=[
                GetCityStateProvinceAPIInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    postal_code="postal_code_example",
                ),
            ],
        ),
    ) # GetCityStateProvinceAPIRequest | 

    # example passing only required values which don't have defaults set
    try:
        # GetCityStateProvince
        api_response = api_instance.get_city_state_province(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->get_city_state_province: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**GetCityStateProvinceAPIRequest**](GetCityStateProvinceAPIRequest.md)|  |

### Return type

[**GetCityStateProvinceAPIResponse**](GetCityStateProvinceAPIResponse.md)

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

# **get_postal_codes**
> GetPostalCodesAPIResponse get_postal_codes(input_address)

GetPostalCodes

GetPostalCodes takes a city and state as input for U.S. addresses and returns the postal codes for that city.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.get_postal_codes_api_response import GetPostalCodesAPIResponse
from com.precisely.apis.model.get_postal_codes_api_request import GetPostalCodesAPIRequest
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = GetPostalCodesAPIRequest(
        options=GetPostalCodesAPIOptions(
            output_city_type="N",
            output_vanity_city="N",
        ),
        input=GetPostalCodesAPIInput(
            row=[
                GetPostalCodesAPIInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    city="city_example",
                    state_province="state_province_example",
                ),
            ],
        ),
    ) # GetPostalCodesAPIRequest | 

    # example passing only required values which don't have defaults set
    try:
        # GetPostalCodes
        api_response = api_instance.get_postal_codes(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->get_postal_codes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**GetPostalCodesAPIRequest**](GetPostalCodesAPIRequest.md)|  |

### Return type

[**GetPostalCodesAPIResponse**](GetPostalCodesAPIResponse.md)

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

# **validate_mailing_address**
> ValidateMailingAddressResponse validate_mailing_address(input_address)

ValidateMailingAddress

ValidateMailingAddress analyses and compares the input addresses against the known address databases around the world to output a standardized detail.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.validate_mailing_address_response import ValidateMailingAddressResponse
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.validate_mailing_address_request import ValidateMailingAddressRequest
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = ValidateMailingAddressRequest(
        options=ValidateMailingAddressOptions(
            output_casing="M",
        ),
        input=ValidateMailingAddressInput(
            row=[
                ValidateMailingAddressInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    address_line1="address_line1_example",
                    address_line2="address_line2_example",
                    firm_name="firm_name_example",
                    city="city_example",
                    state_province="state_province_example",
                    country="country_example",
                    postal_code="postal_code_example",
                ),
            ],
        ),
    ) # ValidateMailingAddressRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ValidateMailingAddress
        api_response = api_instance.validate_mailing_address(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->validate_mailing_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**ValidateMailingAddressRequest**](ValidateMailingAddressRequest.md)|  |

### Return type

[**ValidateMailingAddressResponse**](ValidateMailingAddressResponse.md)

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

# **validate_mailing_address_premium**
> ValidateMailingAddressPremiumResponse validate_mailing_address_premium(input_address)

ValidateMailingAddressPremium

ValidateMailing AddressPremium expands on the ValidateMailingAddressPro service by adding premium address data sources to get the best address validation result possible.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.validate_mailing_address_premium_response import ValidateMailingAddressPremiumResponse
from com.precisely.apis.model.validate_mailing_address_premium_request import ValidateMailingAddressPremiumRequest
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = ValidateMailingAddressPremiumRequest(
        options=ValidateMailingAddressPremiumOptions(
            output_address_blocks="Y",
            keep_multimatch="N",
            output_country_format="E",
            output_record_type="A",
            output_field_level_return_codes="N",
            output_script="InputScript",
            output_casing="M",
            maximum_results="10",
        ),
        input=ValidateMailingAddressPremiumInput(
            row=[
                ValidateMailingAddressPremiumInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    address_line1="address_line1_example",
                    address_line2="address_line2_example",
                    address_line3="address_line3_example",
                    address_line4="address_line4_example",
                    address_line5="address_line5_example",
                    firm_name="firm_name_example",
                    city="city_example",
                    state_province="state_province_example",
                    country="country_example",
                    postal_code="postal_code_example",
                ),
            ],
        ),
    ) # ValidateMailingAddressPremiumRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ValidateMailingAddressPremium
        api_response = api_instance.validate_mailing_address_premium(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->validate_mailing_address_premium: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**ValidateMailingAddressPremiumRequest**](ValidateMailingAddressPremiumRequest.md)|  |

### Return type

[**ValidateMailingAddressPremiumResponse**](ValidateMailingAddressPremiumResponse.md)

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

# **validate_mailing_address_pro**
> ValidateMailingAddressProResponse validate_mailing_address_pro(input_address)

ValidateMailingAddressPro

ValidateMailingAddressPro builds upon the ValidateMailingAddress service by using additional address databases so it can provide enhanced detail.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.validate_mailing_address_pro_response import ValidateMailingAddressProResponse
from com.precisely.apis.model.validate_mailing_address_pro_request import ValidateMailingAddressProRequest
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = ValidateMailingAddressProRequest(
        options=ValidateMailingAddressProOptions(
            output_address_blocks="Y",
            keep_multimatch="N",
            output_country_format="E",
            output_script="InputScript",
            output_casing="M",
            maximum_results="10",
        ),
        input=ValidateMailingAddressProInput(
            row=[
                ValidateMailingAddressProInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    address_line1="address_line1_example",
                    address_line2="address_line2_example",
                    firm_name="firm_name_example",
                    city="city_example",
                    state_province="state_province_example",
                    country="country_example",
                    postal_code="postal_code_example",
                ),
            ],
        ),
    ) # ValidateMailingAddressProRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ValidateMailingAddressPro
        api_response = api_instance.validate_mailing_address_pro(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->validate_mailing_address_pro: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**ValidateMailingAddressProRequest**](ValidateMailingAddressProRequest.md)|  |

### Return type

[**ValidateMailingAddressProResponse**](ValidateMailingAddressProResponse.md)

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

# **validate_mailing_address_uscan**
> ValidateMailingAddressUSCANAPIResponse validate_mailing_address_uscan(input_address)

ValidateMailingAddressUSCAN

ValidateMailingAddressUSCAN analyses and compares the input addresses against the known address databases around the world to output a standardized detail for US and CANADAIt gives RDI and DPV also along with other US/CAN specific functionalities.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import address_verification_service_api
from com.precisely.apis.model.validate_mailing_address_uscanapi_request import ValidateMailingAddressUSCANAPIRequest
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.validate_mailing_address_uscanapi_response import ValidateMailingAddressUSCANAPIResponse
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
    api_instance = address_verification_service_api.AddressVerificationServiceApi(api_client)
    input_address = ValidateMailingAddressUSCANAPIRequest(
        options=ValidateMailingAddressUSCANAPIOptions(
            output_address_blocks="Y",
            perform_us_processing="Y",
            perform_dpv="N",
            output_formatted_on_fail="N",
            output_postal_code_separator="Y",
            output_country_format="E",
            keep_multimatch="N",
            output_casing="M",
            maximum_results="10",
            output_record_type="A",
            output_field_level_return_codes="N",
            dpv_determine_no_stat="N",
            street_matching_strictness="M",
            can_french_apartment_label="Appartement",
            output_abbreviated_alias="N",
            dpv_successful_status_condition="A",
            standard_address_pmb_line="N",
            firm_matching_strictness="M",
            can_rural_route_format="A",
            can_prefer_house_num="N",
            output_preferred_alias="N",
            directional_matching_strictness="M",
            extract_firm="N",
            fail_on_cmra_match="N",
            can_non_civic_format="A",
            can_sslvr_flg="N",
            output_street_name_alias="Y",
            perform_ews="N",
            can_output_city_format="D",
            dual_address_logic="N",
            perform_suite_link="N",
            can_standard_address_format="D",
            output_preferred_city="Z",
            output_multinational_characters="N",
            can_delivery_office_format="I",
            perform_lacs_link="Y",
            can_dual_address_logic="D",
            extract_urb="N",
            standard_address_format="C",
            can_french_format="C",
            dpv_determine_vacancy="N",
            can_english_apartment_label="Apt",
            suppress_zplus_phantom_carrier_r777="N",
            can_output_city_alias="N",
            output_short_city_name="N",
        ),
        input=ValidateMailingAddressUSCANAPIInput(
            row=[
                ValidateMailingAddressUSCANAPIInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    address_line1="address_line1_example",
                    address_line2="address_line2_example",
                    address_line3="address_line3_example",
                    address_line4="address_line4_example",
                    firm_name="firm_name_example",
                    city="city_example",
                    state_province="state_province_example",
                    country="country_example",
                    postal_code="postal_code_example",
                    us_urban_name="us_urban_name_example",
                    can_language="can_language_example",
                ),
            ],
        ),
    ) # ValidateMailingAddressUSCANAPIRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ValidateMailingAddressUSCAN
        api_response = api_instance.validate_mailing_address_uscan(input_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling AddressVerificationServiceApi->validate_mailing_address_uscan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_address** | [**ValidateMailingAddressUSCANAPIRequest**](ValidateMailingAddressUSCANAPIRequest.md)|  |

### Return type

[**ValidateMailingAddressUSCANAPIResponse**](ValidateMailingAddressUSCANAPIResponse.md)

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

