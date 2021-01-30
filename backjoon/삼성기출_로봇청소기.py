import sys
from collections import Counter
sys.stdin=open("input.txt", "rt")

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

n, m= map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]


def dfs(x,y,d):
    global cnt
    if not board[x][y]:
        board[x][y] = 2
        cnt +=1
    for _ in range(4):
        nd = (d+3)%4
        nx, ny = x+dx[nd],y+dy[nd]
        if not board[nx][ny]:
            dfs(nx,ny,nd)
            return
        d = nd

    nd = (d+2)%4
    nx,ny = x+dx[nd],y+dy[nd]
    if board[nx][ny] == 1:
        return
    dfs(nx,ny,d)

cnt = 0
dfs(r,c,d)
print(cnt)