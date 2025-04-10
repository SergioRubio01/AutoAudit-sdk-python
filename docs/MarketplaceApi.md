# autoaudit.MarketplaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post**](MarketplaceApi.md#monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post) | **POST** /api/v1/marketplace/placsp/monitor | Monitor PLACSP for new tenders
[**verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post**](MarketplaceApi.md#verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post) | **POST** /api/v1/marketplace/auditor-profiles/{auditor_profile_id}/verify-credentials | Verify auditor credentials


# **monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post**
> MonitorPLACSPTendersResponse monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post(monitor_placsp_tenders_request)

Monitor PLACSP for new tenders

Monitor the Spanish Public Sector Procurement Platform (PLACSP) for new audit tenders

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.monitor_placsp_tenders_request import MonitorPLACSPTendersRequest
from autoaudit.models.monitor_placsp_tenders_response import MonitorPLACSPTendersResponse
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
    api_instance = autoaudit.MarketplaceApi(api_client)
    monitor_placsp_tenders_request = autoaudit.MonitorPLACSPTendersRequest() # MonitorPLACSPTendersRequest | 

    try:
        # Monitor PLACSP for new tenders
        api_response = api_instance.monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post(monitor_placsp_tenders_request)
        print("The response of MarketplaceApi->monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->monitor_placsp_tenders_api_v1_marketplace_placsp_monitor_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **monitor_placsp_tenders_request** | [**MonitorPLACSPTendersRequest**](MonitorPLACSPTendersRequest.md)|  | 

### Return type

[**MonitorPLACSPTendersResponse**](MonitorPLACSPTendersResponse.md)

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

# **verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post**
> VerifyAuditorCredentialsResponse verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post(auditor_profile_id, verify_auditor_credentials_request)

Verify auditor credentials

Verify auditor credentials like ROAC certification

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import autoaudit
from autoaudit.models.verify_auditor_credentials_request import VerifyAuditorCredentialsRequest
from autoaudit.models.verify_auditor_credentials_response import VerifyAuditorCredentialsResponse
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
    api_instance = autoaudit.MarketplaceApi(api_client)
    auditor_profile_id = 'auditor_profile_id_example' # str | ID of the auditor profile
    verify_auditor_credentials_request = autoaudit.VerifyAuditorCredentialsRequest() # VerifyAuditorCredentialsRequest | 

    try:
        # Verify auditor credentials
        api_response = api_instance.verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post(auditor_profile_id, verify_auditor_credentials_request)
        print("The response of MarketplaceApi->verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketplaceApi->verify_auditor_credentials_api_v1_marketplace_auditor_profiles_auditor_profile_id_verify_credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auditor_profile_id** | **str**| ID of the auditor profile | 
 **verify_auditor_credentials_request** | [**VerifyAuditorCredentialsRequest**](VerifyAuditorCredentialsRequest.md)|  | 

### Return type

[**VerifyAuditorCredentialsResponse**](VerifyAuditorCredentialsResponse.md)

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

