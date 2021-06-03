"""
https://www.acmicpc.net/problem/15900

나무 탈출 출처분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초 (추가 시간 없음)	512 MB	1707	745	598	49.016%
문제
평소에 사이가 좋지 않던 성원이와 형석이가 드디어 제대로 한 판 붙으려고 한다. 성원이와 형석이 둘과 모두 똑같이 친한 인섭이가 대결 종목을 정해 가져왔다. 바로 '나무 탈출' 이라는 보드게임이다.

'나무 탈출' 은 N개의 정점이 있는 트리 모양으로 생긴 게임판과 몇 개의 게임말로 이루어진다. 트리의 각 정점에는 1번부터 N번까지 번호가 붙어있다. 1번 정점은 '루트 노드' 라고 불리며, 이 루트 노드를 중심으로 정점 간에 부모-자식 관계가 만들어진다. 자식이 없는 노드는 '리프 노드' 라고 불린다.

이 게임은 두 사람이 번갈아 가면서 게임판에 놓여있는 게임말을 움직이는 게임이다. 처음에는 트리의 모든 리프 노드에 게임말이 하나씩 놓여있는 채로 시작한다. 어떤 사람의 차례가 오면, 그 사람은 현재 존재하는 게임말 중 아무거나 하나를 골라 그 말이 놓여있던 노드의 부모 노드로 옮긴다. 이 과정에서 한 노드에 여러 개의 게임말이 놓이게 될 수도 있다. 이렇게 옮긴 후에 만약 그 게임말이 루트 노드에 도착했다면 그 게임말을 즉시 제거한다. 모든 과정을 마치면 다음 사람에게 차례를 넘긴다. 이런 식으로 계속 진행하다가 게임말이 게임판에 존재하지 않아 고를 수 없는 사람이 지게 된다.


입력
첫째 줄에 트리의 정점 개수 N(2 ≤ N ≤ 500,000)이 주어진다.

둘째 줄부터 N-1줄에 걸쳐 트리의 간선 정보가 주어진다. 줄마다 두개의 자연수 a, b(1 ≤ a, b ≤ N, a ≠ b)가 주어지는데, 이는 a와 b 사이에 간선이 존재한다는 뜻이다.

출력
성원이가 최선을 다했을 때 이 게임을 이길 수 있으면 Yes, 아니면 No를 출력한다.

.
.

sol
1. n 번에서 루트까지의 길이를 구한다

2. 길이가 홀 수면 이김

3. 길이가 짝수면 패배



"""
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def leaf(self):
        if self.next ==None:
            return True
        else :
            return False
    def parents(self):
        if self.prev == None:
            return True
        else:
            return False
"""

"""
def notLeaf(index):
    cnt = 0
    for i in range(n):
        if info[index][i]!=0:
            cnt+=1

    if cnt > 1 :
        return True
    else :
        return False
"""

def dfs(index,height):
    global cnt;

    visit[index] = True
    leaf = True
    weight = height
    #방문한적 없는 노드라면 부모노드일것임

    print("현재 노드: ", index,"가중치 :",weight )

    print(index, " 가 갈 수 있는 노드 경로")
    for i in range((n-1)*2):

        #index와 일치하는 노드 검사
        if info[i][0]==index :
            # 노드가 이동할 다음 노드

            idx = info[i][1]
            print(idx, "info[",i,"][",idx,"]")
            #방문한적이없다면
            if visit[idx]!=True:
                leaf = False
                dfs(idx,weight+1)
        else:
            continue
    if leaf ==True:
        #print("this is leaf node weight :", weight)
        cnt += weight

    #print("--fun end --")
    return weight

#input line


n = int(input())

cnt = 0

#2차원 배열생성
info = []
#리프노드 확인용
visit =[0 for i in range(n+1)]

# 쌍으로 저장
for i in range(n-1):
    a,b =map(int,input().split())
    info.append((a,b))
    info.append((b,a))

print(info)

#a 노드 우선으로 정렬
#info.sort(key= lambda node: node[0])


dfs(1,0)

print(cnt)
#output line

if cnt%2 ==0:
    print("no")
else:
    print("Yes")




