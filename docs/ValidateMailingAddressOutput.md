# ValidateMailingAddressOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_fields** | [**[GetPostalCodesAPIOutputUserFields]**](GetPostalCodesAPIOutputUserFields.md) | These fields are returned, unmodified, in the user_fields section of the response. | [optional] 
**address_line1** | **str** | The first line of the validated address. | [optional] 
**address_line2** | **str** | The second line of the validated address. | [optional] 
**firm_name** | **str** | The validated firm or company name. | [optional] 
**city** | **str** | The validated city name. | [optional] 
**postal_code** | **str** | The validated ZIP Code or postal code. | [optional] 
**country** | **str** | The country name in English. | [optional] 
**state_province** | **str** | The validated state or province abbreviation. | [optional] 
**block_address** | **str** | The formatted address, as it would appear on a physical mail piece. | [optional] 
**additional_input_data** | **str** | Input data not used by the address validation process. | [optional] 
**postal_code_base** | **str** | The 5-digit ZIP Code. | [optional] 
**postal_code_add_on** | **str** | The 4-digit add-on part of the ZIP Code. | [optional] 
**status** | **str** | Reports the success or failure of the match attempt. | [optional] 
**status_code** | **str** | Reason for failure, if there is one. | [optional] 
**status_description** | **str** | Description of the problem, if there is one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


