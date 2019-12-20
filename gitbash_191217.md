### code(191217)

```bash
student@M160224 MINGW64 ~/Desktop/git_plus
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/git_plus/.git/

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ touch a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit
On branch master

Initial commit

Untracked files:
        a.txt

nothing added to commit but untracked files present

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit
On branch master

Initial commit

nothing to commit

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ touch a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git add a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt


student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit
[master (root-commit) 2b7f472] Add a.txt * a.txt 내용 추가
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log
commit 2b7f47273d1434c363253c1452114aa721593146 (HEAD -> master)
Author: hotaru1619 <hotaru1619@naver.com>
Date:   Wed Dec 18 09:43:43 2019 +0900

    Add a.txt
    * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log --oneline
2b7f472 (HEAD -> master) Add a.txt * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ touch b.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git add .

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log -1 --oneline
2b7f472 (HEAD -> master) Add a.txt * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit -m 'commit message'
[master d47694c] commit message
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log -1 --oneline
d47694c (HEAD -> master) commit message

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log --oneline
d47694c (HEAD -> master) commit message
2b7f472 Add a.txt * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit --amend
[master 7d83608] commit message add
 Date: Wed Dec 18 10:18:59 2019 +0900
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log --oneline
7d83608 (HEAD -> master) commit message add
2b7f472 Add a.txt * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ ls
a.txt  b.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ touch c.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt

nothing added to commit but untracked files present (use "git add" to track)

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git add c.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit --amend
[master 271545a] b.txt c.txt 추가 commit message add
 Date: Wed Dec 18 10:18:59 2019 +0900
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 b.txt
 create mode 100644 c.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
nothing to commit, working tree clean

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log --oneline
271545a (HEAD -> master) b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git log --oneline -1
271545a (HEAD -> master) b.txt c.txt 추가 commit message add

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git add a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   a.txt


student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git restore --staged a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git add a.txt

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git commit -m 'Edit a.txt'
[master ffed5bf] Edit a.txt
 1 file changed, 1 insertion(+)

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    a.txt
        deleted:    b.txt
        deleted:    c.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$ git restore .

student@M160224 MINGW64 ~/Desktop/git_plus (master)
$git merge feature
error: Your local changes to the following files would be overwritten by merge:
        a.txt
Please commit your changes or stash them before you merge.
Aborting
Updating ffed5bf..6bb4986

$ git stash
Saved working directory and index state WIP on master: ffed5bf Edit a.txt

$ git stash list
stash@{0}: WIP on master: ffed5bf Edit a.txt

$ git stash pop
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
The stash entry is kept in case you need it again.

$ git checkout -b feature
Switched to a new branch 'feature'

$ git add .

$ git commit -m 'Edit a.txt on feature'
[feature 6bb4986] Edit a.txt on feature
 1 file changed, 4 insertions(+), 1 deletion(-)

$ git checkout master
Switched to branch 'master'

$ git merge feature
error: Your local changes to the following files would be overwritten by merge:
        a.txt
Please commit your changes or stash them before you merge.
Aborting
Updating ffed5bf..6bb4986

$ git stash
Saved working directory and index state WIP on master: ffed5bf Edit a.txt

$ git status
On branch master
nothing to commit, working tree clean

$ git merge feature
Updating ffed5bf..6bb4986
Fast-forward
 a.txt | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)

$ git stash list
stash@{0}: WIP on master: ffed5bf Edit a.txt

$ git stash pop
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
The stash entry is kept in case you need it again.

$ git add .

$ git commit -m 'Complete commit'
[master 5aebb69] Complete commit
 1 file changed, 8 insertions(+), 1 deletion(-)

$ git status
On branch master
nothing to commit, working tree clean

$ git log --oneline
5aebb69 (HEAD -> master) Complete commit
6bb4986 (feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

$ git reset 6bb4986
Unstaged changes after reset:
M       a.txt

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

$ git stash pop
a.txt: needs merge
The stash entry is kept in case you need it again.

$ git commit -m 'Re a!!'
[master f74cd35] Re a!!
 1 file changed, 4 insertions(+), 1 deletion(-)

$ git log --oneline
f74cd35 (HEAD -> master) Re a!!
6bb4986 (feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

$ git reset --hard 6bb4986
HEAD is now at 6bb4986 Edit a.txt on feature

$ git status
On branch master
nothing to commit, working tree clean

$ git log --oneline
6bb4986 (HEAD -> master, feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가
```

