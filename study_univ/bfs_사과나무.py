from collections import deque
import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]


lim = n//2

total = sum([sum(board[i][lim-i:lim+i+1]) for i in range(lim+1)])

total +=sum([sum(board[i][i-lim:n-(i-lim)]) for i in range(lim+1, n)])
print(total)
