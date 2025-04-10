# MonitorPLACSPTendersResponse

Response model for PLACSP monitoring results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**total_tenders** | **int** |  | 
**tenders** | **List[Dict[str, object]]** |  | 
**search_criteria** | **Dict[str, object]** |  | 
**search_timestamp** | **str** |  | 
**error_message** | **str** |  | [optional] 

## Example

```python
from autoaudit.models.monitor_placsp_tenders_response import MonitorPLACSPTendersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorPLACSPTendersResponse from a JSON string
monitor_placsp_tenders_response_instance = MonitorPLACSPTendersResponse.from_json(json)
# print the JSON string representation of the object
print(MonitorPLACSPTendersResponse.to_json())

# convert the object into a dict
monitor_placsp_tenders_response_dict = monitor_placsp_tenders_response_instance.to_dict()
# create an instance of MonitorPLACSPTendersResponse from a dict
monitor_placsp_tenders_response_from_dict = MonitorPLACSPTendersResponse.from_dict(monitor_placsp_tenders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


