import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
dp = [0]*n
lst = []

for _ in range(n):
    a,b,c = map(int, input().split())
    lst.append([a,b,c])

lst.sort(reverse=True)

dp[0] = lst[0][1]
res = lst[0][1]
for i in range(1,n):
    max_h= 0
    for j in range(i-1, -1, -1):
        if lst[j][2]>lst[i][2] and dp[j]>max_h:
            max_h=dp[j]
    dp[i] = max_h + lst[i][1]
    res = max(res, dp[i])


print(res)
