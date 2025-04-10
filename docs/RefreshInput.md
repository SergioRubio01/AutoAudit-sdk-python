# RefreshInput

Refresh token input model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | 

## Example

```python
from autoaudit.models.refresh_input import RefreshInput

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshInput from a JSON string
refresh_input_instance = RefreshInput.from_json(json)
# print the JSON string representation of the object
print(RefreshInput.to_json())

# convert the object into a dict
refresh_input_dict = refresh_input_instance.to_dict()
# create an instance of RefreshInput from a dict
refresh_input_from_dict = RefreshInput.from_dict(refresh_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


