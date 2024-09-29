# Learning Git, GitHub, and GitLab

## GitHub Common use case

1. If I want to create a new repo, and do some work on it:
```
mkdir repo-folder
cd repo-folder
git init
...
git add .
git commit -m "message"
git push
```
2. If I create a large file, it cannot push to the remote repo. How to unstage this from the commit?


## Git

- git init
```
mkdir my-cool-website
cd my-cool-website
git init   # initiate the repo of "my-cool-website"
git status   # useful to check the repo status
```
<br>

- configure our name and email to identify who has made a specific change:
```
git config --global user.name "FIRST_NAME LAST_NAME"
git config --global user.email "MY_NAME@example.com"
```
<br>

- stage and commit files\
```
git add .
git commit -m "Message"
```
staging one file: `git add <FILE NAME>`; staging all files: `git add .` or `git add --all`\
commit files: `git commit -m "Message"`\
unstage a file: `git reset HEAD <FILE>`
<br>


- track git history:\
`git log`\
`git log --patch`\
<br>

-  gitkeep and gitignore \
`.gitkeep`: A folder tracked by Git, add this emtpy file\
`.gitignore`\
<br>

- git branch   
create a new branch with: `git checkout -b <BRANCH NAME>`  
to switch back to master/main run: `git checkout master`  
create a new branch based on another remote branch: `git checkout -b new-branch-name origin/remote-branch-name`  

- git merge

`git merge <BRANCH YOU WISH TO MERGE>`

you run rebase on the branch you want to sync with the master/main branch
git rebase master

git merge --abort
resolving conflicts in VSC or other IDEs

## GitLab

- Add SSH Key\
`ssh-keygen`: use default algorithm to generate ssh key, which is saved in "id_ed25519.pub".
`ssh-keygen -t rsa -b 4096`: use RSA algorithm with bits larger than 4096 to generate ssh key. The key is in "id_rsa.pub" file\

- Git Clone\
`git clone gitlab-link`\
if we have to use token, we first setup the token from the project account, then we can git clone this way: `git clone https://username:token@gitlab-link.git`\


- git remote\
`git remote add origin <repository_url>`: tell Git which remote repository in GitLab is linked to a local directory.\

- git pull\
pull changes from a remote repo: `git pull origin master`\

- git branch\
`git clone <>`\
`git branch`\
`git branch -a`\
`git checkout <branch-name>`\
push a new local branch to a remote Git repo:
`git push -u origin <branch>`: -u (short for --set-upstream)\
<br>



## Refernce

- Udemy course by Valentin: https://www.udemy.com/course/introduction-to-git-for-gitlab-projects/