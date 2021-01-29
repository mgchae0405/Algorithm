import sys
sys.stdin=open("input.txt", "rt")

dx = [0,0,1]
dy = [1,-1,0]

board = [list(map(int,input().split()))for i in range(10)]


def dfs(x,y,k):
    if x == 9:
        if board[x][y] ==2:
            return print(k)
        else:
            return

    for i in range(3):
        nx,ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >=10 or ny < 0 or ny >= 10 :
            continue
        if (i ==0 or i == 1) and board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny,k)
            break
        elif i == 2 and board[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, k)



for i in range(10):
    if board[0][i]:
        visited = [[0] * 10 for _ in range(10)]
        visited[0][i] = 1
        dfs(0,i,i)