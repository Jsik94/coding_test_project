
import sys

def Floyid (n, maps , visit):
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if maps[i][j] > maps[i][k]+maps[k][j]:
                    maps[i][j] = maps[i][k]+maps[k][j];
                    visit[i][j] = k;


n = int(input())
m = int(input())

INF = 1<<20
maps = [[INF]* (n+1) for _ in range(n+1)]
visit = [[0]* (n+1) for _ in range(n+1)]

# 자기자신은 0
for i in range(1,n+1):
    maps[i][i] = 0

for i in range(m):
    data = list(map(int,input().split()))
    maps[data[0]][data[1]] = min(data[2],maps[data[0]][data[1]])


Floyid(n,maps,visit)

for i in range(1,n+1):
    for j in range(1,n+1):
        if maps[i][j] == INF:
            print("0",end=' ')
        else:
            print(maps[i][j],end=' ')

    print("")

# for i in range(1,n+1):
#     for j in range(1,n+1):
#
