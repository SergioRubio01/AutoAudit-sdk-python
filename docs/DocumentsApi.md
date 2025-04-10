# autoaudit.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_schema_api_v1_documents_schema_post**](DocumentsApi.md#create_document_schema_api_v1_documents_schema_post) | **POST** /api/v1/documents/schema | Create Document Schema
[**get_document_api_v1_documents_document_id_get**](DocumentsApi.md#get_document_api_v1_documents_document_id_get) | **GET** /api/v1/documents/{document_id} | Get Document
[**get_document_content_api_v1_documents_document_id_content_get**](DocumentsApi.md#get_document_content_api_v1_documents_document_id_content_get) | **GET** /api/v1/documents/{document_id}/content | Get Document Content
[**search_documents_api_v1_documents_get**](DocumentsApi.md#search_documents_api_v1_documents_get) | **GET** /api/v1/documents | Search Documents
[**update_document_api_v1_documents_document_id_patch**](DocumentsApi.md#update_document_api_v1_documents_document_id_patch) | **PATCH** /api/v1/documents/{document_id} | Update Document


# **create_document_schema_api_v1_documents_schema_post**
> object create_document_schema_api_v1_documents_schema_post(document_schema_request)

Create Document Schema

Create a document schema for parsing.

Args:
    schema_request: Schema request data
    current_user: Current authenticated user

Returns:
    Created schema information

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.document_schema_request import DocumentSchemaRequest
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
    api_instance = autoaudit.DocumentsApi(api_client)
    document_schema_request = autoaudit.DocumentSchemaRequest() # DocumentSchemaRequest | 

    try:
        # Create Document Schema
        api_response = api_instance.create_document_schema_api_v1_documents_schema_post(document_schema_request)
        print("The response of DocumentsApi->create_document_schema_api_v1_documents_schema_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_document_schema_api_v1_documents_schema_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_schema_request** | [**DocumentSchemaRequest**](DocumentSchemaRequest.md)|  | 

### Return type

**object**

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

# **get_document_api_v1_documents_document_id_get**
> DocumentResponse get_document_api_v1_documents_document_id_get(document_id)

Get Document

Get document by ID.

Args:
    document_id: Document ID
    current_user: Current authenticated user
    document_repository: Document repository

Returns:
    Document information

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.document_response import DocumentResponse
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
    api_instance = autoaudit.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | 

    try:
        # Get Document
        api_response = api_instance.get_document_api_v1_documents_document_id_get(document_id)
        print("The response of DocumentsApi->get_document_api_v1_documents_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_api_v1_documents_document_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

# **get_document_content_api_v1_documents_document_id_content_get**
> DocumentContentResponse get_document_content_api_v1_documents_document_id_content_get(document_id, base_storage_path)

Get Document Content

Get document content and extracted data.

Args:
    document_id: Document ID
    current_user: Current authenticated user
    document_repository: Document repository
    file_storage: File storage service
    document_service: Document service

Returns:
    Document content and extracted data

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.document_content_response import DocumentContentResponse
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
    api_instance = autoaudit.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | 
    base_storage_path = 'base_storage_path_example' # str | 

    try:
        # Get Document Content
        api_response = api_instance.get_document_content_api_v1_documents_document_id_content_get(document_id, base_storage_path)
        print("The response of DocumentsApi->get_document_content_api_v1_documents_document_id_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_content_api_v1_documents_document_id_content_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **base_storage_path** | **str**|  | 

### Return type

[**DocumentContentResponse**](DocumentContentResponse.md)

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

# **search_documents_api_v1_documents_get**
> DocumentListResponse search_documents_api_v1_documents_get(document_type=document_type, status=status, query=query, page=page, page_size=page_size)

Search Documents

Search for documents.

Args:
    document_type: Optional document type filter
    status: Optional status filter
    query: Optional search query
    page: Page number
    page_size: Page size
    current_user: Current authenticated user
    search_documents_use_case: Search documents use case

Returns:
    List of documents matching search criteria

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.document_list_response import DocumentListResponse
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
    api_instance = autoaudit.DocumentsApi(api_client)
    document_type = 'document_type_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    query = 'query_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)

    try:
        # Search Documents
        api_response = api_instance.search_documents_api_v1_documents_get(document_type=document_type, status=status, query=query, page=page, page_size=page_size)
        print("The response of DocumentsApi->search_documents_api_v1_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->search_documents_api_v1_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

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

# **update_document_api_v1_documents_document_id_patch**
> DocumentResponse update_document_api_v1_documents_document_id_patch(document_id, document_update_request)

Update Document

Update document metadata and status.

Args:
    document_id: Document ID
    update_data: Update data
    current_user: Current authenticated user
    document_repository: Document repository
    document_cache: Document cache

Returns:
    Updated document information

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.document_response import DocumentResponse
from autoaudit.models.document_update_request import DocumentUpdateRequest
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
    api_instance = autoaudit.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | 
    document_update_request = autoaudit.DocumentUpdateRequest() # DocumentUpdateRequest | 

    try:
        # Update Document
        api_response = api_instance.update_document_api_v1_documents_document_id_patch(document_id, document_update_request)
        print("The response of DocumentsApi->update_document_api_v1_documents_document_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->update_document_api_v1_documents_document_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**|  | 
 **document_update_request** | [**DocumentUpdateRequest**](DocumentUpdateRequest.md)|  | 

### Return type

[**DocumentResponse**](DocumentResponse.md)

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

