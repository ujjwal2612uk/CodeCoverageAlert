# tests/test_jira_service.py
import unittest
from unittest.mock import Mock
import jira_service

class TestJiraService(unittest.TestCase):

    def test_create_jira_ticket(self):
        # Mock the Jira client
        mock_client = Mock()
        mock_client.url = "https://test-domain.atlassian.net"

        # Define the expected response
        project_key = "TEST"
        summary = "Test Summary"
        description = "Test Description"

        # Call the function
        response = jira_service.create_jira_ticket(mock_client, project_key, summary, description)

        # Assert the response is as expected
        self.assertIn("key", response)
        self.assertIn("url", response)

if __name__ == '__main__':
    unittest.main()
