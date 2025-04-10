# ProjectCreateRequest

Request model for project creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**organization_id** | **str** |  | 
**project_type** | **str** |  | 
**description** | **str** |  | [optional] 
**modules** | **List[str]** |  | [optional] 
**selected_models** | **Dict[str, List[str]]** |  | [optional] 
**selected_workflows** | **Dict[str, object]** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.project_create_request import ProjectCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateRequest from a JSON string
project_create_request_instance = ProjectCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateRequest.to_json())

# convert the object into a dict
project_create_request_dict = project_create_request_instance.to_dict()
# create an instance of ProjectCreateRequest from a dict
project_create_request_from_dict = ProjectCreateRequest.from_dict(project_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


