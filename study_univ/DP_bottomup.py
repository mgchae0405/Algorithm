import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())

dp = [0]*(n+1)

# 1 3 5 8 13 21 33
#  2 2 3 5  8  12
#     1 2  3  4  5

dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n])