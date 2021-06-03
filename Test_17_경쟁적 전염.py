"""

 
 """



#
# def spread(N):
#

# # 바이러스 원점 검색
#     for x in range(N):
#         for y in range(N):
#             # 빈곳은 통과
#             if maps[x][y] == 0:
#                 continue
#             else:
#                 data.append((maps[x][y],x,y))
#
#     sorted(data)
#
#     while data:
#         virus_level, x,y  = data.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 범위 확인
#             if nx >= 0 and nx < N and ny >= 0 and ny < N:
#                 # 아예 없거나 바이러스 우선순위가 높은 (번호가 낮은) 것부터 이동
#
#                 if maps[nx][ny] == 0:
#                     maps[nx][ny] = virus_level
#
#



from collections import deque
import  sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def show_stat(N):
    for i in maps:
        for j in i:
            print(j, end='')
        print()


#init

N, K = map(int,input().split())

maps = []
data =deque()

for i in range(N):
    maps.append(list(map(int,input().split())))


time, X, Y = map(int,input().split())


cnt = 0

#초기 위치 확인
for x in range(N):
    for y in range(N):
        # 빈곳은 통과
        if maps[x][y] == 0:
            continue
        else:
            data.append((maps[x][y], x, y,cnt))

#바이러스 레벨 조절
sorted(data)

while data:
    #해당 바이러스 레벨 , 좌표 , 현재 시간
    virus_level, x, y,cnt = data.popleft()

    #time에 제동
    """
    ㄴcnt 가  time 되는 상황이 1번바이러스까지임 
    
    """
    # if cnt < time+1 :
    #     break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 확인
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            # 아예 없거나 바이러스 우선순위가 높은 (번호가 낮은) 것부터 이동
            if maps[nx][ny] == 0:
                maps[nx][ny] = virus_level
                data.append((maps[nx][ny],nx,ny,cnt+1))





print(maps[X-1][Y-1])