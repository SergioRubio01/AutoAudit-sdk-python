# AutoauditInterfacesApiV1AgentsAgentResponse

Response model for agents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | 
**agent_type** | **str** |  | 
**model_id** | **str** |  | 
**owner_id** | **str** |  | 
**project_id** | **str** |  | [optional] 
**tools** | **List[Dict[str, object]]** |  | [optional] [default to []]
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**last_active** | **str** |  | [optional] 

## Example

```python
from autoaudit.models.autoaudit_interfaces_api_v1_agents_agent_response import AutoauditInterfacesApiV1AgentsAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoauditInterfacesApiV1AgentsAgentResponse from a JSON string
autoaudit_interfaces_api_v1_agents_agent_response_instance = AutoauditInterfacesApiV1AgentsAgentResponse.from_json(json)
# print the JSON string representation of the object
print(AutoauditInterfacesApiV1AgentsAgentResponse.to_json())

# convert the object into a dict
autoaudit_interfaces_api_v1_agents_agent_response_dict = autoaudit_interfaces_api_v1_agents_agent_response_instance.to_dict()
# create an instance of AutoauditInterfacesApiV1AgentsAgentResponse from a dict
autoaudit_interfaces_api_v1_agents_agent_response_from_dict = AutoauditInterfacesApiV1AgentsAgentResponse.from_dict(autoaudit_interfaces_api_v1_agents_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


