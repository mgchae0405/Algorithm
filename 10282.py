import heapq

import sys
sys.stdin=open("input.txt", "rt")
from copy import deepcopy


T = int(input())

for _ in range(T):
    # print()
    # print()
    # print('!!!!!!!!!!!!! T ', T, '!!!!!!!!!!!!!')
    n, d, c = map(int,input().split(' '))

    # print(T,n,d,'시작 : ',c)

    dct = {i: {} for i in range(1,n+1)}

    for _ in range(d):
        x,y,z = map(int,input().split(' '))
        # if not dct:
        #     dct[y] = {x:z}
        # else:
        dct[y][x] = z
    # print(dct)
    # print(len(dct))
    # print('첫 dct!! ',  dct)
    def dijkstra(dct, start):
        dist = {node:float('inf') for node in dct}
        # print('dist, ',dist)
        dist[start] = 0
        queue=[]

        heapq.heappush(queue, [dist[start], start])

        while queue:
            # print('qqqqqqqqqq       ',queue)
            current_dist, current_node = heapq.heappop(queue)
            # print('current_dist, current_node',current_dist, current_node)
            #
            # print('-0----',dct[current_node])
            # print('dist    ',dist)
            # print()
            if dct[current_node]:
                for a,b in dct[current_node].items():
                    now_dist = b+current_dist

                    if now_dist < dist[a]:
                        dist[a] = now_dist
                        heapq.heappush(queue,[now_dist,a])
        return dist



    last_dist = dijkstra(dct,c)
    cnt = 0
    max_dist = 0
    for i in last_dist.values():
        if i != float('inf'):
            cnt +=1
            if max_dist < i:
                max_dist = i

    print(cnt, max_dist)