# tests/test_confluence_service.py
import unittest
from unittest.mock import Mock
import confluence_service

class TestConfluenceService(unittest.TestCase):

    def test_create_confluence_page(self):
        # Mock the Confluence client
        mock_client = Mock()
        mock_client.url = "https://test-domain.atlassian.net"

        # Define the expected response
        space = "TEST"
        title = "Test Title"
        body = "Test Body"

        # Call the function
        response = confluence_service.create_confluence_page(mock_client, space, title, body)

        # Assert the response is as expected
        self.assertIn("id", response)
        self.assertIn("url", response)

if __name__ == '__main__':
    unittest.main()
