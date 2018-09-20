# Git Scripts
A collection of scripts to support git repos. Locally, AWS CodeCommit, and GitHub.

# General git utilities
- find-dirty-repos        :: Checks if a repo is dirty (needs a commit and push)
- find-repos-need-pull    :: Checks if repo needs a pull

# Github
A [Personal Access Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) is required for these scripts.
- github-git-clone  :: Generate a ```git clone``` command for a given repo
- list-github-gists :: Lists a user's gists
- list-github-repos :: Lists a user's repos

# AWS Codecommit
These commands require a configured [AWS CLI](https://aws.amazon.com/cli/).
- codecommit-create
- codecommit-delete
- git-clone
- list-codecomit-repos

* clone-missing-remote-repos  executes a clone of repos which are not local
* find-dirty-repos            find repos which need commits
* find-local-but-not-remote   find dirs in defined dirs which are not listed in code commit
* find-repos-need-pull        find repos which need a pull
* git-clone                   show a simple "git clone" of a repo
* get-full-clone-list         a full listing of all "code commit" repos formatted as a "git clone"
* search                      list all "code commit" repos
* sync-to-aws                 "git push" a dir of bar repos
* is-local-repo               Checks to see if a ".git" dir exists in path provided as param 1

# Setup
Boto3 is required... ```pip install boto3```

# Uses
```
execpath="/path/to/git-scripts"
$execpath/search | while read repo; do 
    $execpath/is-local-repo $repo
    if [ $? -ne 0 ]; then 
        $execpath/git-clone $repo
    fi
done
```
