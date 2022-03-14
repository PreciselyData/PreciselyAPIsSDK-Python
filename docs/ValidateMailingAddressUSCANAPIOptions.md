# ValidateMailingAddressUSCANAPIOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_address_blocks** | **str** | Specifies whether to return a formatted version of the address. | [optional]  if omitted the server will use the default value of "Y"
**perform_us_processing** | **str** | Specifies whether or not to process U.S. addresses. | [optional]  if omitted the server will use the default value of "Y"
**perform_dpv** | **str** | Delivery Point Validation (DPV®) validates that a specific address exists | [optional]  if omitted the server will use the default value of "N"
**output_formatted_on_fail** | **str** | Specifies whether to return a formatted address when an address cannot be validated. | [optional]  if omitted the server will use the default value of "N"
**output_postal_code_separator** | **str** | Specifies whether to use separators (spaces or hyphens) in ZIP™ Codes or Canadian postal codes. | [optional]  if omitted the server will use the default value of "Y"
**output_country_format** | **str** | Specifies the format to use for the country name returned in the Country output field. | [optional]  if omitted the server will use the default value of "E"
**keep_multimatch** | **str** | Indicates whether to return multiple address for input addresses that have more than one possible matches. | [optional]  if omitted the server will use the default value of "N"
**output_casing** | **str** | Specifies the casing of the output address. M for mixed case and U for upper case. | [optional]  if omitted the server will use the default value of "M"
**maximum_results** | **str** | Specifies a number between 1 and 10 that indicates the maximum number of addresses to be returned. | [optional]  if omitted the server will use the default value of "10"
**output_record_type** | **str** | Specifies the type of the output record. | [optional]  if omitted the server will use the default value of "A"
**output_field_level_return_codes** | **str** | Identifies which output addresses are candidate addresses as value if Y for OutputFieldLevelReturnCodes. | [optional]  if omitted the server will use the default value of "N"
**dpv_determine_no_stat** | **str** | Determines the no stat status of an address which means it exists but cannot receive mails. | [optional]  if omitted the server will use the default value of "N"
**street_matching_strictness** | **str** | Specifies the algorithm to determe if an input address matches in the postal database. | [optional]  if omitted the server will use the default value of "M"
**can_french_apartment_label** | **str** | Specifies the default apartment label for the output if there is no apartment label in the input address. This is specific to French address.  | [optional]  if omitted the server will use the default value of "Appartement"
**output_abbreviated_alias** | **str** | Specifies whether to use a street&#39;s abbreviated alias in the output if the output address line is longer than 31 characters. | [optional]  if omitted the server will use the default value of "N"
**dpv_successful_status_condition** | **str** | Selecting the match condition where a DPV result does NOT cause a record to fail. | [optional]  if omitted the server will use the default value of "A"
**standard_address_pmb_line** | **str** | Specifies where Private Mailbox (PMB) information is placed. | [optional]  if omitted the server will use the default value of "N"
**firm_matching_strictness** | **str** | Specifies the algorithm to determining if an input address matches in the postal database. | [optional]  if omitted the server will use the default value of "M"
**can_rural_route_format** | **str** | Specifies where to place rural route delivery information. | [optional]  if omitted the server will use the default value of "A"
**can_prefer_house_num** | **str** | Specifies whether to select a house number of postal code in case of conflict. | [optional]  if omitted the server will use the default value of "N"
**output_preferred_alias** | **str** | Specifies whether to use a street&#39;s preferred alias in the output. | [optional]  if omitted the server will use the default value of "N"
**directional_matching_strictness** | **str** | Specifies the algorithm to determine if an input address matches in the postal database. | [optional]  if omitted the server will use the default value of "M"
**extract_firm** | **str** | Specifies whether to extract the firm name from AddressLine1 through AddressLine4 and place it in the FirmName output field. | [optional]  if omitted the server will use the default value of "N"
**fail_on_cmra_match** | **str** | Specifies whether to consider Treat Commercial Mail Receiving Agency (CMRA) matches as failures? | [optional]  if omitted the server will use the default value of "N"
**can_non_civic_format** | **str** | Specifies whether or not non-civic keywords are abbreviated in the output.  | [optional]  if omitted the server will use the default value of "A"
**can_sslvr_flg** | **str** | Changes the civic and/or suite information to match the LVR or single-single record. | [optional]  if omitted the server will use the default value of "N"
**output_street_name_alias** | **str** | Specifies how to handle street name aliases used in the input. This is specific to US. | [optional]  if omitted the server will use the default value of "Y"
**perform_ews** | **str** | Specifies the Early Warning System (EWS) that uses the USPS EWS File to validate addresses that are not in the ZIP + 4 database. | [optional]  if omitted the server will use the default value of "N"
**can_output_city_format** | **str** | Specifies whether to use the long, medium, or short version of the city if the city has a long name. | [optional]  if omitted the server will use the default value of "D"
**dual_address_logic** | **str** | Specifies how to return a match if multiple non-blank address lines are present or multiple address types are on the same address line. (U.S. addresses only.) | [optional]  if omitted the server will use the default value of "N"
**perform_suite_link** | **str** | Specifies whether to perform SuiteLink processing. | [optional]  if omitted the server will use the default value of "N"
**can_standard_address_format** | **str** | Specifies where to place secondary address information in the output address. | [optional]  if omitted the server will use the default value of "D"
**output_preferred_city** | **str** | Specifies whether the preferred last line city name should be stored. | [optional]  if omitted the server will use the default value of "Z"
**output_multinational_characters** | **str** | Specifies whether to return multinational characters, including diacritical marks such as umlauts or accents. | [optional]  if omitted the server will use the default value of "N"
**can_delivery_office_format** | **str** | Specifies where to place station information. | [optional]  if omitted the server will use the default value of "I"
**perform_lacs_link** | **str** | Facilitates the conversion of rural route address converting into street-style address using the LACS. | [optional]  if omitted the server will use the default value of "Y"
**can_dual_address_logic** | **str** | Specifies whether ValidateMailingAddressUSCAN should return a street match or a PO Box/non-civic match when the address contains both civic and non-civic information. | [optional]  if omitted the server will use the default value of "D"
**extract_urb** | **str** | Specifies whether to extract the urbanization name from AddressLine1 through AddressLine4 and place it in the USUrbanName output field.  | [optional]  if omitted the server will use the default value of "N"
**standard_address_format** | **str** | Specifies where to place secondary address information for U.S. addresses. | [optional]  if omitted the server will use the default value of "C"
**can_french_format** | **str** | Specifies how to determine the language (English or French) to use to format the address and directional. | [optional]  if omitted the server will use the default value of "C"
**dpv_determine_vacancy** | **str** | Determines if the location has been unoccupied for at least 90 days. | [optional]  if omitted the server will use the default value of "N"
**can_english_apartment_label** | **str** | Specifies the default apartment label to use in the output if there is no apartment label in the input address. rhis is specific to English addresses. | [optional]  if omitted the server will use the default value of "Apt"
**suppress_zplus_phantom_carrier_r777** | **str** | Specifies whether to supress addresses with Carrier Route R777. | [optional]  if omitted the server will use the default value of "N"
**can_output_city_alias** | **str** | Specifies whether or not to return the city alias when the alias is in the input address. | [optional]  if omitted the server will use the default value of "N"
**output_short_city_name** | **str** | Specifies how to format city names that have short city name or non-mailing city name alternatives. | [optional]  if omitted the server will use the default value of "N"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


