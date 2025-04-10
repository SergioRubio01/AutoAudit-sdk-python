# DocumentMetadataResponse

Response model for document metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_type** | **str** |  | [optional] 
**main_topics** | **List[str]** |  | [optional] 
**created_date** | **str** |  | [optional] 
**document_category** | **str** |  | [optional] 
**has_tables** | **bool** |  | [optional] 
**extracted_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.document_metadata_response import DocumentMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetadataResponse from a JSON string
document_metadata_response_instance = DocumentMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentMetadataResponse.to_json())

# convert the object into a dict
document_metadata_response_dict = document_metadata_response_instance.to_dict()
# create an instance of DocumentMetadataResponse from a dict
document_metadata_response_from_dict = DocumentMetadataResponse.from_dict(document_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


