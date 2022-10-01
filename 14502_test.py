board = [[0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 2],[1, 1, 1, 0, 'f', 2],[0, 'f', 'f', 0, 0, 2]]

virused = [[False] * 6 for _ in range(4)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]


for kk in board:
    print(kk)




two_lst = []
for i in range(4):
    for j in range(6):
        if board[i][j] == 2:
            two_lst.append([i,j])

for k,l in two_lst:
    for _ in range(4):
        nx = k + dx[_]
        ny = l + dy[_]
        if nx >= 4 or ny >= 6:
            continue
        print('2',nx,ny)
        if not board[nx][ny] and not virused[nx][ny]:
            board[nx][ny] = 2
            virused[nx][ny] = True

            for aa in board:
                print(aa)






def dfs2(board, k,l,virused):
    for _ in range(4):
        nx = k + dx[_]
        ny = l + dy[_]
        # print(nx,ny)
        if nx <0 or ny <0 or  nx >= 4 or ny >= 6:
            continue
        if not board[nx][ny] and not virused[nx][ny]:
            board[nx][ny] = 2
            virused[nx][ny] = True
            # for kkk in board:
            #     print(kkk)
            dfs2(board, nx,ny,virused)

virused = [[False] * 6 for _ in range(4)]

for k, l in two_lst:
    board3 = deepcopy(board)
    virused[k][l] = True
    dfs2(board3, k, l,virused)