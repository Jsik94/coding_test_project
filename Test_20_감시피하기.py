"""

0 세울수 있는곳
1 학생
2 선생
3 벽을 세워 막을 수 있는 곳
4 벽을 세워도 못막는 곳


"""
#상하 좌우
dx = [-1,1,0,0]
dy = [0 ,0,-1,1]

def check_student(cord,type=8):
    x,y = cord
    toggle =True
    # 선생이 선택되면 4방향을 모두 봐야함
    if type == 8:
        for way in range(4):
            nx = x +dx[way];
            ny = y +dy[way];
            # 맵 영역
            if ( nx >= 0 and nx <N and ny >=0 and ny < N):

                # 학생을 만나면 바로 break 돌리는게 의미없음
                if(maps[nx][ny]==1):
                    toggle =False
                    break;
                #학생을 만나지 않았고 벽을 만났다면 막은거니 다른 방향 확인
                elif (maps[nx][ny]==3):
                    continue
                #나머지 경우는 진행
                else:

                    if check_student((nx,ny),way) == False:
                        toggle =False

        if toggle:
             return True
        else:
             return False


        # 재귀용 단방향성
    else:
        nx = x + dx[type]
        ny = y + dy[type]
        if (nx >= 0 and nx < N and ny >= 0 and ny < N):

            # 학생을 만나면 바로 False
            if (maps[nx][ny] == 1):
                return False
            # 학생을 만나지 않았고 벽을 만났다면 막은거니 True
            elif (maps[nx][ny] == 3):
                return True
            # 나머지 경우는 진행
            else:
                return check_student((nx, ny), type)



def setwall (cnt):
    final = False
    toggle =True
    #벽 3개를 세웠을 때
    if cnt == 3 :
        #check_map()
        # 조사

        for cord in teacher_loc:
            if check_student(cord) ==False:
                return False

        # 여기까지 오면 check 걸린것 없음
        return toggle
    else :

        for i in range(N):
            for j in range(N):
                #벽인 곳만 세움
                if(maps[i][j] == 0 ):
                    maps[i][j] = 3;
                    cnt +=1
                    if setwall(cnt):
                        toggle = True
                        return toggle
                    maps[i][j] = 0;
                    cnt -=1

    return False

#init
N = int(input())

maps = []
teacher_loc = []
for i in range(N):
    data = list(input().split())
    trans = []
    for j in range(len(data)):
        if data[j] == 'X':
            trans.append(0)
        elif data[j] == 'S':
            trans.append(1)
        elif data[j] == 'T':
            teacher_loc.append((i,j))
            trans.append(2)
    maps.append(trans)



if setwall(0):
    print("YES")
else:
    print("NO")








#
# maps[0][3] = 3
# maps[1][1] = 3
# maps[2][2] = 3
# check_map()

# print(maps[1][4]==1)
# K = 0
#
# for cord in teacher_loc:
#     K+=1
#     if check_student(cord,8) ==True:
#         print(K,"번 선생 아무도 못봄")
#     else:
#         print(K,"번 선생 학생 적발")
