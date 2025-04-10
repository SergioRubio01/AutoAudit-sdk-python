# CodeExecutionResponse

Response model for code execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**stdout** | **str** |  | 
**stderr** | **str** |  | 
**execution_time** | **float** |  | 
**exit_code** | **int** |  | [optional] 

## Example

```python
from autoaudit.models.code_execution_response import CodeExecutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeExecutionResponse from a JSON string
code_execution_response_instance = CodeExecutionResponse.from_json(json)
# print the JSON string representation of the object
print(CodeExecutionResponse.to_json())

# convert the object into a dict
code_execution_response_dict = code_execution_response_instance.to_dict()
# create an instance of CodeExecutionResponse from a dict
code_execution_response_from_dict = CodeExecutionResponse.from_dict(code_execution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


