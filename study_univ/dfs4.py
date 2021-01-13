import sys
sys.stdin=open("input.txt", "rt")

def dfs(l):
    if l==m:
        for j in range(m):
            print(res[j], end=' ')
        print()

    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[l] = i
                dfs(l+1)
                ch[i]=0


n,m = map(int,input().split())
res = [0]*n
ch = [0]*(n+1)
dfs(0)
print(n**m)