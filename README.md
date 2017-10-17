# Git Scripts
A collection of scripts to support git repos.

# Scripts
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
