"""


등수가 낮을 수록 진입차수가 높아짐( 위에서 모두 접근이 가능)

위상정렬 관계를 세우고
노드를 모두 돌때까지 bfs



"""

from  collections import deque



case = int(input())

for i in range(case):
    num = int(input())
    Node = list(map(int,input().split()))

    problems = int(input())
    dic = {}

    #관계식 생성
    relation = [0 for _ in range(num+1)]
    for i in range(num):
        relation[Node[i]] = [x for x in Node[i:] if x!=Node[i]]
        if relation[Node[i]] == []:
            relation[Node[i]] = [0]

    #print(relation)


    change_nodes = []
    for j in range(problems):
        data = list(map(int,input().split()))

        # print("\ndata :",data)
        # print("data[0] 이 가지고 있는 위상 : ",relation[data[0]])
        if data[1] in relation[data[0]]:
            # print("작년과 같은 데이터입니다.")
            a = 0
        else:
            # print("다른 데이터")
            #위상 변경
            relation[data[0]].append(data[1])
            relation[data[1]].remove(data[0])
            # print("data[0] 이 가지고 있는 위상 : ", relation[data[0]])
            # print("data[1] 이 가지고 있는 위상 : ", relation[data[1]])


    print("\n딕셔너리 완성")
  #차수 정렬
    for j in range(1,num+1):
        dic[num-len(relation[j])-1] = relation[j]

    dic = sorted(dic.items())



    print(dic)
    print("\n릴레이션 데이터")
    print(relation)
    # print(list(dic[0]))



    que = deque()

    que.append(list(dic[0])[1])

    """
    que 에 들어가야하는 정보
    
    현재 노드 위치
    
    안에서 해야하는 작업
    
    if node 갯수 -1 만큼 움직이면 break 
    
    현재 노드위치 off 
    현재 노드에서 갈 수 있는 노드 선택하여 que 에 삽입
    
    
    
    """

    while que:
        movable = que.popleft()





