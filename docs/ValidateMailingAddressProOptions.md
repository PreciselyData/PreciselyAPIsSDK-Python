# ValidateMailingAddressProOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_address_blocks** | **str** | Specifies whether to return a formatted version of the address as it would be printed on a physical mail piece. | [optional]  if omitted the server will use the default value of "Y"
**keep_multimatch** | **str** | Specifies whether to return multiple address for those input addresses that have more than one possible match. | [optional]  if omitted the server will use the default value of "N"
**output_country_format** | **str** | Specifies the format to use for the country name returned in the Country output field. | [optional]  if omitted the server will use the default value of "E"
**output_script** | **str** | Specifies the alphabet or script in which the output should be returned. | [optional]  if omitted the server will use the default value of "InputScript"
**output_casing** | **str** | Specify the casing of the output data. | [optional]  if omitted the server will use the default value of "M"
**maximum_results** | **str** | A number between 1 and 10 that indicates the maximum number of addresses to return. | [optional]  if omitted the server will use the default value of "10"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


