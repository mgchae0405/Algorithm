from collections import deque
import sys
#sys.stdin=open("input.txt", "rt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

max_h = max([max(_) for _ in board])
min_h = min([min(_) for _ in board])

max_total = 0

def bfs(TT,x,y):
    q = deque()
    global visited
    q.append([x,y])
    visited[x][y] = 1
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] > TT and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx,ny])





for i in range(4,max_h+1):
    visited = [[0]*n for _ in range(n)]
    ee = 0
    for z in range(n):
        for w in range(n):

            if board[z][w] > i and not visited[z][w]:
                bfs(i,z,w)
                ee+=1
    if max_total < ee:
        max_total = ee
print(max_total)

