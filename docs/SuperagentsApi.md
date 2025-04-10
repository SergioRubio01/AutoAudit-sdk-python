# autoaudit.SuperagentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_api_v1_superagents_post**](SuperagentsApi.md#create_agent_api_v1_superagents_post) | **POST** /api/v1/superagents | Create Agent
[**delete_agent_api_v1_superagents_agent_id_delete**](SuperagentsApi.md#delete_agent_api_v1_superagents_agent_id_delete) | **DELETE** /api/v1/superagents/{agent_id} | Delete Agent
[**get_agent_api_v1_superagents_agent_id_get**](SuperagentsApi.md#get_agent_api_v1_superagents_agent_id_get) | **GET** /api/v1/superagents/{agent_id} | Get Agent
[**list_agents_api_v1_superagents_get**](SuperagentsApi.md#list_agents_api_v1_superagents_get) | **GET** /api/v1/superagents | List Agents
[**update_agent_api_v1_superagents_agent_id_patch**](SuperagentsApi.md#update_agent_api_v1_superagents_agent_id_patch) | **PATCH** /api/v1/superagents/{agent_id} | Update Agent


# **create_agent_api_v1_superagents_post**
> AutoauditInterfacesApiV1SuperagentsAgentResponse create_agent_api_v1_superagents_post(autoaudit_interfaces_api_v1_superagents_create_agent_request)

Create Agent

Create a new superagent.

Args:
    create_request: Agent creation data
    current_user: Current authenticated user
    create_agent_use_case: Create agent use case

Returns:
    Created agent information

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_agent_response import AutoauditInterfacesApiV1SuperagentsAgentResponse
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_create_agent_request import AutoauditInterfacesApiV1SuperagentsCreateAgentRequest
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SuperagentsApi(api_client)
    autoaudit_interfaces_api_v1_superagents_create_agent_request = autoaudit.AutoauditInterfacesApiV1SuperagentsCreateAgentRequest() # AutoauditInterfacesApiV1SuperagentsCreateAgentRequest | 

    try:
        # Create Agent
        api_response = api_instance.create_agent_api_v1_superagents_post(autoaudit_interfaces_api_v1_superagents_create_agent_request)
        print("The response of SuperagentsApi->create_agent_api_v1_superagents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperagentsApi->create_agent_api_v1_superagents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoaudit_interfaces_api_v1_superagents_create_agent_request** | [**AutoauditInterfacesApiV1SuperagentsCreateAgentRequest**](AutoauditInterfacesApiV1SuperagentsCreateAgentRequest.md)|  | 

### Return type

[**AutoauditInterfacesApiV1SuperagentsAgentResponse**](AutoauditInterfacesApiV1SuperagentsAgentResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_api_v1_superagents_agent_id_delete**
> delete_agent_api_v1_superagents_agent_id_delete(agent_id)

Delete Agent

Delete an agent.

Args:
    agent_id: Agent ID
    current_user: Current authenticated user
    delete_agent_use_case: Delete agent use case

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SuperagentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Delete Agent
        api_instance.delete_agent_api_v1_superagents_agent_id_delete(agent_id)
    except Exception as e:
        print("Exception when calling SuperagentsApi->delete_agent_api_v1_superagents_agent_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_api_v1_superagents_agent_id_get**
> AutoauditInterfacesApiV1SuperagentsAgentResponse get_agent_api_v1_superagents_agent_id_get(agent_id)

Get Agent

Get agent by ID.

#
#     Args:
#         agent_id: Agent ID
#         current_user: Current authenticated user
#         get_agent_use_case: Get agent use case

#
#     Returns:
#         Agent information
#

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_agent_response import AutoauditInterfacesApiV1SuperagentsAgentResponse
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SuperagentsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent
        api_response = api_instance.get_agent_api_v1_superagents_agent_id_get(agent_id)
        print("The response of SuperagentsApi->get_agent_api_v1_superagents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperagentsApi->get_agent_api_v1_superagents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**AutoauditInterfacesApiV1SuperagentsAgentResponse**](AutoauditInterfacesApiV1SuperagentsAgentResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents_api_v1_superagents_get**
> AgentListResponse list_agents_api_v1_superagents_get(status=status, page=page, page_size=page_size)

List Agents

List agents for the current organization.

Args:
    status: Optional status filter
    page: Page number
    page_size: Page size
    current_user: Current authenticated user
    list_agents_use_case: List agents use case

Returns:
    List of agents

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.agent_list_response import AgentListResponse
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SuperagentsApi(api_client)
    status = 'status_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)

    try:
        # List Agents
        api_response = api_instance.list_agents_api_v1_superagents_get(status=status, page=page, page_size=page_size)
        print("The response of SuperagentsApi->list_agents_api_v1_superagents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperagentsApi->list_agents_api_v1_superagents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**AgentListResponse**](AgentListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_api_v1_superagents_agent_id_patch**
> AutoauditInterfacesApiV1SuperagentsAgentResponse update_agent_api_v1_superagents_agent_id_patch(agent_id, update_agent_request)

Update Agent

Update agent details.

#
#     Args:#
        agent_id: Agent ID
#         update_data: Update data
#         current_user: Current authenticated user
#         update_agent_use_case: Update agent use case
#         get_agent_use_case: Get agent use case

#
#     Returns:
#         Updated agent information
#

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_superagents_agent_response import AutoauditInterfacesApiV1SuperagentsAgentResponse
from autoaudit.models.update_agent_request import UpdateAgentRequest
from autoaudit.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = autoaudit.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with autoaudit.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autoaudit.SuperagentsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    update_agent_request = autoaudit.UpdateAgentRequest() # UpdateAgentRequest | 

    try:
        # Update Agent
        api_response = api_instance.update_agent_api_v1_superagents_agent_id_patch(agent_id, update_agent_request)
        print("The response of SuperagentsApi->update_agent_api_v1_superagents_agent_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuperagentsApi->update_agent_api_v1_superagents_agent_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **update_agent_request** | [**UpdateAgentRequest**](UpdateAgentRequest.md)|  | 

### Return type

[**AutoauditInterfacesApiV1SuperagentsAgentResponse**](AutoauditInterfacesApiV1SuperagentsAgentResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

