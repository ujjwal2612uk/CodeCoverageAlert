# watsonx_service.py
import requests
import config

def generate_content(prompt):
    """
    Generates content for Jira and Confluence using the IBM WatsonX Orchestrate API.
    """
    headers = {
        "Authorization": f"Bearer {config.WATSONX_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": f"Create a Jira ticket and a Confluence page for the following request: {prompt}. Return the response in JSON format with the following keys: jira_summary, jira_description, confluence_title, confluence_body"
            }
        ]
    }

    response = requests.post(config.WATSONX_URL, headers=headers, json=data)
    response.raise_for_status()
    content = response.json()

    return content
