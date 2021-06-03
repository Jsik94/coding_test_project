"""

almost 1 ->못품

10-3


두마을로 쪼개되 비용이 최소로 되도록


1. 가장 비용이큰 놈 하나를 짜르고
2. 나머지 유니온

--> 모두 유니온 한다음에 큰놈하나 빼면됨


"""

# find root node
def find_parent(parent,x):

    if par[x] !=x:
        parent[x] = find_parent(parent,x)

    return par[x]


# union oper
def union_parent(parent,a,b):
    a = find_parent(par,a)
    b = find_parent(par,b)

    if a <b :
        par[b] = a
    else:
        par[a] =b


n,m = map(int,input().split())

par = [0] * (n+1)
edges = []

for i in range(0,n+1):
    par[i] = i

for i in range(m):
    a,b,c = map(int,input().split())
    #비용순으로 정리할 것이므로
    edges.append((c,a,b))

result =0

# 정리
edges.sort()
last = 0

for edge in edges:
    c,a,b = edge
    if find_parent(par,a) !=find_parent(par,b):
        union_parent(par,a,b)
        result += c
        last = c


print(result-last)