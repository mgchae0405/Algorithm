import heapq

graph = {
    'A':{'B':8, 'C':1, 'D':2},
    'B':{},
    'C':{'B':5, 'D':2},
    'D':{'E':3, 'F':5},
    'E':{'F':1},
    'F':{'A':5}
}


def dijkstra(graph, start):
    dist = {node:float('inf') for node in graph}
    dist[start] = 0
    queue=[]

    heapq.heappush(queue,[dist[start], start])

    while queue:
        current_dist , current_node = heapq.heappop(queue)

        # 지금까지 찾은 거리가 어차피 가장 짧다면 !?
        if dist[current_node] < current_dist:
            continue

        # ex) 노드가 A일 때, 그 value가 또 하나의 dict이기 때문에 아래와 같은 for문 생성
        for adjacent, weight in graph[current_node].items():
            distance = current_dist+weight

            # 새로운 값이 더 최단거리라면 !?
            if distance < dist[adjacent]:
                dist[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return print(dist)

if __name__ =='__main__':
    dijkstra(graph, 'A')