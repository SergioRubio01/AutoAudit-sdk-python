# coding: utf-8

"""
    AutoAudit API

    API for AutoAudit

    The version of the OpenAPI document: 1.0.0
    Contact: support@autoaudit.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from autoaudit.models.agent_list_response import AgentListResponse

class TestAgentListResponse(unittest.TestCase):
    """AgentListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentListResponse:
        """Test AgentListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentListResponse`
        """
        model = AgentListResponse()
        if include_optional:
            return AgentListResponse(
                agents = [
                    autoaudit.models.agent_response.AgentResponse(
                        id = '', 
                        name = '', 
                        description = '', 
                        capabilities = [
                            autoaudit.models.agent_capability_response.AgentCapabilityResponse(
                                id = '', 
                                name = '', 
                                description = '', 
                                parameters = {
                                    'key' : null
                                    }, 
                                category = '', 
                                execution_tier = '', )
                            ], 
                        tools = [
                            autoaudit.models.agent_tool_response.AgentToolResponse(
                                tool_id = '', 
                                name = '', 
                                description = '', )
                            ], 
                        llm_id = '', 
                        organization_id = '', 
                        creator_id = '', 
                        status = '', 
                        execution_tier = '', 
                        max_iterations = 56, 
                        created_at = '', 
                        updated_at = '', 
                        last_execution_at = '', 
                        execution_count = 56, 
                        metadata = {
                            'key' : null
                            }, )
                    ],
                total = 56,
                page = 56,
                page_size = 56
            )
        else:
            return AgentListResponse(
                agents = [
                    autoaudit.models.agent_response.AgentResponse(
                        id = '', 
                        name = '', 
                        description = '', 
                        capabilities = [
                            autoaudit.models.agent_capability_response.AgentCapabilityResponse(
                                id = '', 
                                name = '', 
                                description = '', 
                                parameters = {
                                    'key' : null
                                    }, 
                                category = '', 
                                execution_tier = '', )
                            ], 
                        tools = [
                            autoaudit.models.agent_tool_response.AgentToolResponse(
                                tool_id = '', 
                                name = '', 
                                description = '', )
                            ], 
                        llm_id = '', 
                        organization_id = '', 
                        creator_id = '', 
                        status = '', 
                        execution_tier = '', 
                        max_iterations = 56, 
                        created_at = '', 
                        updated_at = '', 
                        last_execution_at = '', 
                        execution_count = 56, 
                        metadata = {
                            'key' : null
                            }, )
                    ],
                total = 56,
                page = 56,
                page_size = 56,
        )
        """

    def testAgentListResponse(self):
        """Test AgentListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
