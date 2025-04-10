# AgentCommandRequest

Request model for agent commands

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | 
**context** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.agent_command_request import AgentCommandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCommandRequest from a JSON string
agent_command_request_instance = AgentCommandRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCommandRequest.to_json())

# convert the object into a dict
agent_command_request_dict = agent_command_request_instance.to_dict()
# create an instance of AgentCommandRequest from a dict
agent_command_request_from_dict = AgentCommandRequest.from_dict(agent_command_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


