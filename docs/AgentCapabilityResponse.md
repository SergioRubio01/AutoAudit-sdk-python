# AgentCapabilityResponse

Response model for agent capability

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**parameters** | **Dict[str, object]** |  | [optional] 
**category** | **str** |  | 
**execution_tier** | **str** |  | 

## Example

```python
from autoaudit.models.agent_capability_response import AgentCapabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCapabilityResponse from a JSON string
agent_capability_response_instance = AgentCapabilityResponse.from_json(json)
# print the JSON string representation of the object
print(AgentCapabilityResponse.to_json())

# convert the object into a dict
agent_capability_response_dict = agent_capability_response_instance.to_dict()
# create an instance of AgentCapabilityResponse from a dict
agent_capability_response_from_dict = AgentCapabilityResponse.from_dict(agent_capability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


