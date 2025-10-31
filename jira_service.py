# jira_service.py
from atlassian import Jira

def get_jira_client(url, username, token):
    return Jira(url=url, username=username, password=token)

def create_jira_ticket(client, project_key, summary, description):
    # In a real application, you would make an API call like this:
    new_issue = client.issue_create(
        fields={
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": "Task"},
        }
    )
    return {"key": new_issue['key'], "url": f"{client.url}/browse/{new_issue['key']}"}
