import heapq

queue = []

heapq.heappush(queue, [2,'A'])
heapq.heappush(queue, [5,'B'])
heapq.heappush(queue, [1,'C'])
heapq.heappush(queue, [7,'D'])
heapq.heappush(queue, [3,'E'])

# 트리구조 형태이기 때문에 헷갈릴 수 있다.
print(queue)


#sorting되어있는 데이터 확인
for _ in range(len(queue)):
    print(heapq.heappop(queue))