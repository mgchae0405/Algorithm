import sys
sys.stdin=open("input.txt", "rt")


def dfs(L,S):
    if S > total//2:
        return

    if L ==n:
        if S==(total-S):
            print("YES")
            sys.exit(0)
    else:
        dfs(L + 1, S + lst[L])
        dfs(L + 1, S)



n = int(input())
lst = list(map(int,input().split()))

total = sum(lst)
dfs(0,0)
print('NO')