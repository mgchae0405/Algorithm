from collections import deque
import sys
# sys.stdin=open("input.txt", "rt")

dx = [1,-1,0,0]
dy = [0,0,1,-1]

m,n = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]




ck = True
kk = True
q= deque()
cnt = 0
need_visited = [[0] * m for _ in range(n)]

while ck:

    for i in range(n):
        for j in range(m):

            if board[i][j] == 1 and not visited[i][j]:
                q.append([i,j])
                visited[i][j] = 1
    # print('.이전q',q)

    for _ in range(len(q)):

        x, y = q.popleft()
        # print('xy',x,y)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not board[nx][ny] and not need_visited[nx][ny]:
                board[nx][ny] = 1
                need_visited[nx][ny] = 1
                q.append([nx,ny])
        # print(board)
        # print('q',q)
    if not q:
        for i in board:
            if 0 in i and kk:
                print(-1)
                kk = False
        ck=False
    cnt +=1
if kk:
    print(cnt-1)
