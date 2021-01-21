import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

st = 2147000000
end = 0

cnt = 0

visited = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if st > board[i][j]:
            st = board[i][j]
            st_point = [i,j]
        elif end < board[i][j]:
            end = board[i][j]
            end_point = [i,j]




def dfs(st_point):
    global cnt
    x,y = st_point
    for i in range(4):
        nx, ny = x+dx[i],y+dy[i]
        if nx < 0 or nx >= n or ny<0 or ny >= n:
            continue
        if board[nx][ny] > board[x][y]:
            if board[nx][ny] == end:
                cnt +=1
                return
            dfs([nx,ny])

dfs(st_point)
print(cnt)