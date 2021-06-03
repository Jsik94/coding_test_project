"""
https://programmers.co.kr/learn/courses/30/lessons/43162


네트워크
문제 설명
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

제한사항
컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
computer[i][i]는 항상 1입니다.

네트워크의 갯수를 찾아야됨


35분
원인 : 문제 결과값 오인
--> 연결되어있냐 아니냐가 아니라
연결된 네트워크의 갯수를 찾는게 문제였음



"""
#ALL_CONNECT = 1239213

def dfs(current,computers,visit,n,k = 1):

    #해당노드 방문으로 전환
    visit[current] =True

    # #노드가 모두 이어져 있을 시
    # if visit.count(True) == n:
    #     return ALL_CONNECT

    #갈 수 있는 방향 탐색
    for i in range(n):
        # 자기 자신 제외
        if i == current :
            continue
        # 갈 수 있는 간선이 존재 ( 간선이 존재 하고 방문 한적 없는 곳
        if computers[current][i] == 1 and visit[i] == False:
            k= k
            #DFS로 접근이 가능한 경우
            #모두 이어져 나왔을 시
            # if dfs(i,computers,visit,n, k) == ALL_CONNECT :
            #     return ALL_CONNECT
            # 전부는 아니지만 DFS가 적용된 경우에는 있는 값 배출
            #else :
            #return k
            dfs(i,computers,visit,n,k)

    return k

def solution(n, computers):

    visit = [False]*(n)
    answer = 0
    for i in range(n):
        if visit[i] == True:
            continue
        data =dfs(i,computers,visit,n)
        # if data ==ALL_CONNECT :
        #     answer = 1
        #     break
        answer = answer + data
        #visit = [False] * (n)

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(n,computers))