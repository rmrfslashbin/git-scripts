# Git Scripts
A collection of scripts to support local, AWS CodeCommit, GitHub, and Azure DevOps git repos.

- mkgitignore  ::  Generates a ```.gitignore``` file from a selection of gitignore files from https://github.com/github/gitignore

# General git utilities
- find-dirty-repos        :: Checks if a repo is dirty (needs a commit and push)
- find-repos-need-pull    :: Checks if repo needs a pull
- find-dirs-no-repo       :: Looks for dirs which don't have a git repo
- find-needs-push         :: Checks if repo needs a push

# Github
A [Personal Access Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) is required for these scripts.
- github-git-clone  :: Generate a ```git clone``` command for a given repo
- github-list-gists :: Lists a user's gists
- github-list-repos :: Lists a user's repos

# AWS Codecommit
- Deprecated in favor of: https://github.com/rmrfslashbin/aws-cli-tools.

# Azure DevOps Repos
Azure DevOps provides TFS style git repos. A personal access token is requred to use these scripts.
- tfs-list   :: List available repos
- tfs-clone  :: Generate a ```git clone``` command to clone a repo 
