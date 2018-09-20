# Git Scripts
A collection of scripts to support git repos. Locally, AWS CodeCommit, and GitHub.

# General git utilities
- find-dirty-repos        :: Checks if a repo is dirty (needs a commit and push)
- find-repos-need-pull    :: Checks if repo needs a pull

# Github
A [Personal Access Token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) is required for these scripts.
- github-git-clone  :: Generate a ```git clone``` command for a given repo
- github-list-gists :: Lists a user's gists
- github-list-repos :: Lists a user's repos

# AWS Codecommit
These commands require a configured [AWS CLI](https://aws.amazon.com/cli/).
- codecommit-clone      :: Generate a ```git clone``` command for a given repo
- codecommit-create     :: Creates a repo
- codecommit-delete     :: Deletes a user's repo
- codecommit-list-repos :: Lists a user's repos
