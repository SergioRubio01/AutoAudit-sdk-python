# ProjectCreateFromTemplateRequest

Request model for creating a project from a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**template_id** | **str** |  | 
**organization_id** | **str** |  | 
**description** | **str** |  | [optional] 
**settings** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.project_create_from_template_request import ProjectCreateFromTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateFromTemplateRequest from a JSON string
project_create_from_template_request_instance = ProjectCreateFromTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateFromTemplateRequest.to_json())

# convert the object into a dict
project_create_from_template_request_dict = project_create_from_template_request_instance.to_dict()
# create an instance of ProjectCreateFromTemplateRequest from a dict
project_create_from_template_request_from_dict = ProjectCreateFromTemplateRequest.from_dict(project_create_from_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


