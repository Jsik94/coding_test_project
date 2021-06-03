import heapq


def solution(scoville, K):

    answer = 0
    heap = []

    for i in scoville:
        heapq.heappush(heap,i)

    print(heap)

    while True:

        #일반적인 탈출 조건
        if heap[0] >= K :
            break
        # 남은 원소가 한개다
        if len(heap) < 2:
            answer =-1
            break

        answer += 1
        mixed = heapq.heappop(heap) +heapq.heappop(heap)*2
        heapq.heappush(heap,mixed)

        print("current status :" , answer)
        print(heap)
        print("\n")

    return answer




#test

scoville =[9, 10, 12]
k = 1000

result =  solution(scoville,k)
print(result)