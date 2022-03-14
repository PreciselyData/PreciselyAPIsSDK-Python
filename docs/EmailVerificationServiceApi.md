# com.precisely.apis.EmailVerificationServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_email_address**](EmailVerificationServiceApi.md#validate_email_address) | **POST** /emailverification/v1/validateemailaddress/results.json | ValidateEmailAddress


# **validate_email_address**
> ValidateEmailAddressAPIResponse validate_email_address(input_email_address)

ValidateEmailAddress

Confirm that your customer’s mailing address exists and that mail and packages can be delivered to it.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import email_verification_service_api
from com.precisely.apis.model.validate_email_address_api_response import ValidateEmailAddressAPIResponse
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.validate_email_address_api_request import ValidateEmailAddressAPIRequest
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
    api_instance = email_verification_service_api.EmailVerificationServiceApi(api_client)
    input_email_address = ValidateEmailAddressAPIRequest(
        options={},
        input=ValidateEmailAddressInput(
            row=[
                ValidateEmailAddressInputRow(
                    user_fields=[
                        GetPostalCodesAPIOutputUserFields(
                            name="name_example",
                            value="value_example",
                        ),
                    ],
                    rtc="rtc_example",
                    bogus="bogus_example",
                    role="role_example",
                    emps="emps_example",
                    fccwireless="fccwireless_example",
                    language="language_example",
                    complain="complain_example",
                    disposable="disposable_example",
                    atc="atc_example",
                    email_address="email_address_example",
                    rtc_timeout="rtc_timeout_example",
                ),
            ],
        ),
    ) # ValidateEmailAddressAPIRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ValidateEmailAddress
        api_response = api_instance.validate_email_address(input_email_address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling EmailVerificationServiceApi->validate_email_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input_email_address** | [**ValidateEmailAddressAPIRequest**](ValidateEmailAddressAPIRequest.md)|  |

### Return type

[**ValidateEmailAddressAPIResponse**](ValidateEmailAddressAPIResponse.md)

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

