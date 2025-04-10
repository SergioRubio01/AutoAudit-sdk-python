# AgentCommandResponse

Response model for agent commands

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**agent_id** | **str** |  | 
**timestamp** | **str** |  | 
**tool_results** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from autoaudit.models.agent_command_response import AgentCommandResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCommandResponse from a JSON string
agent_command_response_instance = AgentCommandResponse.from_json(json)
# print the JSON string representation of the object
print(AgentCommandResponse.to_json())

# convert the object into a dict
agent_command_response_dict = agent_command_response_instance.to_dict()
# create an instance of AgentCommandResponse from a dict
agent_command_response_from_dict = AgentCommandResponse.from_dict(agent_command_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


