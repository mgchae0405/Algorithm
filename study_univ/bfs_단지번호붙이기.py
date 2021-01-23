from collections import deque
import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
lst = [[int(i) for i in input()] for _ in range(n)]

visited = [[0]*n for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

q =deque()
total_lst = []

def bfs(x,y):
    cnt = 0
    q.append([x,y])
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if lst[nx][ny] and not visited[nx][ny]:
                visited[nx][ny]=1

                q.append([nx,ny])
    if cnt>0:
        total_lst.append(cnt)






for i in range(n):
    for j in range(n):
        if lst[i][j] and not visited[i][j]:
            visited[i][j]=1
            bfs(i,j)

print(len(total_lst))
for z in sorted(total_lst):
    print(z)