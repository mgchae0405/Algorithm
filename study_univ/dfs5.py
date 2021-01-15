import sys
sys.stdin=open("input.txt", "rt")


def dfs(L, summ, time):
    global res

    if time >m:
        return

    if L>=n:
        if summ>res:
            res = summ

    else:
        dfs(L+1, summ+lst_1[L], time+lst_2[L])
        dfs(L+1, summ, time)


n, m = map(int, input().split())
lst_1 = []
lst_2 = []
for _ in range(n):
    a,b = map(int, input().split())
    lst_1.append(a)
    lst_2.append(b)

res = 0
dfs(0, 0, 0)
print(res)