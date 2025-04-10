# AgentToolRequest

Request model for agent tool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_id** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.agent_tool_request import AgentToolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentToolRequest from a JSON string
agent_tool_request_instance = AgentToolRequest.from_json(json)
# print the JSON string representation of the object
print(AgentToolRequest.to_json())

# convert the object into a dict
agent_tool_request_dict = agent_tool_request_instance.to_dict()
# create an instance of AgentToolRequest from a dict
agent_tool_request_from_dict = AgentToolRequest.from_dict(agent_tool_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


