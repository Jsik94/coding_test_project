"""

https://www.acmicpc.net/problem/4963


시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	24698	12442	8961	49.770%
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

"""
from  collections import deque


#init
visit = deque()
#8방향
move_kind = [ [-1,0],
               [0,1],
               [1,0],
               [0,-1],
              [-1,1],
              [-1,-1],
              [1,1],
              [1,-1]]

def bfs(x,y):
    visit.append((x,y))

    while visit:
        x,y = visit.popleft()

        #8방향 검색

        for i in range(8):
            next_x = x + move_kind[i][0]
            next_y = y + move_kind[i][1]
            print("next cordinate : ", next_x, " * ", next_y)
            if next_x < 0 or next_x >= h or next_y < 0 or next_y >= w :
                continue
            if land[next_x][next_y] == 0:
                continue
             ##방문한곳은 다시못가게 바꿔줌
            if land[next_x][next_y] ==1:
                land[next_x][next_y]=0
                visit.append((next_x,next_y))

#input line

while True:
    w , h = map(int,input().split())
    if w ==0 and h ==0 :
        break
    result = 0
    land = []
    for row in range(h):
        land.append(list(map(int,input().split())))

    for row in range(h):
        for col in range(w):
            if land[row][col] ==1:
                bfs(row,col)
                print(land)
                result +=1

    # output line
    print(result)

