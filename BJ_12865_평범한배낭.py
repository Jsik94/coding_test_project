"""


DP[i] --> 무게 i 일대 최대  벨류

수정

DP[i][j] j는 각 가방들의 종류
"""

#init
N,K = map(int,input().split())

weight , value = [] ,[]

for i in range(N):
    data = list(map(int,input().split()))
    weight.append(data[0])
    value.append(data[1])

DP = [[0]* (K+1) for _ in range(N+1)]


#
for i in range(1,N+1):
    for j in range(1, K + 1):


        if j < weight[i-1]:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(value[i-1] + DP[i - 1][j - weight[i-1]], DP[i - 1][j])

print(max(DP[N]))