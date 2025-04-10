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

from autoaudit.models.agent_tool_response import AgentToolResponse

class TestAgentToolResponse(unittest.TestCase):
    """AgentToolResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentToolResponse:
        """Test AgentToolResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentToolResponse`
        """
        model = AgentToolResponse()
        if include_optional:
            return AgentToolResponse(
                tool_id = '',
                name = '',
                description = '',
                parameters = {
                    'key' : null
                    }
            )
        else:
            return AgentToolResponse(
                tool_id = '',
                name = '',
                description = '',
        )
        """

    def testAgentToolResponse(self):
        """Test AgentToolResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
