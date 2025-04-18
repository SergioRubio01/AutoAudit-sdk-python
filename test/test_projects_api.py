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

from autoaudit.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_add_project_member_api_v1_projects_project_id_members_post(self) -> None:
        """Test case for add_project_member_api_v1_projects_project_id_members_post

        Add Project Member
        """
        pass

    def test_create_project_api_v1_projects_post(self) -> None:
        """Test case for create_project_api_v1_projects_post

        Create Project
        """
        pass

    def test_create_project_from_template_api_v1_projects_from_template_post(self) -> None:
        """Test case for create_project_from_template_api_v1_projects_from_template_post

        Create Project From Template
        """
        pass

    def test_delete_project_api_v1_projects_project_id_delete(self) -> None:
        """Test case for delete_project_api_v1_projects_project_id_delete

        Delete Project
        """
        pass

    def test_get_project_api_v1_projects_project_id_get(self) -> None:
        """Test case for get_project_api_v1_projects_project_id_get

        Get Project
        """
        pass

    def test_list_project_members_api_v1_projects_project_id_members_get(self) -> None:
        """Test case for list_project_members_api_v1_projects_project_id_members_get

        List Project Members
        """
        pass

    def test_list_projects_api_v1_projects_get(self) -> None:
        """Test case for list_projects_api_v1_projects_get

        List Projects
        """
        pass

    def test_remove_project_member_api_v1_projects_project_id_members_user_id_delete(self) -> None:
        """Test case for remove_project_member_api_v1_projects_project_id_members_user_id_delete

        Remove Project Member
        """
        pass

    def test_update_project_api_v1_projects_project_id_put(self) -> None:
        """Test case for update_project_api_v1_projects_project_id_put

        Update Project
        """
        pass


if __name__ == '__main__':
    unittest.main()
