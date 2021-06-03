"""

1시간 초과 틀림

9-2

N: 노드 갯수
M: 통로의 갯수
C: 메세지 발사 지점

모든 도시들이 메세지를 받는 시간
--> 모든 도시를 거치는 최솟값 구하기

bfs 로 짧은곳 찾아서 값구하기


"""
from collections import deque
import  heapq

MAX_VALUE = 999999

N,M,C = map(int,input().split())

# N= 5
graph = [[MAX_VALUE]*(N+1) for _ in range(N+1)]
dist = [MAX_VALUE] *(N+1)


# print(graph)

for i in range(M):
    a, b ,c = map(int,input().split())
    graph[a][b]=c




"""
que = deque()

# 시작점, 목표 세팅
que.append(c,0)
dist[c] = 0

while que:
    start ,target = que.popleft()
    distance = 999999999;
    for i in range(graph[start]):
        distance = min(dist[start]+i,distance)
        """


que = []
heapq.heappush(que,(0,C))
dist[c] = 0

while que:

    distance, now =heapq.heappop(que)
    if(dist[now] < distance):
        continue
    for i in graph[now]:
        cost = distance+i[1]
        if cost < distance[i[0]]:
            distance[i[0]]= cost
            heapq.heappush(que,(cost,i[0]))

count = 0

max_distance = 0

for d in dist :
    if d != MAX_VALUE:
        count +=1
        max_distance = map(max_distance,d)


print(count -1 , max_distance)


