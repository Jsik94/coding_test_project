"""


N 정사각 보드

뱀 초기길이 1

뱀의 이동규칙
-첫 시작은 오른쪽
-매초마다 이동
-해더를 다음칸에 이동

--> 다음칸에 사과가 존재하면 , 사과만 사라짐

--> 다음칸에 사과가 없다면 , 꼬리가 위치한 칸을 비움


게임 종결 조건
1. 벽을 만난다.
2. 자기몸과 부딪힌다

"""

from collections import deque


def next_move(way, direction):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    if direction == 'L':
        way -= 1
    elif direction == 'D':
        way += 1

    if way < 1:
        way = 4
    elif way > 5:
        way = 1

    if way == 1:
        return dx[0], dy[0], way
    elif way == 2:
        return dx[1], dy[1], way
    elif way == 3:
        return dx[2], dy[2], way
    elif way == 4:
        return dx[3], dy[3], way


def end_condition(cur_x, cur_y):
    # 자기 몸 or 벽인지 확인
    if 0 < cur_x < N + 1 and 0 < cur_y < N + 1:
        if table[cur_x][cur_y] != snake_code:
            return True
        else:
            return False
    else:
        return False


N = int(input())
K = int(input())

table = [[0] * (N + 1) for _ in range(N + 1)]
rule = []
snake_code = 'Z'
time_score = 0
"""
way 시계 방향 
1- 오른쪽
2- 아래쪽
3- 왼쪽
4- 위쪽
"""
way = 1
snake = deque()
loc_x, loc_y = 1, 1

for i in range(K):
    x, y = list(map(int, input().split()))
    table[x][y] = 1

L = int(input())

for i in range(L):
    time, direction = input().split()
    rule.append((int(time), direction))

table[1][1] = snake_code
snake.append((1, 1))

while True:
    time_score += 1

    direction = 'S'

    # 방향 규칙이 있나 확인
    for i in rule:
        if i[0] == time_score-1:
            direction = i[1]

    # print("--- Current Status ---")
    # print("현재 ", time_score,"초 진행중")
    dx, dy, way = next_move(way, direction)

    nx = loc_x + dx
    ny = loc_y + dy

    snake.append((nx, ny))

    if end_condition(nx, ny):
        # 사과가 없으면
        if table[nx][ny] == 0:
            # print("사과없음")
            tx, ty = snake.popleft()
            table[tx][ty] = 0


    else:
        print(time_score)
        break

    table[nx][ny] = snake_code

    loc_x = nx
    loc_y = ny
