# ProjectUpdateRequest

Request model for project update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**project_type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modules** | **List[str]** |  | [optional] 
**selected_models** | **Dict[str, List[str]]** |  | [optional] 
**selected_workflows** | **Dict[str, object]** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.project_update_request import ProjectUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateRequest from a JSON string
project_update_request_instance = ProjectUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateRequest.to_json())

# convert the object into a dict
project_update_request_dict = project_update_request_instance.to_dict()
# create an instance of ProjectUpdateRequest from a dict
project_update_request_from_dict = ProjectUpdateRequest.from_dict(project_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


