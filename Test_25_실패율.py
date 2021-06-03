
# 해당 레벨을 도전한 사람의 수
def countChall (level, stages):
    total = len(stages)
    unable = 0
    for i in range(len(stages)):
        if stages[i] <level:
            unable += 1
    total -= unable
    return total


def solution(N, stages):
    # 결과 저장용
    result = []
    #답안용
    answer = []
    for i in range(N):

        tmp = countChall(i+1,stages)
        #스테이지 도전자가 없을 경우
        if tmp ==0 :
            result.append((i+1,0))
        else:
            # 레벨, 각 레벨 실패율 ( 해당스테이지에서 멈춘 사람 / 도전자 수)
            result.append((i + 1,  stages.count(i + 1) / tmp))

    # 실패율 기준으로 오름차순 정렬
    result.sort(key=lambda x: -x[1])

    # 정렬된 리스트 행만 뽑음
    for i in range(N):
        answer.append(result[i][0])


    return answer

N = 7
stages = [2,1,2,6,2,4,3,3]

solution(N,stages)