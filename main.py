# main.py
import config
import watsonx_service
import jira_service
import confluence_service

def main():
    # Get user prompt
    prompt = input("Please enter your prompt: ")

    # Initialize clients
    jira_client = jira_service.get_jira_client(config.JIRA_URL, config.JIRA_USER_EMAIL, config.JIRA_API_TOKEN)
    confluence_client = confluence_service.get_confluence_client(config.CONFLUENCE_URL, config.CONFLUENCE_USER_EMAIL, config.CONFLUENCE_API_TOKEN)

    # Generate content
    content = watsonx_service.generate_content(prompt)

    # Create Jira ticket
    jira_ticket = jira_service.create_jira_ticket(
        jira_client,
        "PROJ",  # Replace with your Jira project key
        content["jira_summary"],
        content["jira_description"]
    )
    print(f"Successfully created Jira ticket: {jira_ticket['url']}")

    # Create Confluence page
    confluence_page = confluence_service.create_confluence_page(
        confluence_client,
        "SPACE",  # Replace with your Confluence space key
        content["confluence_title"],
        content["confluence_body"]
    )
    print(f"Successfully created Confluence page: {confluence_page['url']}")

if __name__ == "__main__":
    main()
