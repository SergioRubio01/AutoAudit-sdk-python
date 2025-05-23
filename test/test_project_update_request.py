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

from autoaudit.models.project_update_request import ProjectUpdateRequest

class TestProjectUpdateRequest(unittest.TestCase):
    """ProjectUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectUpdateRequest:
        """Test ProjectUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectUpdateRequest`
        """
        model = ProjectUpdateRequest()
        if include_optional:
            return ProjectUpdateRequest(
                name = '',
                status = '',
                project_type = '',
                description = '',
                modules = [
                    ''
                    ],
                selected_models = {
                    'key' : [
                        ''
                        ]
                    },
                selected_workflows = {
                    'key' : null
                    },
                settings = {
                    'key' : null
                    }
            )
        else:
            return ProjectUpdateRequest(
        )
        """

    def testProjectUpdateRequest(self):
        """Test ProjectUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
