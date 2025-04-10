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

from autoaudit.models.document_update_request import DocumentUpdateRequest

class TestDocumentUpdateRequest(unittest.TestCase):
    """DocumentUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentUpdateRequest:
        """Test DocumentUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentUpdateRequest`
        """
        model = DocumentUpdateRequest()
        if include_optional:
            return DocumentUpdateRequest(
                name = '',
                description = '',
                status = '',
                metadata = {
                    'key' : null
                    }
            )
        else:
            return DocumentUpdateRequest(
        )
        """

    def testDocumentUpdateRequest(self):
        """Test DocumentUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
