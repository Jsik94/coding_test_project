"""

다수의 치킨 집중 M 개를 고르고

M개와 home 의 값중 최소


"""
from itertools import combinations

N, M = list(map(int, input().split()))

table = [[0] * N for _ in range(N)]

"""
집 , 치킨집 좌표 저장용
조합 열거용
결과 저장용
"""
home, chicken, kind, result = [], [], [], []

for i in range(N):
    table[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if table[i][j] == 1:
            home.append((i, j))
        elif table[i][j] == 2:
            chicken.append((i, j))

# 조합
kind = list(combinations(chicken, M))

# 조합중에
for chicken_set in kind:
    tmp = 0
    # 집과 모두 비교
    for j in home:
        mini = 2e99
        for chick in chicken_set:
            dist = abs(chick[0] - j[0]) + abs(chick[1] - j[1])
            mini = min(mini, dist)

        tmp += mini
    result.append(tmp)

#print(result)
print(min(result))
