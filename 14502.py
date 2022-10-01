import sys
sys.stdin=open("input.txt", "rt")
from copy import deepcopy


n,m = map(int,input().split(' '))

board = [list(map(int,input().split())) for _ in range(n)]

# board = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]


two_lst = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            two_lst.append([i,j])
# print(two_lst)


flg = 0
max_val = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]




def dfs2(board, k,l,virused):
    for _ in range(4):
        nx = k + dx[_]
        ny = l + dy[_]
        # print(nx,ny)
        if nx <0 or ny <0 or  nx >= n or ny >= m:
            continue
        if not board[nx][ny] and not virused[nx][ny]:
            board[nx][ny] = 2
            virused[nx][ny] = True
            # for kkk in board:
            #     print(kkk)
            dfs2(board, nx,ny,virused)






def dfs(board, visited, flg):
    global max_val
    for i in range(n):
        for j in range(m):
            if not board[i][j] and not visited[i][j]:
                board2 = deepcopy(board)

                board2[i][j] = 'f'
                visited[i][j] = True
                # for kk in board2:
                #     print(kk)
                # print()
                if flg<2:
                    dfs(board2,visited,flg+1)
                else:
                    cnt=0

                    virused = [[False] * m for _ in range(n)]
                    board3 = deepcopy(board2)
                    for k, l in two_lst:

                        virused[k][l] = True
                        dfs2(board3, k, l,virused)


                    for kk in board3:
                        cnt+=kk.count(0)
                        # print(kk)
                    # for kk in board2:
                    #     cnt+=kk.count(0)
                    #     print(kk)
                    #     # print(kk.count(0))
                    if cnt> max_val:
                        max_val = cnt
                    # print(cnt)
                    # print()

                visited[i][j] = False


dfs(board,visited,flg)
print(max_val)


#
# virused = [[False] * m for _ in range(n)]
#
# for k,l in two_lst:
#     board3 = deepcopy(board2)
#     virused[k][l] = True
#     dfs2(board3, k, l)
#
#
#     print(k,l)
#     for _ in range(4):
#         nx = k + dx[_]
#         ny = k + dy[_]
#         if nx > n or ny > m:
#             continue
#         if not board[nx][ny] and not virused[nx][ny]:



#
# for i in range(n):
#     for j in range(m):
#         if not board[i][j]:
#             board2 = deepcopy(board)
#             board2[i][j] = 'f'
#             visited[i][j] = True
#             for z in range(n):
#                 for w in range(m):
#                     if not board2[z][w] and not visited[z][w]:
#                         board2[z][w] = 's'
#                         visited[z][w] = True
#                         for k in range(n):
#                             for h in range(m):
#                                 if not board2[k][h] and not visited[k][h]:
#                                     board2[k][h] = 't'
#                                     visited[k][h] = True
#                                     for kk in board2:
#                                         print(kk)
#                                     print()
#                                     board2[k][h] = 0
#                                     visited[k][h] =  False
#                         board2[z][w] = 0
#                         visited[z][w] = False
#             board2[i][j] = 0
#             visited[i][j] = False




