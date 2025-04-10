# WorkflowResponse

Response model for workflows

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**version** | **str** |  | 
**owner_id** | **str** |  | 
**is_public** | **bool** |  | 
**tags** | **List[str]** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**nodes_count** | **int** |  | 
**edges_count** | **int** |  | 

## Example

```python
from autoaudit.models.workflow_response import WorkflowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponse from a JSON string
workflow_response_instance = WorkflowResponse.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponse.to_json())

# convert the object into a dict
workflow_response_dict = workflow_response_instance.to_dict()
# create an instance of WorkflowResponse from a dict
workflow_response_from_dict = WorkflowResponse.from_dict(workflow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


