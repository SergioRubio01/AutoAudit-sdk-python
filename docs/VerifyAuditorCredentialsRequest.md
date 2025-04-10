# VerifyAuditorCredentialsRequest

Request model for verifying auditor credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_url** | **str** | URL to the document containing credential information | 
**credential_type** | **str** | Type of credential to verify (ROAC, CISA, etc.) | [optional] [default to 'ROAC']
**organization_id** | **str** |  | [optional] 

## Example

```python
from autoaudit.models.verify_auditor_credentials_request import VerifyAuditorCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAuditorCredentialsRequest from a JSON string
verify_auditor_credentials_request_instance = VerifyAuditorCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyAuditorCredentialsRequest.to_json())

# convert the object into a dict
verify_auditor_credentials_request_dict = verify_auditor_credentials_request_instance.to_dict()
# create an instance of VerifyAuditorCredentialsRequest from a dict
verify_auditor_credentials_request_from_dict = VerifyAuditorCredentialsRequest.from_dict(verify_auditor_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


