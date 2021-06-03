"""


상어는 2부터 시작

상어크기보다 작은놈만 먹을 수 있음

같으면 통과만 가능 ㅇㄹ마ㅣㄴ어라ㅣ


"""

from collections import deque

import sys

input = sys.stdin.readline

#상하좌우
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

maps =[]

def bfs(x, y, weight, timer, eat):

    # while 종결
    toggle =True
    q, can_eat = deque(), []
    q.append([x, y])
    timetable = [[-1]*N for _ in range(N)]
    #현재위치
    timetable[x][y] = timer
    while q:
        #갈수있는 방향
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위
                if 0 <= nx < N and 0 <= ny < N:
                    #간적이 없고
                    if timetable[nx][ny] == -1:
                        #맵에 없거나 일단 갈 수 있는 곳 크기가 같은곳
                        if maps[nx][ny] == 0 or maps[nx][ny] == weight:
                            timetable[nx][ny] = timetable[x][y] + 1
                            q.append([nx, ny])
                        #먹을 수 있는 곳
                        elif 0 < maps[nx][ny] < weight:
                            can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            # 먹고 크기 증가
            if eat == weight-1:
                eat = 0
                weight += 1
            maps[nx][ny] = 0
            return nx, ny, weight, timetable[x][y] + 1, eat, toggle

    #먹을게 없다면
    print(timer)
    toggle =False
    return nx, ny, weight, timetable[x][y] + 1, eat , toggle


N = int(input())

for _ in range(N):
    maps.append([list(map(int, input().split()))])

for i in range(N):
    for j in range(N):
        if maps[i][j] == 9:
            x, y = i, j
            maps[i][j] = 0

weight, timer, eat = 2, 0, 0

while True:
    x, y, weight, timer, eat , toggle = bfs(x, y, weight, timer, eat)

    if toggle is False:
        break;