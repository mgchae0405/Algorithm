import sys
from copy import deepcopy
# sys.stdin=open("input.txt", "rt")

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def rotate(board):
    new_board = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[j][n-i-1] =  board[i][j]
    return new_board

def move(lst):
    new_lst = []
    for z in lst:
        if z:
            new_lst.append(z)
    4-2-8-0
    for i in range(len(new_lst)-1):
        if new_lst[i] and new_lst[i]==new_lst[i+1]:
            new_lst[i]+=new_lst[i+1]
            new_lst[i+1] = 0
    new_lst2=[]
    for z in new_lst:
        if z:
            new_lst2.append(z)
    [4 2 8] + [0,0,0]
    return new_lst2+[0]*(len(lst)-len(new_lst2))


maxi = -2147000000
def dfs(L,B):
    global maxi
    if L == 5:


        a = max([max(i) for i in B])

        if maxi < a:
            maxi = a
        return
    else:
        for _ in range(4):
            B = rotate(B)
            NB = deepcopy(B)
            for i in range(len(NB)):
                NB[i] = move(NB[i])
            dfs(L+1, NB)

dfs(0,board)
print(maxi)