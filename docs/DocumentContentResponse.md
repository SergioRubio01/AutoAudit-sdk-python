# DocumentContentResponse

Response model for document content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**key_insights** | **List[str]** |  | [optional] 
**language** | **str** |  | [optional] 
**word_count** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**metadata** | [**DocumentMetadataResponse**](DocumentMetadataResponse.md) |  | [optional] 

## Example

```python
from autoaudit.models.document_content_response import DocumentContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentContentResponse from a JSON string
document_content_response_instance = DocumentContentResponse.from_json(json)
# print the JSON string representation of the object
print(DocumentContentResponse.to_json())

# convert the object into a dict
document_content_response_dict = document_content_response_instance.to_dict()
# create an instance of DocumentContentResponse from a dict
document_content_response_from_dict = DocumentContentResponse.from_dict(document_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


