import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())

def dfs(n):
    if dp[n]>0:
        return dp[n]
    #이게 있음으로써 매번 예를들어 4 라는 숫자가 필요할때마다 -1,-2만큼 재귀를안들어가고 그냥 기록된값으로써라가 되는거

    if n==1 or n==2:
        return n
    else:
        print('현재n', n)
        dp[n] = dfs(n-1)+dfs(n-2)
        print('나와서',n)
        print(dp)
        return dp[n]

dp = [0]*(n+1)

print(dfs(n))