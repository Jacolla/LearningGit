#   <-- Forma interactiva de practicar con comandos Git -->
#   <-- https://learngitbranching.js.org/ -->



# <-- Comands for Git -->

#   1. init
#   To initialize a git repository for a new or existing project.
#   The git init command is used for creating a new git repository.
#   It can be used to convert an existing project to a git repository or initialize a new and empty repository.
#   git init [repository name]
#   
#   
#   2. add
#   To add changes to index in your working directory.
#   The git add command adds a change in the working directory to the staging area. 
#   It tells git that you want to include updates to a particular file in the next commit.
#   git add [file]
#   
#   
#   3. commit
#   To commit your changes and sets it to new commit object for your remote version.
#   The git commit command captures a snapshot of the project's currently staged changes.
#   git commit -m ”commit-message”
#   
#   
#   4. stash
#   To save changes that you don’t want to commit immediately.
#   Use git stash command is used to record the current state of the working directory and the index. 
#   This command saves your local modifications away and reverts the working directory to match the head commit.
#   git stash [list]
#   
#   
#   5. push
#   To push the local changes to the master branch of the project.
#   The git push command is used to upload local repository content to a remote repository.
#   git push [branch-name]
#   
#   
#   6. branch
#   To list out all the branches in the project.
#   The git branch command lets you create, list, rename, and delete branches. 
#   However it doesn’t let you switch between branches or put a forked history back together again.
#   git branch [branch-name]
#   
#   
#   7. checkout
#   To switch to a different branch.
#   The git checkout command lets you navigate between the branches created by git branch. 
#   Checking out a branch updates the files in the working directory to match the version stored in that branch, 
#   and it tells git to record all new commits on that branch.
#   git checkout [branch-name]
#   
#   
#   8. merge
#   To merge two branches you were working on.
#   The git merge command is used to integrate changes from another branch. 
#   It combines all the integrated changes into a single commit, instead of preserving them as individual commits.
#   git merge [branch-name]
#   
#   
#   9. clone
#   To copy a git repository from a remote source.
#   The git clone command copies an existing git repository. 
#   This is similar to SVN checkout, except the working copy is a git repository, having its own history, manages its own files, 
#   and is a completely isolated environment from the original repository.
#   git clone [url]
#   
#   
#   10. status
#   To check the status of files you’ve changed in your working directory
#   The git status command displays the state of the working directory and the staging area. 
#   It lets you see which changes have been staged, which haven’t, 
#   and which files aren’t being tracked by git at the moment.
#   git status
#   




#  These are common Git commands used in various situations:
#  
#  start a working area (see also: git help tutorial)
#     clone     Clone a repository into a new directory
#     init      Create an empty Git repository or reinitialize an existing one
#  
#  work on the current change (see also: git help everyday)
#     add       Add file contents to the index
#     mv        Move or rename a file, a directory, or a symlink
#     restore   Restore working tree files
#     rm        Remove files from the working tree and from the index
#  
#  examine the history and state (see also: git help revisions)
#     bisect    Use binary search to find the commit that introduced a bug
#     diff      Show changes between commits, commit and working tree, etc
#     grep      Print lines matching a pattern
#     log       Show commit logs
#     show      Show various types of objects
#     status    Show the working tree status
#  
#  grow, mark and tweak your common history
#     branch    List, create, or delete branches
#     commit    Record changes to the repository
#     merge     Join two or more development histories together
#     rebase    Reapply commits on top of another base tip
#     reset     Reset current HEAD to the specified state
#     switch    Switch branches
#     tag       Create, list, delete or verify a tag object signed with GPG
#  
#  collaborate (see also: git help workflows)
#     fetch     Download objects and refs from another repository
#     pull      Fetch from and integrate with another repository or a local branch
#     push      Update remote refs along with associated objects
#  
#  'git help -a' and 'git help -g' list available subcommands and some
#  concept guides. See 'git help <command>' or 'git help <concept>'
#  to read about a specific subcommand or concept.
#  See 'git help git' for an overview of the system.
#  