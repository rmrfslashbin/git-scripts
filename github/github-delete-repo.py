#!/usr/bin/env python

from github import Github
from os import environ

try:
    t = environ['GITHUB_TOKEN']
except KeyError:
    raise SystemExit("GITHUB_TOKEN env var is not set")
g = Github(t)

repoName = raw_input("Name of repo to delete: ")
try:
    r = g.get_repo(repoName)
except BaseException:
    raise

confirm = raw_input(
    "Enter YES to Confirm you intend to delete ({}): ".format(repoName))
if confirm != "YES":
    raise SystemExit("User did not respond YES")

try:
    r.delete()
except BaseException:
    raise