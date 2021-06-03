"""
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[[ICN, JFK], [HND, IAD], [JFK, HND]]	[ICN, JFK, HND, IAD]
[[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]	[ICN, ATL, ICN, SFO, ATL, SFO]
입출력 예 설명
예제 #1

[ICN, JFK, HND, IAD] 순으로 방문할 수 있습니다.

예제 #2

[ICN, SFO, ATL, ICN, ATL, SFO] 순으로 방문할 수도 있지만 [ICN, ATL, ICN, SFO, ATL, SFO] 가 알파벳 순으로 앞섭니다.



sol 1.

알파벳순 정렬




"""
from collections import deque
import copy


#다음 출발지를 찾는 함수
def next(tickets,next_start):
    #도착지를 저장할 리스트
    finder = ["a","a"]

    #검색
    for i in tickets:
        if i[0] == next_start:
            #아스키 코드가 더 작은 (알파벳 우선순) 비교 저장
            if ord(i[1][0]) < ord(finder[1][0]):
                finder = i

    #하나도 못찾았을 경우 []으로 리턴
    if finder ==["a","a"]:
        return [] ;

    result = copy.deepcopy(finder)

    # 사용한 티켓 제거
    tickets.remove(result)
    # 도착지(=다음 출발지)만 반환
    return result[1]

def solution(tickets):

    answer=[]

    #init
    start = "ICN"
    dest = next(tickets,start)
    answer.append("ICN")
    answer.append(dest)

    # 경로 전환용
    toggle = False
    # 임시 저장용 리스트
    buff =[]

    # 티켓을  다쓸때 까지 진행
    while tickets :
        start = dest
        dest = next(tickets,start)

        if toggle:
            #지금까지 찾았던 경로를 버퍼에 저장해두고
            #ICN 부터 시작함
            buff=buff + (answer[1:])
            answer = ["ICN"]
            toggle = not toggle


        if dest ==[] :
            # 티켓으로 더 이상 도착지로 갈 수 없는 경우
            # 토글 활성
            toggle = not toggle
            dest= "ICN"

        else:
            answer.append(dest)

    #임시 저장된것이 있다면 뒤에 삽입
    if buff is not []:
        answer= answer +buff
    return answer




#tickets = [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]
# tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
# tickets= [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(tickets[0][0])
result = solution(tickets)

print(result)




"""
삽질했던 코드의 흔적

    #
    # answer.append(tickets[0][0])
    # answer.append(tickets[0][1])
    # tickets.pop(0)
    #
    # while tickets :
    #     #출발지 도착지
    #     #current_start , current_dest = que.popleft()
    #     #ways =[]
    #     #현재 도착지가 출발지인 나머지 ways 에 저장
    #     tmp = list(copy.deepcopy(tickets))
    #     # print(tmp)
    #     # print(len(tmp))
    #     # for i in len(tmp):
    #     #     if tmp[i][0] == current_dest:
    #     #         ways.append(tmp[i])
    #     #         answer.append(tmp[i][1])
    #     #         tickets.pop(i)
    #     #
    #     #
    #     # ways.sort()
    #     while que:
    #         current_start, current_dest = que.popleft()
    #         for i
    #
    #

"""