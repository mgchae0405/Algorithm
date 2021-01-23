from collections import deque
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

print(lst)

q =deque()
visited = [[0]*n for i in range(n)]

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]

def bfs(x,y):
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(len(dx)):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if lst[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append([nx,ny])



cnt = 0
for i in range(n):
    for j in range(n):
        if lst[i][j] and not visited[i][j]:
            visited[i][j]=1
            bfs(i,j)
            cnt+=1

print(cnt)