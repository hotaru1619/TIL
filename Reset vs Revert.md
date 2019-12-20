# Reset vs Revert

## Reset

> 공개된 저장소(원격 저장소)에 push된 이력은 절대 reset하지 않는다.

```bash
$ git reset {해시코드}
```

* 기본 (`--mixed`) : 이후 변경 사항을 WD에 유지시켜줌.

* `--hard` : 이후 변경 사항이 모두 삭제됨.

  **주의**

* `--soft` : 지금 작업하고 있는 내용(WD) 및 변경사항을 WD에 유지시켜줌.

## Revert

> 해당 커밋으로 되돌렸다라는 이력(revert commit)을 남긴다.

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

$ git log --oneline
6bb4986 (HEAD -> master, feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

```



```bash
$ git status
On branch master
nothing to commit, working tree clean

$ git log --oneline
3ee254d (HEAD -> master) from revert
6bb4986 (feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

$ git reset 6bb4986
Unstaged changes after reset:
M       a.txt

$ git add .
$ git commit -m 'reset 6bb4986'
[master 0d82046] reset 6bb4986
 1 file changed, 1 insertion(+), 1 deletion(-)
 
 $ git status
On branch master
nothing to commit, working tree clean

$ git log --oneline
0d82046 (HEAD -> master) reset 6bb4986
6bb4986 (feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가

$ git revert 0d82046
[master a17ab1b] try Revert "reset 6bb4986"
 1 file changed, 1 insertion(+), 1 deletion(-)

$ git log --oneline
a17ab1b (HEAD -> master) try Revert "reset 6bb4986"
0d82046 reset 6bb4986
6bb4986 (feature) Edit a.txt on feature
ffed5bf Edit a.txt
271545a b.txt c.txt 추가 commit message add
2b7f472 Add a.txt * a.txt 내용 추가
.
.
.

```

