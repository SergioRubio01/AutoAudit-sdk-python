# AgentCapabilityRequest

Request model for agent capability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 
**category** | **str** |  | [optional] [default to 'general']
**execution_tier** | **str** |  | [optional] [default to 'standard']

## Example

```python
from autoaudit.models.agent_capability_request import AgentCapabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCapabilityRequest from a JSON string
agent_capability_request_instance = AgentCapabilityRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCapabilityRequest.to_json())

# convert the object into a dict
agent_capability_request_dict = agent_capability_request_instance.to_dict()
# create an instance of AgentCapabilityRequest from a dict
agent_capability_request_from_dict = AgentCapabilityRequest.from_dict(agent_capability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


