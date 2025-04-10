# CodeExecutionRequest

Request model for code execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**language** | **str** |  | [optional] [default to 'python']
**context** | **Dict[str, object]** |  | [optional] 
**dependencies** | **List[str]** |  | [optional] 

## Example

```python
from autoaudit.models.code_execution_request import CodeExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodeExecutionRequest from a JSON string
code_execution_request_instance = CodeExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(CodeExecutionRequest.to_json())

# convert the object into a dict
code_execution_request_dict = code_execution_request_instance.to_dict()
# create an instance of CodeExecutionRequest from a dict
code_execution_request_from_dict = CodeExecutionRequest.from_dict(code_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


