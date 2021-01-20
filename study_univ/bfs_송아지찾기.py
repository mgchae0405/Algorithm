from collections import deque
import sys
#sys.stdin=open("input.txt", "rt")
MAX = 10000
visited = [0]*(MAX+1)
ck = [0]*(MAX+1)
n, m = map(int,input().split())
visited[n] =1
ck[n]=0
q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now==m:
        break
    for i in (now - 1, now + 1, now + 5):
        if 0 < i <= MAX and not visited[i]:

            q.append(i)
            visited[i] = 1
            ck[i]=ck[now]+1
print(ck[m])