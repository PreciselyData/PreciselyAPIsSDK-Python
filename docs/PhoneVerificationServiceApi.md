# com.precisely.apis.PhoneVerificationServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validatephonenumber**](PhoneVerificationServiceApi.md#validatephonenumber) | **POST** /phoneverification/v2/validatephonenumber/results.json | Phone verification.


# **validatephonenumber**
> PhoneVerification validatephonenumber(validate_phone_number_api_request)

Phone verification.

This service accepts a phone number as input and returns details distinguishing landline and wireless numbers.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import phone_verification_service_api
from com.precisely.apis.model.phone_verification import PhoneVerification
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.validate_phone_number_api_request import ValidatePhoneNumberAPIRequest
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
    api_instance = phone_verification_service_api.PhoneVerificationServiceApi(api_client)
    validate_phone_number_api_request = ValidatePhoneNumberAPIRequest(
        input=ValidatePhoneNumberAPIRequestInput(
            row=[
                ValidatePhoneNumberAPIRequestInputRow(
                    phone_number="phone_number_example",
                    country="country_example",
                ),
            ],
        ),
    ) # ValidatePhoneNumberAPIRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Phone verification.
        api_response = api_instance.validatephonenumber(validate_phone_number_api_request)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PhoneVerificationServiceApi->validatephonenumber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_phone_number_api_request** | [**ValidatePhoneNumberAPIRequest**](ValidatePhoneNumberAPIRequest.md)|  |

### Return type

[**PhoneVerification**](PhoneVerification.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

