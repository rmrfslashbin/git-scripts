#!/usr/bin/env python3

from github import Github
from os import environ
import argparse

parser = argparse.ArgumentParser(description="List Github repos")
parser.add_argument("--private", action="store_true", help="Show private flag")
parser.add_argument("--descr", action="store_true", help="Show description")
parser.add_argument("--fork", action="store_true", help="Show fork flag")
parser.add_argument("--url", action="store_true", help="Show homepage (html_url) URL")
parser.add_argument("--sshurl", action="store_true", help="Show ssh URL")
parser.add_argument("--topics", action="store_true", help="Show topics")
parser.add_argument("--forks", action="store_true", help="Show fork count")
parser.add_argument("--stars", action="store_true", help="Show start count")
parser.add_argument("--watchers", action="store_true", help="Show watchers count")
parser.add_argument("--subscribers", action="store_true", help="Show subscribes count")
parser.add_argument("--created", action="store_true", help="Show created date")
parser.add_argument("--updated", action="store_true", help="Show updated date")

args = parser.parse_args()



# First create a Github instance:

# or using an access token
try:
    t = environ['GITHUB_TOKEN']
except KeyError:
    raise SystemExit("GITHUB_TOKEN env var is not set")
g = Github(t)

for repo in g.get_user().get_repos():
    reponame = repo.full_name
    private = repo.private
    descr = repo.description
    fork = repo.fork
    html_url = repo.html_url
    ssh_url = repo.ssh_url
    topics = repo.topics
    forks_count = repo.forks_count
    stars_count = repo.stargazers_count
    watchers_count = repo.watchers_count
    subcribers = repo.subscribers_count
    created_at = repo.created_at
    updated_at = repo.updated_at

    print(reponame)
    if args.descr:
        print("    Descr", descr)
    if args.url:
        print("    HTML URL", htm_url)
    if args.private:
        print("    Private", private)
    if args.fork:
        print("    Fork", fork)
    if args.sshurl:
        print("    SSH URL", ssh_url)
    if args.topics:
        print("    Topics", topics)
    if args.forks:
        print("    Fork count", forks_count)
    if args.stars:
        print("    Star count", stars_count)
    if args.watchers:
        print("    Watchers count", watchers_count)
    if args.subscribers:
        print("    Subscribers count", subscribers)
    if args.created:
        print("    Created at", created_at)
    if args.updated:
        print("    Updated at", updated_at)
