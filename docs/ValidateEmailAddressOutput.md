# ValidateEmailAddressOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_fields** | [**[GetPostalCodesAPIOutputUserFields]**](GetPostalCodesAPIOutputUserFields.md) | These fields are returned, unmodified, in the user_fields section of the response. | [optional] 
**email** | **str** | The email address submitted for verification. | [optional] 
**finding** | **str** | One character code indicating the validity of the submitted email address. | [optional] 
**comment** | **str** | The comment string pertaining to the result of the submitted email address. | [optional] 
**comment_code** | **str** | A short code which maps to each returned COMMENT field value. | [optional] 
**sugg_email** | **str** | Suggested correction for submitted email address, if found. A suggestion will only be provided if it is valid and SafeToDeliver. | [optional] 
**sugg_comment** | **str** | This field contains suggestion not SafeToDeliver when ValidateEmailAddress corrected the address and the corrected version of the email address failed one or more SafeToDeliver process checks. | [optional] 
**error_response** | **str** | Pre-formatted response intended to be provided to user. | [optional] 
**error** | **str** | Field reserved for special features only. | [optional] 
**status** | **str** |  | [optional] 
**status_code** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


