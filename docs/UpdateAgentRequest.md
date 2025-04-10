# UpdateAgentRequest

Request model for updating an agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**capabilities** | [**List[AgentCapabilityRequest]**](AgentCapabilityRequest.md) |  | [optional] 
**tools** | [**List[AgentToolRequest]**](AgentToolRequest.md) |  | [optional] 
**llm_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**execution_tier** | **str** |  | [optional] 
**max_iterations** | **int** |  | [optional] 
**status** | [**AgentStatus**](AgentStatus.md) |  | [optional] 

## Example

```python
from autoaudit.models.update_agent_request import UpdateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentRequest from a JSON string
update_agent_request_instance = UpdateAgentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAgentRequest.to_json())

# convert the object into a dict
update_agent_request_dict = update_agent_request_instance.to_dict()
# create an instance of UpdateAgentRequest from a dict
update_agent_request_from_dict = UpdateAgentRequest.from_dict(update_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


