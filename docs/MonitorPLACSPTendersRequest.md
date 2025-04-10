# MonitorPLACSPTendersRequest

Request model for monitoring PLACSP tenders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_keywords** | **List[str]** | Keywords to search for in tender descriptions | [optional] 
**categories** | **List[str]** | Categories of tenders to search for | [optional] 
**min_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**regions** | **List[str]** | Spanish regions to search in | [optional] 

## Example

```python
from autoaudit.models.monitor_placsp_tenders_request import MonitorPLACSPTendersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorPLACSPTendersRequest from a JSON string
monitor_placsp_tenders_request_instance = MonitorPLACSPTendersRequest.from_json(json)
# print the JSON string representation of the object
print(MonitorPLACSPTendersRequest.to_json())

# convert the object into a dict
monitor_placsp_tenders_request_dict = monitor_placsp_tenders_request_instance.to_dict()
# create an instance of MonitorPLACSPTendersRequest from a dict
monitor_placsp_tenders_request_from_dict = MonitorPLACSPTendersRequest.from_dict(monitor_placsp_tenders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


