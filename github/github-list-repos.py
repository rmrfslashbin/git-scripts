#!/usr/bin/env python3

from github import Github
from os import environ

# First create a Github instance:

# or using an access token
try:
    t = environ['GITHUB_TOKEN']
except KeyError:
    raise SystemExit("GITHUB_TOKEN env var is not set")
g = Github(t)

for repo in g.get_user().get_repos():
    print(repo.name)
