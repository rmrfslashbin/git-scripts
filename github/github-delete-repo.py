#!/usr/bin/env python3

from github import Github
from os import environ
import argparse

try:
    t = environ['GITHUB_TOKEN']
except KeyError:
    raise SystemExit("GITHUB_TOKEN env var is not set")
try:
    user = environ['GITHUB_USER']
except KeyError:
    raise SystemExit("GITHUB_USER env var is not set")

g = Github(t)
parser = argparse.ArgumentParser(description='Delete Github repo')
parser.add_argument("--repo", "-r", required=True, type=str, nargs="+", help="Repo name")
parser.add_argument("--user", "-u", type=str, nargs="+", help="Github user")
parser.add_argument("--confirm", "-c", required=True, action="store_true", help="Confirm repo deletion")
args = parser.parse_args()


if args.user:
    user = args.user

for repo in args.repo:
    repoName = "{}/{}".format(user, repo)
    try:
        r = g.get_repo(repoName)

    except BaseException:
        raise

    try:
        r.delete()
        print("Deleted {}".format(repoName))
    except BaseException:
        raise
