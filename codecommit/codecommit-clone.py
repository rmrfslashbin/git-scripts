#!/usr/bin/python

import boto3
import argparse

session = boto3.session.Session()
client = session.client('codecommit')

parser = argparse.ArgumentParser(description='Get the SSH URL for a repo')
parser.add_argument("repo", type=str, nargs="+")
args = parser.parse_args()

repoData = client.get_repository(repositoryName=args.repo[0])
sshURL = repoData["repositoryMetadata"]["cloneUrlSsh"]
print("git clone {}".format(sshURL))