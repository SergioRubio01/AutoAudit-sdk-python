# ProjectMemberAddRequest

Request model for adding a member to a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from autoaudit.models.project_member_add_request import ProjectMemberAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMemberAddRequest from a JSON string
project_member_add_request_instance = ProjectMemberAddRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectMemberAddRequest.to_json())

# convert the object into a dict
project_member_add_request_dict = project_member_add_request_instance.to_dict()
# create an instance of ProjectMemberAddRequest from a dict
project_member_add_request_from_dict = ProjectMemberAddRequest.from_dict(project_member_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


