# AutoauditInterfacesApiV1SuperagentsAgentResponse

Response model for agent details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**capabilities** | [**List[AgentCapabilityResponse]**](AgentCapabilityResponse.md) |  | 
**tools** | [**List[AgentToolResponse]**](AgentToolResponse.md) |  | [optional] 
**llm_id** | **str** |  | [optional] 
**organization_id** | **str** |  | 
**creator_id** | **str** |  | 
**status** | **str** |  | 
**execution_tier** | **str** |  | 
**max_iterations** | **int** |  | 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**last_execution_at** | **str** |  | [optional] 
**execution_count** | **int** |  | [optional] [default to 0]
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_agent_response import AutoauditInterfacesApiV1SuperagentsAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AutoauditInterfacesApiV1SuperagentsAgentResponse from a JSON string
autoaudit_interfaces_api_v1_superagents_agent_response_instance = AutoauditInterfacesApiV1SuperagentsAgentResponse.from_json(json)
# print the JSON string representation of the object
print(AutoauditInterfacesApiV1SuperagentsAgentResponse.to_json())

# convert the object into a dict
autoaudit_interfaces_api_v1_superagents_agent_response_dict = autoaudit_interfaces_api_v1_superagents_agent_response_instance.to_dict()
# create an instance of AutoauditInterfacesApiV1SuperagentsAgentResponse from a dict
autoaudit_interfaces_api_v1_superagents_agent_response_from_dict = AutoauditInterfacesApiV1SuperagentsAgentResponse.from_dict(autoaudit_interfaces_api_v1_superagents_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


