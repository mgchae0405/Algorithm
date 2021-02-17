import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
board = [list(map(int,input().split())) for i in range(n)]
dp = [[0]*n for i in range(n)]
dp[0][0] = board[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i-1] + board[0][i]
    dp[i][0] = dp[i-1][0] + board[i][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = min(dp[i-1][j],dp[i][j-1])+board[i][j]

print(dp[n-1][n-1])