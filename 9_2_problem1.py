"""
34min
9-2

N: 노드 갯수
K: 중간지점
X: 목표지점

각 회사간 거리는 1
K 를 거쳐 X로 가는 최단경로


sol.
1~ k까지 최단 + k ~ X 까지 최단 ==> 플루이드

"""
def floyd (end):
    for k in range(1,end +1):
        for a in range(1,end+1):
            for b in range(1,end+1):
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])




#input line

N , M = map(int,input().split())

graph = [[99999]*(N+1)for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X , K = map(int,input().split())

floyd(M)

answer = graph[1][K]+graph[K][X]

if answer >= 99999:
    print(-1)
else:
    print(answer)



