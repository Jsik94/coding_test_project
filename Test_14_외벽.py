def solution(n, weak, dist):
    """
    solution

    사람수 내림차순

    while que:


    dist가 큰 사람부터 모든 weak을 기준으로 dist 계산
    양쪽의 기준을 봐야하므로 forward , backward 둘다 비교

    forward, backward에 기준 weak을 잡고 dist 만큼 계산

    포함되는 범위가 있다면 cnt +1

    issue --> 내가 포함하고 있는 weak 에 대해 어떻게 저장하지 ?


    """
"""
from collections import deque






def solution(n, weak, dist):

    dist.sort(reverse=True)
    dist =deque(dist)

    complete = [True]*n

    for i in weak
        complete[i] = False
    cnt = 0
    while dist:
        target_dist = dist.popleft()
        cnt = cnt +1

        for i in weak :
            # forward case
                forward_range = i + target_dist
            # backward case
                backward_range = n + ( i - target_dist)


    answer = 0


    return answer


#init

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]


solution(n,weak,dist)
"""

