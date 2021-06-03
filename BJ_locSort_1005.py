"""

https://www.acmicpc.net/problem/1005

ACM Craft 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	512 MB	39676	7441	4794	21.319%
문제
서기 2012년! 드디어 2년간 수많은 국민들을 기다리게 한 게임 ACM Craft (Association of Construction Manager Craft)가 발매되었다.

이 게임은 지금까지 나온 게임들과는 다르게 ACM크래프트는 다이나믹한 게임 진행을 위해 건물을 짓는 순서가 정해져 있지 않다. 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다. 매 게임시작 시 건물을 짓는 순서가 주어진다. 또한 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay가 존재한다.


42분 -- 시간초과


"""
from collections import deque


def topology_sort():
    que = deque()

    # que 에 넣되 결과엔 시간 삽입
    # 0번차수 스타트 셋업
    for i in range(1, N + 1):
        if indegree[i] == 0:
            que.append(i)
            result[i] = time[i]

    while que:
        now = que.popleft()
        #현재 가지고 있는 노드의 rule 을 찾아 비교
        for i in rule[now]:
            indegree[i] -= 1
            result[i] = max(result[now] + time[i], result[i])
            if indegree[i] == 0:
                que.append(i)


Case = int(input())

for i in range(Case):
    N, K = map(int,input().split())



    #위상 정렬 진입차수 , 걸리는 시간 , 건설 규칙 , 결과 메모제이션
    indegree = [0] * (N+1)
    time = [0] * (N+1)
    rule = [[0] for _ in range(N+1)]
    result = [0]*(N+1)

    time = [0]+list(map(int,input().split()))

    #규칙 차수 셋업
    for i in range(K):
        X,Y = map(int,input().split())
        rule[X].append(Y)
        indegree[Y] +=1

    topology_sort()
    target = int(input())
    print(result[target])




