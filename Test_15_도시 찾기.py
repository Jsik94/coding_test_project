
"""
18352
특정 거리의 도시 찾기 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	256 MB	4374	1231	825	30.077%
문제
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

solution

1. bfs로 가되 k 까지만확인

2. list 모아서 출력

"""


from collections import deque
import sys

input = sys.stdin.readline

#init

N, M, K, X = map(int,input().split())


maps = [[] for _ in range(N)]
visit = [False]* (N)


for i in range(M):
    i,j = map(int,input().split())
    maps[i-1].append(j-1)

que =deque()

result = list()
que.append((X-1,0))
visit[X-1]=True

while que:
    loc ,cnt = que.popleft()

    if cnt == K :
        result.append(loc+1)
    elif cnt < K :
        for way in maps[loc]:
            if visit[way] is False:
                visit[way] = True;
                que.append((way,cnt+1))




if len(result) == 0:
    print(-1)
else :
    result.sort()
    for city in result:
        print(city)