from collections import deque
import sys
sys.stdin=open("input.txt", "rt")

board = [list(map(int, input().split())) for i in range(7)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
q. append([0,0])

visited = [[0]*7 for _ in range(7)]
visited[0][0] = 1

def bfs(i,j):
    cnt = 1
    ck = True
    q.append([i, j])
    while q:

        for _ in range(len(q)):
            x,y = q.popleft()


            for i in range(4):
                    nx,ny = x+dx[i], y+dy[i]
                    if nx < 0 or nx >=7 or ny <0 or ny >=7:
                        continue
                    if not board[nx][ny] and not visited[nx][ny]:
                        q.append([nx,ny])
                        visited[nx][ny] = cnt
                    if nx == 6 and ny==6:
                        ck = False
                        return visited[nx][ny]


        cnt+=1
    if ck:
        return -1


print(bfs(0,0))