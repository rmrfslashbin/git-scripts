#!/usr/bin/env python

from github import Github
from os import environ

try:
    t = environ['GITHUB_TOKEN']
except KeyError:
    raise SystemExit("GITHUB_TOKEN env var is not set")
g = Github(t)

for gist in g.get_user().get_gists():
    print(u"{} :: {}".format(gist.html_url, gist.description))
