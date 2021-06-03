"""

퇴사 2

DP [i]  i 까지 계산이 끝난 최대치

"""

import sys

#init
day = int(sys.stdin.readline())

date , schedule =[] , []
DP = [0] * (day+1)


for i in range(day):
    tmp = list(map(int,sys.stdin.readline().split()))
    date.append(tmp[0])
    schedule.append(tmp[1])


"""
마지막날 x
마지막 전날 1 일
1일 day -1 일 

day - i 까지 가능 
"""

for i in range(day):
    # 가능한 날만 DP에 넣음
    if date[i] <= day - i :
        #DP 이동 점 -> 이전에 됏던 날 + 지금 가능한 날을 합친 곳
        #거기 있는 값이랑 지금 dp + 스케줄 값
        DP[i + date[i]] = max(DP[i+date[i]], DP[i]+schedule[i])
    # 가능한 날이 아니면 이전 값 옮겨오기 if 문값과 비교
    DP[i+1] = max(DP[i],DP[i+1])

print(DP[day])