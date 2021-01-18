import sys
sys.stdin=open("input.txt", "rt")


def dfs(L, summ):
    global total
    if L == n+1:
        if summ>total:
            total = summ

    else:
        if L+T[L]<=n+1:
            dfs(L+T[L], summ+P[L])
        dfs(L+1,summ)




n = int(input())
T = [0]
P = [0]

for _ in range(n):
    a,b = map(int,input().split())
    T.append(a)
    P.append(b)


total = 0
dfs(1,0)
print(total)