# ProjectResponse

Response model for projects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | 
**status** | **str** |  | 
**owner_id** | **str** |  | 
**project_type** | **str** |  | 
**description** | **str** |  | [optional] 
**modules** | **List[str]** |  | [optional] [default to []]
**selected_models** | **Dict[str, List[str]]** |  | [optional] 
**selected_workflows** | **Dict[str, object]** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from autoaudit.models.project_response import ProjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponse from a JSON string
project_response_instance = ProjectResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectResponse.to_json())

# convert the object into a dict
project_response_dict = project_response_instance.to_dict()
# create an instance of ProjectResponse from a dict
project_response_from_dict = ProjectResponse.from_dict(project_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


