import sys
sys.stdin=open("input.txt", "rt")


n, m = map(int,input().split())
dp = [0]*(m+1)



for i in range(n):
    a,b = map(int, input().split())
    for j in range(a,m+1):
        dp[j] = max(dp[j],dp[j-a]+b)
    print(dp)

#
#     lst.append([a,b])
# #lst.sort(key=lambda x:x[1], reverse=True)
# lst.sort()
#
# print(lst)