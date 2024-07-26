# Learning Git, GitHub, and GitLab

- init Git repository inside an empty folder:
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

`git merge <BRANCH YOU WISH TO MERGE>`

you run rebase on the branch you want to sync with the master/main branch
git rebase master

git merge --abort
resolving conflicts in VSC or other IDEs

## GitLab
- Add SSH Key\
`ssh-keygen`

- git remote\
`git remote add origin <repository_url>`: tell Git which remote repository in GitLab is linked to a local directory.\

- git pull\ 
pull changes from a remote repo: `git pull origin master`\

- git branch\
`git clone <>`\
`git branch`\
`git branch -a`\
`git checkout <branch-name>`\
have many remote branches that you want to fetch at once: `git pull -all`\




# Refernce
- Udemy course by Valentin: https://www.udemy.com/course/introduction-to-git-for-gitlab-projects/