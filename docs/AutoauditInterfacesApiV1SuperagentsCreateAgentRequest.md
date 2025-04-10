# AutoauditInterfacesApiV1SuperagentsCreateAgentRequest

Request model for creating an agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**capabilities** | [**List[AgentCapabilityRequest]**](AgentCapabilityRequest.md) |  | 
**tools** | [**List[AgentToolRequest]**](AgentToolRequest.md) |  | [optional] 
**llm_id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**execution_tier** | **str** |  | [optional] [default to 'standard']
**max_iterations** | **int** |  | [optional] [default to 10]

## Example

```python
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_create_agent_request import AutoauditInterfacesApiV1SuperagentsCreateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoauditInterfacesApiV1SuperagentsCreateAgentRequest from a JSON string
autoaudit_interfaces_api_v1_superagents_create_agent_request_instance = AutoauditInterfacesApiV1SuperagentsCreateAgentRequest.from_json(json)
# print the JSON string representation of the object
print(AutoauditInterfacesApiV1SuperagentsCreateAgentRequest.to_json())

# convert the object into a dict
autoaudit_interfaces_api_v1_superagents_create_agent_request_dict = autoaudit_interfaces_api_v1_superagents_create_agent_request_instance.to_dict()
# create an instance of AutoauditInterfacesApiV1SuperagentsCreateAgentRequest from a dict
autoaudit_interfaces_api_v1_superagents_create_agent_request_from_dict = AutoauditInterfacesApiV1SuperagentsCreateAgentRequest.from_dict(autoaudit_interfaces_api_v1_superagents_create_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


