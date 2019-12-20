# Git status & undoing

## 1. commit

```bash
# WD O, Staging area X
$ git commit

# commit 할 것이 없지만, ->staging area가 비어있음.
# untracked file이 있다. -> git commit 이력에 담기지 않은 파일은 있음.
nothing added to commit but untracked files present

# WD X, Staging area X
$ git commit
# 어떠한 변경 사항도 없음.
nothing to commit

```

### status

1. 새로 파일 생성한 경우

```bash
$ git status
On branch master

No commits yet
# commit 이력에 담긱 적 없는 (신규 생성) 파일들
Untracked files:
# commit 될 목록(staging area)에 추가하려면, git add <file>
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)

```

2. add 한 이후

   ```bash
   $ git add a.txt
   $ git status
   On branch master
   
   No commits yet
   # 커밋할 변경사항들(changes)
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
           new file:   a.txt
   
   ```

   

### commit 메시지 작성하기

> 부제 : vim 활용 기초

```bash
$ git commit
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch master
#
# Initial commit
#
# Changes to be committed:
#       new file:   a.txt
#

```

* 편집 (입력) 모드 :`i`
  * 문서 편집 가능
* 명령 모드 : `esc`
  * `dd` :  해당 줄 삭제
  * `:wq` : 저장 및 종료
    * `w` : write
    * `q` : quit
  * `:!q` : 강제 종료
    * `q` : quit
    * `!` :  강제

```bash
$ git commit -m 'commit message'
```

* 커밋 메시지는 항상 해당 작업 이력을 나타낼 수 있도록 작성한다.
* 일관적인 포맷으로 작성하려고 노력한다.

### log

> 커밋은 해시 값(hash value)에 의해서 구분된다.

> SHA-1 해시 알고리즘을 사용하여 표현하다.
>
> (예) 비밀번호 암호화 저장시, 비트코인

```bash
$ git log
commit 2b7f47273d1434c363253c1452114aa721593146 (HEAD -> master)
Author: hotaru1619 <hotaru1619@naver.com>
Date:   Wed Dec 18 09:43:43 2019 +0900

    Add a.txt
    * a.txt 내용 추가
$ git log --oneline
2b7f472 (HEAD -> master) Add a.txt * a.txt 내용 추가
$ git log -1
$ git log --oneline --graph
$ git log -1 --oneline
```



## commit undoing

1. 커밋 메시지 수정(직전 커밋 메시지만)

```bash
$ git commit --amend
```

커밋 메시지 수정하는 경우 해시 값이 변경되므로, 다른 이력으로 관리가 된다.

**따라서, 공개된 저장소(원격저장소)에 이미 push된 경우 절대 수정해서는 안된다.**

2. 특정 파일 추가하기(시점 돌리기)
   * ` c.txt` 파일을 같이 커밋을 하려고 했는데, add를 하지 못하고 커밋해버렸다.

```bash
$ git add c.txt
$ git commit --amend
```

### Staging area

1. 커밋 이력이 있는 파일 수정하는 경우 

```bash
# a.txt파일 수정 후
$ git status
On branch master
# 변경 사항인데(WD 변화했는데), staging area X
Changes not staged for commit:
# git add로 staging area로 보낼 수 있다.
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")

$ git add a.txt
$ git status
On branch master
Changes to be committed:
# unstage하기 위해서(staging area에서 제외하기 위해서)
  (use "git restore --staged <file>..." to unstage)
        modified:   a.txt

$ git restore --staged a.txt
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

#### add 취소하기

```bash
$ git restore --staged a.txt
```

* 구버전의 git 에서는 아래의 명령어를 사용해야 한다.

```bash
$ git reset HEAD <file>
```

### WD 변화 삭제하기

삭제되었다는 변화 사항을 삭제하여

이전 커밋으로 돌아감.

```bash
$ git add a.txt
$ git commit -m 'Edit a.txt'
[master ffed5bf] Edit a.txt
 1 file changed, 1 insertion(+)
 # a.txt b.txt c.txt 삭제 후
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    a.txt
        deleted:    b.txt
        deleted:    c.txt

```

> git 에서는 모든 commit 시점으로 되돌릴 수는 있다.
>
> 다만,  WD 삭제하는 것은 되돌릴 수가 없다.

```bash
$ git restore <file>
# $ git restore .
```

* 구버전 git에서는 아래의 명령어를 사용해야 한다.

```bash
$ git checkout -- <file>
```

## Stash

> 변경사항을 임시로 저장 해놓는 공간
>
> 마지막 커밋 시점으로 되돌려준다.
>
> ```bash
> 1. feature branch에서 a.txt 변경 후 커밋
> 2. master branch에서 a.txt 수정
> (add나 commit없이)
> 3. merge
> ```

```bash
$ git merge feature
error: Your local changes to the following files would be overwritten by merge:
        a.txt
Please commit your changes or stash them before you merge.
Aborting
Updating ffed5bf..6bb4986

# 3. merge하려고 했는데 문제 발생
```

###  명령어

stash 저장

```bash
$ git stash
Saved working directory and index state WIP on master: ffed5bf Edit a.txt

```

stash 목록

```bash
$ git stash list
stash@{0}: WIP on master: ffed5bf Edit a.txt

$ git stash pop
Auto-merging a.txt
CONFLICT (content): Merge conflict in a.txt
The stash entry is kept in case you need it again.

```

stash 불러오기

```bash
$ git stash pop # 불러오기 + 목록에서 삭제
# $ git stash apply # 불러오기
# $ git stash drop # 목록에서 삭제
```



### 해결

```bash
$ git stash # 임시 공간 저장
$ git merge feature # 병합
$ git stash pop # 임시 공간에서 불러오기
# 충돌 발생, 해결 후 작업 이어가기...!
```

```bash
<<<<<<< Updated upstream
마지막 커밋 시점
=======
마지막 커밋 시점

master master
wd에 있는 상태(수정만)에서 merge
>>>>>>> Stashed changes
```

```bash
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

```



```bash
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

