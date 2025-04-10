# OAuthLoginInput

OAuth login input model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**code** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**id_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from autoaudit.models.o_auth_login_input import OAuthLoginInput

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthLoginInput from a JSON string
o_auth_login_input_instance = OAuthLoginInput.from_json(json)
# print the JSON string representation of the object
print(OAuthLoginInput.to_json())

# convert the object into a dict
o_auth_login_input_dict = o_auth_login_input_instance.to_dict()
# create an instance of OAuthLoginInput from a dict
o_auth_login_input_from_dict = OAuthLoginInput.from_dict(o_auth_login_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


