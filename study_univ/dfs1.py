import sys
sys.stdin=open("input.txt", "rt")

def dfs(v):
    if v== n+1:
        for i in range(len(ck)):
            if ck[i] == 1:
                print(i, end=' ')
        print()

    else:
        ck[v]=1
        dfs(v+1)
        ck[v]=0
        dfs(v+1)


n = int(input())
ck = [0]*(n+1)
dfs(1)