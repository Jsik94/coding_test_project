
"""
DFS
5-4 미로 탈출

1. 벽은 1 빈공간은 0 으로 표시
2. 빈공간이 상하좌우로 이어진 곳은 하나로봄

탈출을 위해 이동한 수를 구하시오


sol. bfs 탐색

1. 시작점 찾기
logic

1. 큐에 넣은 노드를 뺌

2. 뺀노드를 기준으로 인접 노드 큐에 추가

3. 다음 큐에 들어가있는 내용을 1-2 번 과정 수행 ( 큐가 빌때 까지)



"""
def bfs(x,y):
    queue = deque()
    #첫 노드 삽입
    queue.append((x,y))

    #queue 가 빌때까지 진행
    while queue:
        #큐 맨앞에 있는 값을 꺼냄 (기준이 될 데이터 )
        stand_x , stand_y =queue.popleft()

        print("current location : " ,stand_x," *",stand_y)

        for i in range(4):
            next_x = stand_x + move_kind[i][0]
            next_y = stand_y + move_kind[i][1]

            print("next location -> ", next_x, " *", next_y)
            #해당 좌표가 범위를 벗어나는지 벽인지 확인

            if next_x < 0 or next_x >= row or next_y <0 or next_y >= col:
                continue
            if loc[next_x][next_y] == 0:
                continue
            #해당 좌표가 갈 수 있는 곳이라면 큐에 넣음
            if loc[next_x][next_y] ==1:
                print("find next location ---> push !")
                #이동한곳에 이동 가중치 현재경로까지 걸린 거리 +1
                loc[next_x][next_y]=1 + loc[stand_x][stand_y]
                print("distant : " , loc[next_x][next_y])
                queue.append((next_x,next_y))
    return  loc[row-1][col-1]

from collections import deque

#input Line
row ,col = map(int,input().split())

loc = []

for i in range(row):
    loc.append(list(map(int,input())))

move_kind = [ [-1,0],
               [0,1],
               [1,0],
               [0,-1]]






#output line

print(bfs(0,0))


"""
def main():
    x, y = map(int, input().split())
    data = [[0]*y for _ in range(x)]
    for i in range(x):
        temp = list(map(int,input()))
        for j in range(y):
            data[i][j] = int(temp[j])
            #print(data)
            visit = [[0]*y for _ in range(x)]
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            # bfs
            arr = []
            arr.append((0,0))
            visit[0][0] = 1
            while arr:
                a, b = arr.pop(0)
                if a == x-1 and b == y-1:
                    print(visit[a][b])
                    exit()
                for i in range(4):
                    ax = a + dx[i]
                    ay = b + dy[i]
                    if ax>=0 and ax<x and ay>=0 and ay<y:
                        if visit[ax][ay]==0 and data[ax][ay] == 1:
                            visit[ax][ay] = visit[a][b] + 1
                            arr.append((ax, ay))
"""


