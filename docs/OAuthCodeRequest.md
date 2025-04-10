# OAuthCodeRequest

OAuth code request model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from autoaudit.models.o_auth_code_request import OAuthCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCodeRequest from a JSON string
o_auth_code_request_instance = OAuthCodeRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthCodeRequest.to_json())

# convert the object into a dict
o_auth_code_request_dict = o_auth_code_request_instance.to_dict()
# create an instance of OAuthCodeRequest from a dict
o_auth_code_request_from_dict = OAuthCodeRequest.from_dict(o_auth_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


