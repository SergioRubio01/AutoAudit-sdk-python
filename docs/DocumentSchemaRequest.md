# DocumentSchemaRequest

Document schema request model for API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **Dict[str, Dict[str, object]]** |  | 
**required_fields** | **List[str]** |  | [optional] [default to []]
**document_type** | **str** |  | 

## Example

```python
from autoaudit.models.document_schema_request import DocumentSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSchemaRequest from a JSON string
document_schema_request_instance = DocumentSchemaRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentSchemaRequest.to_json())

# convert the object into a dict
document_schema_request_dict = document_schema_request_instance.to_dict()
# create an instance of DocumentSchemaRequest from a dict
document_schema_request_from_dict = DocumentSchemaRequest.from_dict(document_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


