# autoaudit.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_member_api_v1_projects_project_id_members_post**](ProjectsApi.md#add_project_member_api_v1_projects_project_id_members_post) | **POST** /api/v1/projects/{project_id}/members | Add Project Member
[**create_project_api_v1_projects_post**](ProjectsApi.md#create_project_api_v1_projects_post) | **POST** /api/v1/projects | Create Project
[**create_project_from_template_api_v1_projects_from_template_post**](ProjectsApi.md#create_project_from_template_api_v1_projects_from_template_post) | **POST** /api/v1/projects/from-template | Create Project From Template
[**delete_project_api_v1_projects_project_id_delete**](ProjectsApi.md#delete_project_api_v1_projects_project_id_delete) | **DELETE** /api/v1/projects/{project_id} | Delete Project
[**get_project_api_v1_projects_project_id_get**](ProjectsApi.md#get_project_api_v1_projects_project_id_get) | **GET** /api/v1/projects/{project_id} | Get Project
[**list_project_members_api_v1_projects_project_id_members_get**](ProjectsApi.md#list_project_members_api_v1_projects_project_id_members_get) | **GET** /api/v1/projects/{project_id}/members | List Project Members
[**list_projects_api_v1_projects_get**](ProjectsApi.md#list_projects_api_v1_projects_get) | **GET** /api/v1/projects | List Projects
[**remove_project_member_api_v1_projects_project_id_members_user_id_delete**](ProjectsApi.md#remove_project_member_api_v1_projects_project_id_members_user_id_delete) | **DELETE** /api/v1/projects/{project_id}/members/{user_id} | Remove Project Member
[**update_project_api_v1_projects_project_id_put**](ProjectsApi.md#update_project_api_v1_projects_project_id_put) | **PUT** /api/v1/projects/{project_id} | Update Project


# **add_project_member_api_v1_projects_project_id_members_post**
> ProjectMemberListResponse add_project_member_api_v1_projects_project_id_members_post(project_id, project_member_add_request)

Add Project Member

Add a member to a project.

This endpoint allows project owners to add members to their projects.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_member_add_request import ProjectMemberAddRequest
from autoaudit.models.project_member_list_response import ProjectMemberListResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
    project_member_add_request = autoaudit.ProjectMemberAddRequest() # ProjectMemberAddRequest | 

    try:
        # Add Project Member
        api_response = api_instance.add_project_member_api_v1_projects_project_id_members_post(project_id, project_member_add_request)
        print("The response of ProjectsApi->add_project_member_api_v1_projects_project_id_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_project_member_api_v1_projects_project_id_members_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project | 
 **project_member_add_request** | [**ProjectMemberAddRequest**](ProjectMemberAddRequest.md)|  | 

### Return type

[**ProjectMemberListResponse**](ProjectMemberListResponse.md)

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

# **create_project_api_v1_projects_post**
> ProjectResponse create_project_api_v1_projects_post(project_create_request)

Create Project

Create a new project.

This endpoint allows users to create a new project with the specified details.
Projects serve as containers for workflows, documents, and other resources.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_create_request import ProjectCreateRequest
from autoaudit.models.project_response import ProjectResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_create_request = autoaudit.ProjectCreateRequest() # ProjectCreateRequest | 

    try:
        # Create Project
        api_response = api_instance.create_project_api_v1_projects_post(project_create_request)
        print("The response of ProjectsApi->create_project_api_v1_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_api_v1_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_request** | [**ProjectCreateRequest**](ProjectCreateRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **create_project_from_template_api_v1_projects_from_template_post**
> ProjectResponse create_project_from_template_api_v1_projects_from_template_post(project_create_from_template_request)

Create Project From Template

Create a new project from a template.

This endpoint allows users to create a new project based on a project template.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_create_from_template_request import ProjectCreateFromTemplateRequest
from autoaudit.models.project_response import ProjectResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_create_from_template_request = autoaudit.ProjectCreateFromTemplateRequest() # ProjectCreateFromTemplateRequest | 

    try:
        # Create Project From Template
        api_response = api_instance.create_project_from_template_api_v1_projects_from_template_post(project_create_from_template_request)
        print("The response of ProjectsApi->create_project_from_template_api_v1_projects_from_template_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project_from_template_api_v1_projects_from_template_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_from_template_request** | [**ProjectCreateFromTemplateRequest**](ProjectCreateFromTemplateRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **delete_project_api_v1_projects_project_id_delete**
> delete_project_api_v1_projects_project_id_delete(project_id)

Delete Project

Delete a project.

This endpoint allows users to delete an existing project.

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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project to delete

    try:
        # Delete Project
        api_instance.delete_project_api_v1_projects_project_id_delete(project_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_api_v1_projects_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project to delete | 

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

# **get_project_api_v1_projects_project_id_get**
> ProjectResponse get_project_api_v1_projects_project_id_get(project_id)

Get Project

Get a single project by ID.

This endpoint retrieves the details of a specific project.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_response import ProjectResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project to retrieve

    try:
        # Get Project
        api_response = api_instance.get_project_api_v1_projects_project_id_get(project_id)
        print("The response of ProjectsApi->get_project_api_v1_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_api_v1_projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project to retrieve | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **list_project_members_api_v1_projects_project_id_members_get**
> ProjectMemberListResponse list_project_members_api_v1_projects_project_id_members_get(project_id)

List Project Members

List members of a project.

This endpoint allows users to list all members of a project.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_member_list_response import ProjectMemberListResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project

    try:
        # List Project Members
        api_response = api_instance.list_project_members_api_v1_projects_project_id_members_get(project_id)
        print("The response of ProjectsApi->list_project_members_api_v1_projects_project_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->list_project_members_api_v1_projects_project_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project | 

### Return type

[**ProjectMemberListResponse**](ProjectMemberListResponse.md)

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

# **list_projects_api_v1_projects_get**
> List[ProjectResponse] list_projects_api_v1_projects_get(organization_id=organization_id, search=search, limit=limit, offset=offset)

List Projects

List projects.

This endpoint retrieves a list of projects that the current user has access to.
Results can be filtered by organization and search query.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_response import ProjectResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    organization_id = 'organization_id_example' # str | Filter by organization ID (optional)
    search = 'search_example' # str | Search query (optional)
    limit = 10 # int | Number of results to return (optional) (default to 10)
    offset = 0 # int | Number of results to skip (optional) (default to 0)

    try:
        # List Projects
        api_response = api_instance.list_projects_api_v1_projects_get(organization_id=organization_id, search=search, limit=limit, offset=offset)
        print("The response of ProjectsApi->list_projects_api_v1_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->list_projects_api_v1_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Filter by organization ID | [optional] 
 **search** | **str**| Search query | [optional] 
 **limit** | **int**| Number of results to return | [optional] [default to 10]
 **offset** | **int**| Number of results to skip | [optional] [default to 0]

### Return type

[**List[ProjectResponse]**](ProjectResponse.md)

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

# **remove_project_member_api_v1_projects_project_id_members_user_id_delete**
> ProjectMemberListResponse remove_project_member_api_v1_projects_project_id_members_user_id_delete(project_id, user_id)

Remove Project Member

Remove a member from a project.

This endpoint allows project owners to remove members from their projects.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_member_list_response import ProjectMemberListResponse
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project
    user_id = 'user_id_example' # str | ID of the user to remove

    try:
        # Remove Project Member
        api_response = api_instance.remove_project_member_api_v1_projects_project_id_members_user_id_delete(project_id, user_id)
        print("The response of ProjectsApi->remove_project_member_api_v1_projects_project_id_members_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_project_member_api_v1_projects_project_id_members_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project | 
 **user_id** | **str**| ID of the user to remove | 

### Return type

[**ProjectMemberListResponse**](ProjectMemberListResponse.md)

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

# **update_project_api_v1_projects_project_id_put**
> ProjectResponse update_project_api_v1_projects_project_id_put(project_id, project_update_request)

Update Project

Update a project.

This endpoint allows users to update the details of an existing project.

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.project_response import ProjectResponse
from autoaudit.models.project_update_request import ProjectUpdateRequest
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
    api_instance = autoaudit.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | ID of the project to update
    project_update_request = autoaudit.ProjectUpdateRequest() # ProjectUpdateRequest | 

    try:
        # Update Project
        api_response = api_instance.update_project_api_v1_projects_project_id_put(project_id, project_update_request)
        print("The response of ProjectsApi->update_project_api_v1_projects_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project_api_v1_projects_project_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| ID of the project to update | 
 **project_update_request** | [**ProjectUpdateRequest**](ProjectUpdateRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

