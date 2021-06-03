"""

dist 사이 관계식 구함

"""

import sys

#dist vector min
def distance (planet1, planet2):
    x = abs(planet1[0] - planet2[0])
    y = abs(planet1[1] - planet2[1])
    z = abs(planet1[2] - planet2[2])

    return min(x,y,z)

# find root node
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]


# union oper
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a <b :
        parent[b] = a
    else:
        parent[a] =b


N = int(sys.stdin.readline())
# 행성좌표
planet_cord = []
# 하나에 행성에서 갈수 있는 위치와 백터 값을 세트로 저장
route = []
# 트리용
parent = [0]*(N+1)
# 자기 자신 초기화
for i in range(1,N+1):
    parent[i] = i


for i in range(N):
    data = list(map(int,sys.stdin.readline().split()))
    planet_cord.append(data)


#여길 더 줄여야하나 ?
for i in range(N):
    for j in range(N):
        if i == j :
            continue
        dist = distance(planet_cord[i],planet_cord[j])
        route.append((dist,i,j))


route.sort()
result = 0

for edge in route:
    cost , planet1, planet2 = edge

    # 사이클 방지
    if find_parent(parent,planet1) != find_parent(parent,planet2):
        union_parent(parent,planet1,planet2)
        result +=cost

print(result)