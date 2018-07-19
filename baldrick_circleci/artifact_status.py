import requests

from baldrick.github.github_auth import github_request_headers
from .circleci import circleci_webhook_handler


HOST = "https://api.github.com"


@circleci_webhook_handler
def set_commit_status_for_artifacts(repo_handler, payload):
    if payload['status'] == 'success':
        artifacts = get_artifacts_from_build(payload)

        urls = repo_handler.get_config_value("circleci_artifacts",
                                             {"sphinx": {
                                                 "url": "html/index.html",
                                                 "message":
                                                 "Click details to preview the documentation build"}})

        for name, config in urls.items():

            url = get_documentation_url_from_artifacts(artifacts, config['url'])

            if url:
                set_commit_status(repo_handler,
                                  payload['vcs_revision'],
                                  name,
                                  "success",
                                  config['message'],
                                  url)

    return "All good"


def get_artifacts_from_build(p):
    base_url = "https://circleci.com/api/v1.1"
    query_url = f"{base_url}/project/github/{p['username']}/{p['reponame']}/{p['build_num']}/artifacts"
    response = requests.get(query_url)
    assert response.ok, response.content
    return response.json()


def get_documentation_url_from_artifacts(artifacts, url):
    for artifact in artifacts:
        # Find the root sphinx index.html
        if url in artifact['path']:
            return artifact['url']


def set_commit_status(repo_handler, commit_hash, context, state, description, target_url):

    headers = github_request_headers(repo_handler.installation)

    set_status(repo_handler.repository, commit_hash, state, description, context,
               headers=headers, target_url=target_url)


def set_status(repository, commit_hash, state, description, context, *, headers, target_url=None):
    """
    Set status message in a pull request on GitHub.

    Parameters
    ----------
    state : { 'pending' | 'success' | 'error' | 'failure' }
        The state to set for the pull request.

    description : str
        The message that appears in the status line.

    context : str
        A string used to identify the status line.

    target_url : str or `None`
        Link to bot comment that is relevant to this status, if given.

    """

    data = {}
    data['state'] = state
    data['description'] = description
    data['context'] = context

    if target_url is not None:
        data['target_url'] = target_url

    url = f'{HOST}/repos/{repository}/statuses/{commit_hash}'
    response = requests.post(url, json=data, headers=headers)
    assert response.ok, response.content
