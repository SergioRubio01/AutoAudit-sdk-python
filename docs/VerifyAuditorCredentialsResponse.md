# VerifyAuditorCredentialsResponse

Response model for auditor credential verification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditor_profile_id** | **str** |  | 
**credential_type** | **str** |  | 
**verified** | **bool** |  | 
**credential_number** | **str** |  | [optional] 
**verification_date** | **str** |  | [optional] 
**valid_until** | **str** |  | [optional] 
**details** | **Dict[str, object]** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from autoaudit.models.verify_auditor_credentials_response import VerifyAuditorCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAuditorCredentialsResponse from a JSON string
verify_auditor_credentials_response_instance = VerifyAuditorCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyAuditorCredentialsResponse.to_json())

# convert the object into a dict
verify_auditor_credentials_response_dict = verify_auditor_credentials_response_instance.to_dict()
# create an instance of VerifyAuditorCredentialsResponse from a dict
verify_auditor_credentials_response_from_dict = VerifyAuditorCredentialsResponse.from_dict(verify_auditor_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


