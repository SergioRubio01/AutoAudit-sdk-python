# AgentToolResponse

Response model for agent tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.agent_tool_response import AgentToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToolResponse from a JSON string
agent_tool_response_instance = AgentToolResponse.from_json(json)
# print the JSON string representation of the object
print(AgentToolResponse.to_json())

# convert the object into a dict
agent_tool_response_dict = agent_tool_response_instance.to_dict()
# create an instance of AgentToolResponse from a dict
agent_tool_response_from_dict = AgentToolResponse.from_dict(agent_tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


