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

from autoaudit.models.document_metadata_response import DocumentMetadataResponse

class TestDocumentMetadataResponse(unittest.TestCase):
    """DocumentMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentMetadataResponse:
        """Test DocumentMetadataResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentMetadataResponse`
        """
        model = DocumentMetadataResponse()
        if include_optional:
            return DocumentMetadataResponse(
                document_type = '',
                main_topics = [
                    ''
                    ],
                created_date = '',
                document_category = '',
                has_tables = True,
                extracted_data = {
                    'key' : null
                    }
            )
        else:
            return DocumentMetadataResponse(
        )
        """

    def testDocumentMetadataResponse(self):
        """Test DocumentMetadataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
