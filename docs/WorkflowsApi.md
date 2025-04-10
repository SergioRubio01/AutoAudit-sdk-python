# autoaudit.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_workflows_api_v1_workflows_get**](WorkflowsApi.md#list_workflows_api_v1_workflows_get) | **GET** /api/v1/workflows/ | List Workflows


# **list_workflows_api_v1_workflows_get**
> object list_workflows_api_v1_workflows_get()

List Workflows

List all workflows.
This is a stub endpoint that will be implemented later.

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
    api_instance = autoaudit.WorkflowsApi(api_client)

    try:
        # List Workflows
        api_response = api_instance.list_workflows_api_v1_workflows_get()
        print("The response of WorkflowsApi->list_workflows_api_v1_workflows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->list_workflows_api_v1_workflows_get: %s\n" % e)
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

