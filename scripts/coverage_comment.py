import os
import xml.etree.ElementTree as ET
import requests
import json

def get_coverage(filename):
    """Parses a JaCoCo XML report and returns the instruction coverage."""
    if not os.path.exists(filename):
        return 0.0

    tree = ET.parse(filename)
    root = tree.getroot()

    instruction_counter = root.find("./counter[@type='INSTRUCTION']")
    if instruction_counter is None:
        return 0.0

    missed = int(instruction_counter.get('missed'))
    covered = int(instruction_counter.get('covered'))
    total = missed + covered
    return (covered / total) * 100 if total > 0 else 0.0

def get_pr_number():
    """Gets the PR number from the GitHub event payload."""
    if 'GITHUB_EVENT_PATH' not in os.environ:
        return None

    with open(os.environ['GITHUB_EVENT_PATH']) as f:
        event = json.load(f)
        if 'pull_request' in event:
            return event['pull_request']['number']
    return None

def post_comment(pr_number, comment_body):
    """Posts a comment to the specified PR."""
    if 'GITHUB_TOKEN' not in os.environ:
        print("Error: GITHUB_TOKEN not found.")
        return

    token = os.environ['GITHUB_TOKEN']
    repo = os.environ['GITHUB_REPOSITORY']
    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"body": comment_body}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Comment posted successfully.")
    else:
        print(f"Error posting comment: {response.status_code} - {response.text}")


def main():
    pr_coverage = get_coverage('jacoco_pr.xml')
    base_coverage = get_coverage('jacoco_base.xml')
    coverage_diff = pr_coverage - base_coverage

    pr_branch = os.environ.get('GITHUB_HEAD_REF', 'PR branch')
    base_branch = os.environ.get('GITHUB_BASE_REF', 'base branch')

    comment = f"""
    📊 **Code Coverage Report for this PR** 📊

    **Current Branch (`{pr_branch}`):** `{pr_coverage:.2f}%`
    **Compared to (`{base_branch}`):** `{base_coverage:.2f}%`
    **Change:** `{coverage_diff:+.2f}%`
    """

    pr_number = get_pr_number()
    if pr_number:
        post_comment(pr_number, comment)
    else:
        print("Not a PR. Skipping comment.")


if __name__ == "__main__":
    main()
