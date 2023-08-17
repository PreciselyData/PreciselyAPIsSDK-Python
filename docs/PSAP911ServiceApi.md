# com.precisely.apis.PSAP911ServiceApi

All URIs are relative to *https://api.precisely.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ahj_plus_psapby_address**](PSAP911ServiceApi.md#get_ahj_plus_psapby_address) | **GET** /911/v1/ahj-psap/byaddress | AHJ &amp; PSAP By Address.
[**get_ahj_plus_psapby_location**](PSAP911ServiceApi.md#get_ahj_plus_psapby_location) | **GET** /911/v1/ahj-psap/bylocation | AHJ &amp; PSAP By Location
[**get_psapby_address**](PSAP911ServiceApi.md#get_psapby_address) | **GET** /911/v1/psap/byaddress | PSAP By Address.
[**get_psapby_location**](PSAP911ServiceApi.md#get_psapby_location) | **GET** /911/v1/psap/bylocation | PSAP By Location.
[**search_by_fcc_id**](PSAP911ServiceApi.md#search_by_fcc_id) | **GET** /911/v1/ahj-psap/byfccid | AHJ &amp; PSAP By Fccid


# **get_ahj_plus_psapby_address**
> AHJPlusPSAPResponse get_ahj_plus_psapby_address(address)

AHJ & PSAP By Address.

Accepts addresses as input and Returns contact details for Authorities Having Jurisdiction (AHJ) on-behalf-of local Public Safety Answering Points (PSAP). 911/PSAP accepts an address and returns PSAP contact data plus contact data for an AHJ to communicate directly with a PSAP. Details include agency name, phone number, city name, coverage, contact person's details, site details and mailing addresses for EMS, Fire, and Police PSAP contacts.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import psap_911_service_api
from com.precisely.apis.model.ahj_plus_psap_response import AHJPlusPSAPResponse
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
    api_instance = psap_911_service_api.PSAP911ServiceApi(api_client)
    address = "address_example" # str | The address to be searched.

    # example passing only required values which don't have defaults set
    try:
        # AHJ & PSAP By Address.
        api_response = api_instance.get_ahj_plus_psapby_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PSAP911ServiceApi->get_ahj_plus_psapby_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |

### Return type

[**AHJPlusPSAPResponse**](AHJPlusPSAPResponse.md)

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

# **get_ahj_plus_psapby_location**
> AHJPlusPSAPResponse get_ahj_plus_psapby_location(longitude, latitude)

AHJ & PSAP By Location

Accepts latitude & longitude as input and Returns contact details for Authorities Having Jurisdiction (AHJ) on-behalf-of local Public Safety Answering Points (PSAP). 911/PSAP accepts a location coordinate and returns PSAP contact data plus contact data for an AHJ to communicate directly with a PSAP. Details include agency name, phone number, city name, coverage, contact person's details, site details and mailing addresses for EMS, Fire, and Police PSAP contacts.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import psap_911_service_api
from com.precisely.apis.model.ahj_plus_psap_response import AHJPlusPSAPResponse
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
    api_instance = psap_911_service_api.PSAP911ServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location.
    latitude = "latitude_example" # str | Latitude of the location.

    # example passing only required values which don't have defaults set
    try:
        # AHJ & PSAP By Location
        api_response = api_instance.get_ahj_plus_psapby_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PSAP911ServiceApi->get_ahj_plus_psapby_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. |
 **latitude** | **str**| Latitude of the location. |

### Return type

[**AHJPlusPSAPResponse**](AHJPlusPSAPResponse.md)

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

# **get_psapby_address**
> PSAPResponse get_psapby_address(address)

PSAP By Address.

Accepts addresses as input and Returns contact details for local Public Safety Answering Points (PSAP). 911/PSAP accepts an address as input and returns the relevant PSAP address and contact details including agency name, phone number, county name, coverage, contact person's details, site details and mailing address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import psap_911_service_api
from com.precisely.apis.model.psap_response import PSAPResponse
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
    api_instance = psap_911_service_api.PSAP911ServiceApi(api_client)
    address = "address_example" # str | The address to be searched.

    # example passing only required values which don't have defaults set
    try:
        # PSAP By Address.
        api_response = api_instance.get_psapby_address(address)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PSAP911ServiceApi->get_psapby_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| The address to be searched. |

### Return type

[**PSAPResponse**](PSAPResponse.md)

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

# **get_psapby_location**
> PSAPResponse get_psapby_location(longitude, latitude)

PSAP By Location.

Accepts latitude & longitude as input and Returns contact details for local Public Safety Answering Points (PSAP). 911/PSAP accepts a location coordinate and returns the relevant PSAP address and contact details including dispatch name, phone number, county name, coverage, contact person's details, site details and mailing address.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import psap_911_service_api
from com.precisely.apis.model.psap_response import PSAPResponse
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
    api_instance = psap_911_service_api.PSAP911ServiceApi(api_client)
    longitude = "longitude_example" # str | Longitude of the location.
    latitude = "latitude_example" # str | Latitude of the location.

    # example passing only required values which don't have defaults set
    try:
        # PSAP By Location.
        api_response = api_instance.get_psapby_location(longitude, latitude)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PSAP911ServiceApi->get_psapby_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **longitude** | **str**| Longitude of the location. |
 **latitude** | **str**| Latitude of the location. |

### Return type

[**PSAPResponse**](PSAPResponse.md)

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

# **search_by_fcc_id**
> AHJPlusPSAPResponse search_by_fcc_id(fcc_id)

AHJ & PSAP By Fccid

Accepts fccid as input and Returns contact details for Authorities Having Jurisdiction (AHJ) on-behalf-of local Public Safety Answering Points (PSAP). 911/PSAP accepts a location coordinate and returns PSAP contact data plus contact data for an AHJ to communicate directly with a PSAP. Details include agency name, phone number, city name, coverage, contact person's details, site details and mailing addresses for EMS, Fire, and Police PSAP contacts.

### Example

* OAuth Authentication (oAuth2Password):

```python
import time
import com.precisely.apis
from com.precisely.apis.api import psap_911_service_api
from com.precisely.apis.model.ahj_plus_psap_response import AHJPlusPSAPResponse
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
    api_instance = psap_911_service_api.PSAP911ServiceApi(api_client)
    fcc_id = "fccId_example" # str | fccId

    # example passing only required values which don't have defaults set
    try:
        # AHJ & PSAP By Fccid
        api_response = api_instance.search_by_fcc_id(fcc_id)
        pprint(api_response)
    except com.precisely.apis.ApiException as e:
        print("Exception when calling PSAP911ServiceApi->search_by_fcc_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fcc_id** | **str**| fccId |

### Return type

[**AHJPlusPSAPResponse**](AHJPlusPSAPResponse.md)

### Authorization

[oAuth2Password](../README.md#oAuth2Password)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

