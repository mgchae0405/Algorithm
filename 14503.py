import sys
from collections import Counter
sys.stdin=open("input.txt", "rt")
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]

n, m= map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
board2 = deepcopy(board)
visited = [[False for _ in range(n)] for _ in range(m)]
# for z in visited:
#     print(z)
# board[r][c] = 'X'
visited[r][c] = True

for k in board:
    print(k)

print()
flg = True
cnt = 0
total = 1
flg2=0
while flg and flg2<20:
    board2[r][c] = 'X'

    #방향만체크
    print('왜에러일까')
    print('r, c =  ', r,c)
    print('d= ',d)
    print('dx[d]= ', dx[d])
    print('dy[d]= ', dy[d])
    print(r + dx[d],c + dy[d])
    print()
    a = board2[r + dx[d]][c + dy[d]]
    board2[r + dx[d]][c + dy[d]] = '방'


    for w in board2:
        print(w)
    print('cnt=',cnt)

    #방향썼던곳 초기화
    board2[r + dx[d]][c + dy[d]] = a


    if cnt == 4:
        r -= dx[d]
        c -= dy[d]
        cnt = 0
        if board[r][c] == 1:
            break

    if not board[r+dx[d-1]][c+dy[d-1]] == 1 and  not visited[r+dx[d-1]][c+dy[d-1]] :
        d -= 1
        if d < 0:
            d = 3
        r += dx[d]
        c += dy[d]
        visited[r][c] = True
        total += 1
        cnt = 0
    elif board[r+dx[d-1]][c+dy[d-1]] == 1 or visited[r+dx[d-1]][c+dy[d-1]]:
        d -= 1
        if d < 0:
            d = 3
        print('벽이네')
        cnt +=1
        continue

    # flg2 +=1
    for i in visited:
        print(i)
    print()


for i in visited:
    print(i)
print()
print(total)


# d -= 1
# if d < 0 :
#     d = 3



# ===================================================
#
# print('test==========test==========test===========test=========')
#
# board[r+dx[d]][c+dy[d]] = 'X'
# print(d)
# for i in board:
#     print(i)
# print()
#
# board[r+dx[d-1]][c+dy[d-1]] = 'X'
# print(d-1)
# for i in board:
#     print(i)
# print()
#
#
# print('----------------------------------------------')
# board2[r][c] = 'O'
#
# board2[r+dx[0]][c+dy[0]] = 'X'
# for i in board2:
#     print(i)
# print()
#
# board2[r+dx[1]][c+dy[1]] = 'X'
# for i in board2:
#     print(i)
# print()
#
# board2[r+dx[2]][c+dy[2]] = 'X'
# for i in board2:
#     print(i)
# print()
#
# board2[r+dx[3]][c+dy[3]] = 'X'
# for i in board2:
#     print(i)
# print()
# #
#
