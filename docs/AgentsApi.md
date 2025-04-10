# autoaudit.AgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_agent_api_v1_agents_agent_id_activate_post**](AgentsApi.md#activate_agent_api_v1_agents_agent_id_activate_post) | **POST** /api/v1/agents/{agent_id}/activate | Activate Agent
[**create_agent_api_v1_agents_post**](AgentsApi.md#create_agent_api_v1_agents_post) | **POST** /api/v1/agents | Create Agent
[**create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post**](AgentsApi.md#create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post) | **POST** /api/v1/agents/{agent_id}/create-workflow | Create Workflow With Agent
[**execute_agent_command_api_v1_agents_agent_id_command_post**](AgentsApi.md#execute_agent_command_api_v1_agents_agent_id_command_post) | **POST** /api/v1/agents/{agent_id}/command | Execute Agent Command
[**get_agent_api_v1_agents_agent_id_get**](AgentsApi.md#get_agent_api_v1_agents_agent_id_get) | **GET** /api/v1/agents/{agent_id} | Get Agent
[**list_agents_api_v1_agents_get**](AgentsApi.md#list_agents_api_v1_agents_get) | **GET** /api/v1/agents | List Agents


# **activate_agent_api_v1_agents_agent_id_activate_post**
> AutoauditInterfacesApiV1AgentsAgentResponse activate_agent_api_v1_agents_agent_id_activate_post(agent_id)

Activate Agent

Activate an agent.

This endpoint activates an existing agent, which must be in INACTIVE status.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_agents_agent_response import AutoauditInterfacesApiV1AgentsAgentResponse
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
    api_instance = autoaudit.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | ID of the agent to activate

    try:
        # Activate Agent
        api_response = api_instance.activate_agent_api_v1_agents_agent_id_activate_post(agent_id)
        print("The response of AgentsApi->activate_agent_api_v1_agents_agent_id_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->activate_agent_api_v1_agents_agent_id_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| ID of the agent to activate | 

### Return type

[**AutoauditInterfacesApiV1AgentsAgentResponse**](AutoauditInterfacesApiV1AgentsAgentResponse.md)

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

# **create_agent_api_v1_agents_post**
> AutoauditInterfacesApiV1AgentsAgentResponse create_agent_api_v1_agents_post(autoaudit_interfaces_api_v1_agents_create_agent_request)

Create Agent

Create a new agent.

This endpoint allows users to create a new agent with the specified details.
If the agent type is MULTITOOL, it will be initialized with advanced capabilities.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_agents_agent_response import AutoauditInterfacesApiV1AgentsAgentResponse
from autoaudit.models.autoaudit_interfaces_api_v1_agents_create_agent_request import AutoauditInterfacesApiV1AgentsCreateAgentRequest
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
    api_instance = autoaudit.AgentsApi(api_client)
    autoaudit_interfaces_api_v1_agents_create_agent_request = autoaudit.AutoauditInterfacesApiV1AgentsCreateAgentRequest() # AutoauditInterfacesApiV1AgentsCreateAgentRequest | 

    try:
        # Create Agent
        api_response = api_instance.create_agent_api_v1_agents_post(autoaudit_interfaces_api_v1_agents_create_agent_request)
        print("The response of AgentsApi->create_agent_api_v1_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_agent_api_v1_agents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **autoaudit_interfaces_api_v1_agents_create_agent_request** | [**AutoauditInterfacesApiV1AgentsCreateAgentRequest**](AutoauditInterfacesApiV1AgentsCreateAgentRequest.md)|  | 

### Return type

[**AutoauditInterfacesApiV1AgentsAgentResponse**](AutoauditInterfacesApiV1AgentsAgentResponse.md)

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

# **create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post**
> WorkflowResponse create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post(agent_id, create_workflow_request)

Create Workflow With Agent

Create a workflow using an agent.

This endpoint allows users to create a workflow using an agent,
by providing a name, description, and requirements.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.create_workflow_request import CreateWorkflowRequest
from autoaudit.models.workflow_response import WorkflowResponse
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
    api_instance = autoaudit.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | ID of the agent to use
    create_workflow_request = autoaudit.CreateWorkflowRequest() # CreateWorkflowRequest | 

    try:
        # Create Workflow With Agent
        api_response = api_instance.create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post(agent_id, create_workflow_request)
        print("The response of AgentsApi->create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->create_workflow_with_agent_api_v1_agents_agent_id_create_workflow_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| ID of the agent to use | 
 **create_workflow_request** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)|  | 

### Return type

[**WorkflowResponse**](WorkflowResponse.md)

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

# **execute_agent_command_api_v1_agents_agent_id_command_post**
> AgentCommandResponse execute_agent_command_api_v1_agents_agent_id_command_post(agent_id, agent_command_request)

Execute Agent Command

Execute a command with an agent.

This endpoint allows users to send commands to an agent and receive responses.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.agent_command_request import AgentCommandRequest
from autoaudit.models.agent_command_response import AgentCommandResponse
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
    api_instance = autoaudit.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | ID of the agent to use
    agent_command_request = autoaudit.AgentCommandRequest() # AgentCommandRequest | 

    try:
        # Execute Agent Command
        api_response = api_instance.execute_agent_command_api_v1_agents_agent_id_command_post(agent_id, agent_command_request)
        print("The response of AgentsApi->execute_agent_command_api_v1_agents_agent_id_command_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->execute_agent_command_api_v1_agents_agent_id_command_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| ID of the agent to use | 
 **agent_command_request** | [**AgentCommandRequest**](AgentCommandRequest.md)|  | 

### Return type

[**AgentCommandResponse**](AgentCommandResponse.md)

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

# **get_agent_api_v1_agents_agent_id_get**
> AutoauditInterfacesApiV1AgentsAgentResponse get_agent_api_v1_agents_agent_id_get(agent_id)

Get Agent

Get a single agent by ID.

This endpoint retrieves the details of a specific agent.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_agents_agent_response import AutoauditInterfacesApiV1AgentsAgentResponse
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
    api_instance = autoaudit.AgentsApi(api_client)
    agent_id = 'agent_id_example' # str | ID of the agent to retrieve

    try:
        # Get Agent
        api_response = api_instance.get_agent_api_v1_agents_agent_id_get(agent_id)
        print("The response of AgentsApi->get_agent_api_v1_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_api_v1_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**| ID of the agent to retrieve | 

### Return type

[**AutoauditInterfacesApiV1AgentsAgentResponse**](AutoauditInterfacesApiV1AgentsAgentResponse.md)

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

# **list_agents_api_v1_agents_get**
> List[AutoauditInterfacesApiV1AgentsAgentResponse] list_agents_api_v1_agents_get(project_id=project_id, agent_type=agent_type)

List Agents

List agents.

This endpoint retrieves a list of agents that the current user has access to.
Results can be filtered by project ID and agent type.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.autoaudit_interfaces_api_v1_agents_agent_response import AutoauditInterfacesApiV1AgentsAgentResponse
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
    api_instance = autoaudit.AgentsApi(api_client)
    project_id = 'project_id_example' # str | Filter by project ID (optional)
    agent_type = 'agent_type_example' # str | Filter by agent type (optional)

    try:
        # List Agents
        api_response = api_instance.list_agents_api_v1_agents_get(project_id=project_id, agent_type=agent_type)
        print("The response of AgentsApi->list_agents_api_v1_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->list_agents_api_v1_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter by project ID | [optional] 
 **agent_type** | **str**| Filter by agent type | [optional] 

### Return type

[**List[AutoauditInterfacesApiV1AgentsAgentResponse]**](AutoauditInterfacesApiV1AgentsAgentResponse.md)

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

