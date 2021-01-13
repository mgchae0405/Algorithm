import sys
sys.stdin=open("input.txt", "rt")

def dfs(l):
    if l==m:
        for j in range(m):
            print(res[j], end=' ')
        print()

    else:
        for i in range(l,n+1):
            res[l] = i
            dfs(l+1)

n,m = map(int,input().split())
res = [0]*n
dfs(0)
print(n**m)