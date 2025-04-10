# AutoauditInterfacesApiV1AgentsCreateAgentRequest

Request model for agent creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**model_id** | **str** |  | 
**agent_type** | **str** |  | 
**project_id** | **str** |  | [optional] 
**selected_capabilities** | **List[str]** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.autoaudit_interfaces_api_v1_agents_create_agent_request import AutoauditInterfacesApiV1AgentsCreateAgentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoauditInterfacesApiV1AgentsCreateAgentRequest from a JSON string
autoaudit_interfaces_api_v1_agents_create_agent_request_instance = AutoauditInterfacesApiV1AgentsCreateAgentRequest.from_json(json)
# print the JSON string representation of the object
print(AutoauditInterfacesApiV1AgentsCreateAgentRequest.to_json())

# convert the object into a dict
autoaudit_interfaces_api_v1_agents_create_agent_request_dict = autoaudit_interfaces_api_v1_agents_create_agent_request_instance.to_dict()
# create an instance of AutoauditInterfacesApiV1AgentsCreateAgentRequest from a dict
autoaudit_interfaces_api_v1_agents_create_agent_request_from_dict = AutoauditInterfacesApiV1AgentsCreateAgentRequest.from_dict(autoaudit_interfaces_api_v1_agents_create_agent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


