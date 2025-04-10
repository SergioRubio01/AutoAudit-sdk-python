# autoaudit.SandboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_code_sandbox_execute_post**](SandboxApi.md#execute_code_sandbox_execute_post) | **POST** /sandbox/execute | Execute Code
[**health_check_sandbox_health_get**](SandboxApi.md#health_check_sandbox_health_get) | **GET** /sandbox/health | Health Check


# **execute_code_sandbox_execute_post**
> CodeExecutionResponse execute_code_sandbox_execute_post(code_execution_request, authorization=authorization)

Execute Code

Execute code in a sandboxed environment

### Example


```python
import autoaudit
from autoaudit.models.code_execution_request import CodeExecutionRequest
from autoaudit.models.code_execution_response import CodeExecutionResponse
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SandboxApi(api_client)
    code_execution_request = autoaudit.CodeExecutionRequest() # CodeExecutionRequest | 
    authorization = 'authorization_example' # str |  (optional)

    try:
        # Execute Code
        api_response = api_instance.execute_code_sandbox_execute_post(code_execution_request, authorization=authorization)
        print("The response of SandboxApi->execute_code_sandbox_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->execute_code_sandbox_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_execution_request** | [**CodeExecutionRequest**](CodeExecutionRequest.md)|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**CodeExecutionResponse**](CodeExecutionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_sandbox_health_get**
> object health_check_sandbox_health_get()

Health Check

Health check endpoint

### Example


```python
import autoaudit
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SandboxApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_sandbox_health_get()
        print("The response of SandboxApi->health_check_sandbox_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->health_check_sandbox_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

