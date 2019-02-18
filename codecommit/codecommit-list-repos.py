#!/usr/bin/env python3

import boto3
import concurrent.futures


session = boto3.session.Session()
client = session.client('codecommit')

def getRepoData(repoName):
    try:
        repoInfo = client.get_repository(repositoryName=repoName)
        return repoInfo["repositoryMetadata"]
    except: 
        raise



repoList = client.list_repositories()
repos = []
for repo in repoList["repositories"]:
    repos.append(repo["repositoryName"])

reposData = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future_to_repo = {executor.submit(getRepoData, repo): repo for repo in repos}
    for future in concurrent.futures.as_completed(future_to_repo):
        repo = future_to_repo[future]
        try:
            reposData[repo] = future.result()
        except Exception as exc:
            print("{} generated an exception: {}".format(url, exc))

for repo in sorted(reposData):
    descr = reposData[repo].get("repositoryDescription")
    print("{0:20s} {1}".format(repo, descr))
