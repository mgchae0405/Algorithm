from collections import deque
import sys
from copy import deepcopy
sys.setrecursionlimit(100000)
sys.stdin=open("input.txt", "rt")


board = [list(map(int, input().split())) for i in range(7)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0]*7 for _ in range(7)]
visited[0][0] = 1

cnt = 0
def bfs(x,y,NB):
    global cnt

    if x == 6 and y == 6:
        cnt += 1
        return
    for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >=7 or ny <0 or ny >=7:
                continue

            if not board[nx][ny] and not NB[nx][ny]:
                NB2 = deepcopy(NB)
                NB2[nx][ny] = 1
                bfs(nx,ny,NB2)


bfs(0,0,visited)
print(cnt)