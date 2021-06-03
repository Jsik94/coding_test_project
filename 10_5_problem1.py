"""

10-3

N개 의 강의 나열

강의 걸리는 시간 , 선수강 강의 -1은 마무리


"""


n = int(input())

info = [[]for _ in range(n+1)]
latency=[0] * (n+1)
par=[0] * (n+1)


for i in range(n+1):
    par[i] = i

# 위치 맞추기위해 1로 재조정
for i in range(1,n+1):
    data = list(map(int,input().split()))
    latency[i] = data[0]
    for k in data[1:-1]:
        if k == -1:
            break
        par[i] = k



print(par)