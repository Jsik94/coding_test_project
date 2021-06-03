
"""
구현 문제
4-4 게임 개발


1. 외곽은 무조건 1 - 바다 , 0은 육지이며 , 사용자는 육지만 이동가능하다
2. 사용자는 반시계 방향으로 이동하며, 재귀적으로 탐색함

출력은 방문할 수 있는 갯수


sol. 재귀문제

1. for  - 4방향 탐색을 한다
2. 갈 수 있는 곳이 있다면 현재 위치를 true 로 바꾸고 다시 재귀
3. 4방향 다 갈곳이 없으면 return
"""

#__init__

#이동가능수
global count , location
count = 0

#지형
location =[]

#시계방향 전환 함수
def rotation(cur_location):

    cur_location-=1
    if cur_location<0:
        cur_location =3

    return cur_location


def search(lo_x, lo_y,direction):
    global  count
    #방문점 찍고
    visit[lo_x][lo_y] = 1;

    print(lo_x," , ",lo_y," 지역을 방문하였습니다.")
    print("4지역 탐색을 시작합니다.")

    #4방향 탐색
    for n in range(4):
        #90도 돌리고
        next_dirction = rotation(direction)
        #돌려서 갈 수 있는 예상 좌표

        print("lo : " , lo_x," , ",lo_y)
        print("move : " , move_kind[next_dirction][0]," , ",move_kind[next_dirction][1])
        next_loc_x = lo_x + move_kind[next_dirction][0]
        next_loc_y = lo_y + move_kind[next_dirction][1]
        print("예상 좌표 : " , next_loc_x," , ",next_loc_y)
        # 예상좌표가 육지이며 , visit이 =0 이면 count +1 재귀
        print("------------------------------------------")
        print("지형 : " , location[next_loc_x][next_loc_y])
        print("방문 : " , visit[next_loc_x][next_loc_y])
        print("------------------------------------------")

        if location[next_loc_x][next_loc_y] ==0 and visit[next_loc_x][next_loc_y]==0:
            count+=1
            print(n,"번째 탐색 도중 가능 지역을 찾았습니다. 이동합니다.")
            search(next_loc_x,next_loc_y,next_dirction)
        direction = next_dirction
    return 0

#북 동 남 서 방향
move_kind = [ [-1,0],
               [0,1],
               [1,0],
               [0,-1]]


#__input line __

#블록 입력
block_x, block_y = map(int,input().split())

#캐릭터 좌표 , 방향
loc_x ,loc_y , direc = map(int,input().split())

#방문용 좌표 생성
visit = [[0 for col in range(block_y)] for row in range(block_x)]

#지형 입력
"""
    자료형 넣을때 list 형태로 넣을것 
"""
for i in range(block_x):
    location.append(list(map(int,input().split())))




if location[loc_x][loc_y] ==0:
    count+=1;
    print("첫 좌표는 방문이 가능합니다 이동 지역이 추가되었습니다.")

search(loc_x,loc_y,direc)

#output line

print(" < ---- answer  ---- >")
print(count)