
import heapq

def Dijkstra(start):
    q=[]
    heapq.heappush(q,[0,start])
    result=[INF for _ in range(n+1)]
    result[start]=0
    while q:
        dis,idx=heapq.heappop(q)
        # 거리가 크면 넘김
        if dis>result[idx]:
            continue
        for d,x in maps[idx]:
            d+=dis
            if d<result[x]:
                result[x]=d
                heapq.heappush(q,[d,x])
    return result



#init

n , k = int(input().split())
INF = 2 <<20;

maps = [[]for _ in range(n+1)]

for i in range(k):
    data = list(map(int,input().split()))
    maps[data[0]].append([data[1],data[2]])
    maps[data[1]].append([data[0],data[2]])


start , end = int(input().split())


