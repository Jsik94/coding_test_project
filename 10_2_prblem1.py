"""

35

10-2


같은팀 여부 확인 연산에 대해 Yes or No 출력



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

for i in range(0,n+1):
    par[i] = i;

for i in range(m):
    oper,a,b = map(int,input().split())

    if oper ==0:
        union_parent(par,a,b)
    elif oper ==1:
        # mean cycle
        if find_parent(par,a) == find_parent(par,b):
            print('yes')
        else:
            print('no')