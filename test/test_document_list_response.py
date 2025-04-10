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

from autoaudit.models.document_list_response import DocumentListResponse

class TestDocumentListResponse(unittest.TestCase):
    """DocumentListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentListResponse:
        """Test DocumentListResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentListResponse`
        """
        model = DocumentListResponse()
        if include_optional:
            return DocumentListResponse(
                documents = [
                    autoaudit.models.document_response.DocumentResponse(
                        id = '', 
                        name = '', 
                        description = '', 
                        document_type = '', 
                        status = '', 
                        file_path = '', 
                        file_type = '', 
                        file_size = 56, 
                        created_at = '', 
                        updated_at = '', 
                        processed_at = '', 
                        metadata = {
                            'key' : null
                            }, )
                    ],
                total = 56,
                page = 56,
                page_size = 56
            )
        else:
            return DocumentListResponse(
                documents = [
                    autoaudit.models.document_response.DocumentResponse(
                        id = '', 
                        name = '', 
                        description = '', 
                        document_type = '', 
                        status = '', 
                        file_path = '', 
                        file_type = '', 
                        file_size = 56, 
                        created_at = '', 
                        updated_at = '', 
                        processed_at = '', 
                        metadata = {
                            'key' : null
                            }, )
                    ],
                total = 56,
                page = 56,
                page_size = 56,
        )
        """

    def testDocumentListResponse(self):
        """Test DocumentListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
