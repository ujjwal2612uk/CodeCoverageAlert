# confluence_service.py
from atlassian import Confluence

def get_confluence_client(url, username, token):
    return Confluence(url=url, username=username, password=token)

def create_confluence_page(client, space, title, body):
    # In a real application, you would make an API call like this:
    new_page = client.create_page(
        space=space,
        title=title,
        body=body
    )
    return {"id": new_page['id'], "url": f"{client.url}/wiki/spaces/{space}/pages/{new_page['id']}"}
