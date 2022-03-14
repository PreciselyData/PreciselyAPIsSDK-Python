# ValidateMailingAddressProOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_fields** | [**[GetPostalCodesAPIOutputUserFields]**](GetPostalCodesAPIOutputUserFields.md) | These fields are returned, unmodified, in the user_fields section of the response. | [optional] 
**address_line1** | **str** | The first line of the validated address. | [optional] 
**address_line2** | **str** | The second line of the validated address. | [optional] 
**firm_name** | **str** | The validated firm or company name. | [optional] 
**change_score** | **str** | A value of 0 and 100 that reflects how much the address has changed to make it valid. | [optional] 
**locality** | **str** | Generally a locality is a village in rural areas or it may be a suburb in urban areas. | [optional] 
**suburb** | **str** | The suburb name. | [optional] 
**address_type** | **str** | A single letter code that indicates the type of address. | [optional] 
**deliverability** | **str** | An estimate of confidence that an item mailed or shipped to this address would be successfully delivered. | [optional] 
**address_quality** | **str** | A two character code indicating overall quality of the resulting address. | [optional] 
**could_not_validate** | **str** | Mentions the address component that could not be validated, in case no match is found. | [optional] 
**city** | **str** | The validated city name. | [optional] 
**postal_code** | **str** | The validated ZIP Code or postal code. | [optional] 
**country** | **str** | The country in the format determined by what you selected. | [optional] 
**state_province** | **str** | The validated state or province abbreviation. | [optional] 
**block_address** | **str** | The formatted address, as it would appear on a physical mail piece. | [optional] 
**additional_input_data** | **str** | Input data that could not be matched to a particular address component. | [optional] 
**postal_code_base** | **str** | The 5-digit ZIP Code. | [optional] 
**postal_code_add_on** | **str** | The 4-digit add-on part of the ZIP Code. | [optional] 
**status** | **str** | Reports the success or failure of the match attempt. | [optional] 
**status_code** | **str** | Reason for failure, if there is one. | [optional] 
**status_description** | **str** | Description of the problem, if there is one. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


