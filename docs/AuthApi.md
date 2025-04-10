# autoaudit.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_google_oauth_url_api_v1_oauth_google_get**](AuthApi.md#get_google_oauth_url_api_v1_oauth_google_get) | **GET** /api/v1/oauth/google | Get Google Oauth Url
[**get_microsoft_oauth_url_api_v1_oauth_microsoft_get**](AuthApi.md#get_microsoft_oauth_url_api_v1_oauth_microsoft_get) | **GET** /api/v1/oauth/microsoft | Get Microsoft Oauth Url
[**get_user_info_api_v1_auth_me_get**](AuthApi.md#get_user_info_api_v1_auth_me_get) | **GET** /api/v1/auth/me | Get User Info
[**google_callback_api_v1_v1_auth_callback_google_get**](AuthApi.md#google_callback_api_v1_v1_auth_callback_google_get) | **GET** /api/v1/v1/auth/callback/google | Google Callback
[**google_post_callback_api_v1_v1_auth_callback_google_post**](AuthApi.md#google_post_callback_api_v1_v1_auth_callback_google_post) | **POST** /api/v1/v1/auth/callback/google | Google Post Callback
[**login_api_v1_auth_login_post**](AuthApi.md#login_api_v1_auth_login_post) | **POST** /api/v1/auth/login | Login
[**login_for_access_token_api_v1_auth_token_post**](AuthApi.md#login_for_access_token_api_v1_auth_token_post) | **POST** /api/v1/auth/token | Login For Access Token
[**microsoft_callback_api_v1_v1_auth_callback_microsoft_get**](AuthApi.md#microsoft_callback_api_v1_v1_auth_callback_microsoft_get) | **GET** /api/v1/v1/auth/callback/microsoft | Microsoft Callback
[**microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post**](AuthApi.md#microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post) | **POST** /api/v1/v1/auth/callback/microsoft | Microsoft Post Callback
[**oauth_authorize_api_v1_auth_oauth_provider_get**](AuthApi.md#oauth_authorize_api_v1_auth_oauth_provider_get) | **GET** /api/v1/auth/oauth/{provider} | Oauth Authorize
[**oauth_login_api_v1_auth_oauth_post**](AuthApi.md#oauth_login_api_v1_auth_oauth_post) | **POST** /api/v1/auth/oauth | Oauth Login
[**refresh_access_token_api_v1_auth_refresh_post**](AuthApi.md#refresh_access_token_api_v1_auth_refresh_post) | **POST** /api/v1/auth/refresh | Refresh Access Token


# **get_google_oauth_url_api_v1_oauth_google_get**
> object get_google_oauth_url_api_v1_oauth_google_get()

Get Google Oauth Url

Generate Google OAuth authorization URL

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
    api_instance = autoaudit.AuthApi(api_client)

    try:
        # Get Google Oauth Url
        api_response = api_instance.get_google_oauth_url_api_v1_oauth_google_get()
        print("The response of AuthApi->get_google_oauth_url_api_v1_oauth_google_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_google_oauth_url_api_v1_oauth_google_get: %s\n" % e)
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

# **get_microsoft_oauth_url_api_v1_oauth_microsoft_get**
> object get_microsoft_oauth_url_api_v1_oauth_microsoft_get()

Get Microsoft Oauth Url

Generate Microsoft OAuth authorization URL

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
    api_instance = autoaudit.AuthApi(api_client)

    try:
        # Get Microsoft Oauth Url
        api_response = api_instance.get_microsoft_oauth_url_api_v1_oauth_microsoft_get()
        print("The response of AuthApi->get_microsoft_oauth_url_api_v1_oauth_microsoft_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_microsoft_oauth_url_api_v1_oauth_microsoft_get: %s\n" % e)
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

# **get_user_info_api_v1_auth_me_get**
> UserResponse get_user_info_api_v1_auth_me_get()

Get User Info

Get current user info

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.user_response import UserResponse
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
    api_instance = autoaudit.AuthApi(api_client)

    try:
        # Get User Info
        api_response = api_instance.get_user_info_api_v1_auth_me_get()
        print("The response of AuthApi->get_user_info_api_v1_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_user_info_api_v1_auth_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_callback_api_v1_v1_auth_callback_google_get**
> object google_callback_api_v1_v1_auth_callback_google_get(code=code)

Google Callback

Handle Google OAuth callback
- Validates the authorization code
- Processes user information
- Redirects back to frontend with token

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
    api_instance = autoaudit.AuthApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        # Google Callback
        api_response = api_instance.google_callback_api_v1_v1_auth_callback_google_get(code=code)
        print("The response of AuthApi->google_callback_api_v1_v1_auth_callback_google_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->google_callback_api_v1_v1_auth_callback_google_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 

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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_post_callback_api_v1_v1_auth_callback_google_post**
> object google_post_callback_api_v1_v1_auth_callback_google_post(o_auth_code_request)

Google Post Callback

Handle Google OAuth callback via POST request
- Extracts code from request body
- Validates the authorization code
- Processes user information
- Returns token in JSON response

### Example


```python
import autoaudit
from autoaudit.models.o_auth_code_request import OAuthCodeRequest
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
    api_instance = autoaudit.AuthApi(api_client)
    o_auth_code_request = autoaudit.OAuthCodeRequest() # OAuthCodeRequest | 

    try:
        # Google Post Callback
        api_response = api_instance.google_post_callback_api_v1_v1_auth_callback_google_post(o_auth_code_request)
        print("The response of AuthApi->google_post_callback_api_v1_v1_auth_callback_google_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->google_post_callback_api_v1_v1_auth_callback_google_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_code_request** | [**OAuthCodeRequest**](OAuthCodeRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_api_v1_auth_login_post**
> Token login_api_v1_auth_login_post(login_input)

Login

Login with email and password

### Example


```python
import autoaudit
from autoaudit.models.login_input import LoginInput
from autoaudit.models.token import Token
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
    api_instance = autoaudit.AuthApi(api_client)
    login_input = autoaudit.LoginInput() # LoginInput | 

    try:
        # Login
        api_response = api_instance.login_api_v1_auth_login_post(login_input)
        print("The response of AuthApi->login_api_v1_auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_api_v1_auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_input** | [**LoginInput**](LoginInput.md)|  | 

### Return type

[**Token**](Token.md)

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

# **login_for_access_token_api_v1_auth_token_post**
> Token login_for_access_token_api_v1_auth_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login For Access Token

OAuth2 compatible token login, get an access token for future requests

### Example


```python
import autoaudit
from autoaudit.models.token import Token
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
    api_instance = autoaudit.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login For Access Token
        api_response = api_instance.login_for_access_token_api_v1_auth_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->login_for_access_token_api_v1_auth_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->login_for_access_token_api_v1_auth_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **microsoft_callback_api_v1_v1_auth_callback_microsoft_get**
> object microsoft_callback_api_v1_v1_auth_callback_microsoft_get(code=code)

Microsoft Callback

Handle Microsoft OAuth callback
- Validates the authorization code
- Processes user information
- Redirects back to frontend with token

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
    api_instance = autoaudit.AuthApi(api_client)
    code = 'code_example' # str |  (optional)

    try:
        # Microsoft Callback
        api_response = api_instance.microsoft_callback_api_v1_v1_auth_callback_microsoft_get(code=code)
        print("The response of AuthApi->microsoft_callback_api_v1_v1_auth_callback_microsoft_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->microsoft_callback_api_v1_v1_auth_callback_microsoft_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 

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
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post**
> object microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post(o_auth_code_request)

Microsoft Post Callback

Handle Microsoft OAuth callback via POST request
- Extracts code from request body
- Validates the authorization code
- Processes user information
- Returns token in JSON response

### Example


```python
import autoaudit
from autoaudit.models.o_auth_code_request import OAuthCodeRequest
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
    api_instance = autoaudit.AuthApi(api_client)
    o_auth_code_request = autoaudit.OAuthCodeRequest() # OAuthCodeRequest | 

    try:
        # Microsoft Post Callback
        api_response = api_instance.microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post(o_auth_code_request)
        print("The response of AuthApi->microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->microsoft_post_callback_api_v1_v1_auth_callback_microsoft_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_code_request** | [**OAuthCodeRequest**](OAuthCodeRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_authorize_api_v1_auth_oauth_provider_get**
> Token oauth_authorize_api_v1_auth_oauth_provider_get(provider, redirect_uri)

Oauth Authorize

Generate OAuth authorization URL and redirect to it

### Example


```python
import autoaudit
from autoaudit.models.token import Token
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
    api_instance = autoaudit.AuthApi(api_client)
    provider = 'provider_example' # str | 
    redirect_uri = 'redirect_uri_example' # str | 

    try:
        # Oauth Authorize
        api_response = api_instance.oauth_authorize_api_v1_auth_oauth_provider_get(provider, redirect_uri)
        print("The response of AuthApi->oauth_authorize_api_v1_auth_oauth_provider_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_authorize_api_v1_auth_oauth_provider_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **redirect_uri** | **str**|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_login_api_v1_auth_oauth_post**
> Token oauth_login_api_v1_auth_oauth_post(o_auth_login_input)

Oauth Login

Login with OAuth token

### Example


```python
import autoaudit
from autoaudit.models.o_auth_login_input import OAuthLoginInput
from autoaudit.models.token import Token
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
    api_instance = autoaudit.AuthApi(api_client)
    o_auth_login_input = autoaudit.OAuthLoginInput() # OAuthLoginInput | 

    try:
        # Oauth Login
        api_response = api_instance.oauth_login_api_v1_auth_oauth_post(o_auth_login_input)
        print("The response of AuthApi->oauth_login_api_v1_auth_oauth_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->oauth_login_api_v1_auth_oauth_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_login_input** | [**OAuthLoginInput**](OAuthLoginInput.md)|  | 

### Return type

[**Token**](Token.md)

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

# **refresh_access_token_api_v1_auth_refresh_post**
> Token refresh_access_token_api_v1_auth_refresh_post(refresh_input)

Refresh Access Token

Refresh access token

### Example


```python
import autoaudit
from autoaudit.models.refresh_input import RefreshInput
from autoaudit.models.token import Token
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
    api_instance = autoaudit.AuthApi(api_client)
    refresh_input = autoaudit.RefreshInput() # RefreshInput | 

    try:
        # Refresh Access Token
        api_response = api_instance.refresh_access_token_api_v1_auth_refresh_post(refresh_input)
        print("The response of AuthApi->refresh_access_token_api_v1_auth_refresh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->refresh_access_token_api_v1_auth_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_input** | [**RefreshInput**](RefreshInput.md)|  | 

### Return type

[**Token**](Token.md)

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

