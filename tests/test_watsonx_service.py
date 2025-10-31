# tests/test_watsonx_service.py
import unittest
import requests_mock
import watsonx_service
import config

class TestWatsonxService(unittest.TestCase):

    @requests_mock.Mocker()
    def test_generate_content(self, m):
        # Define the expected response
        prompt = "test prompt"
        expected_response = {
            "jira_summary": f"Jira ticket for: {prompt}",
            "jira_description": f"This is a Jira ticket generated from the prompt: {prompt}",
            "confluence_title": f"Confluence page for: {prompt}",
            "confluence_body": f"This is a Confluence page generated from the prompt: {prompt}"
        }

        # Mock the API call
        m.post(config.WATSONX_URL, json=expected_response)

        # Call the function
        response = watsonx_service.generate_content(prompt)

        # Assert the response is as expected
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
