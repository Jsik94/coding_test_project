"""


N ,M , K



"""

#init

N,M,K = map(int,input().split())

maps = [[0]* (M+1) for _ in range(N+1)]
maps[1][1] = 1;
result = 0



for i in range(1,N+1):
    for j in range(1,M+1):
        #init
        if i ==1 and j == 1:
            continue
        # 중간점이 없다면
        if K ==0 :
            maps[i][j] = maps[i - 1][j] + maps[i][j - 1]
        else :
            mid_x = K // M + 1
            mid_y = K % M

            if K % M == 0 :
                mid_x = mid_x -1
                mid_y = M

            # 첫번째 영역
            if 0<= i <= mid_x and 0 <= j <= mid_y :
                maps[i][j] = maps[i - 1][j] + maps[i][j - 1]
                if i == mid_x and j ==mid_y :
                    result = maps[mid_x][mid_y]
                    maps[mid_x][mid_y] = 1
            # 두번째 영역
            elif (mid_x <= i <= N and mid_y <= j <= M):
                maps[i][j] = maps[i - 1][j] + maps[i][j - 1]
            else:
                continue

if K != 0:
    result = result *maps[N][M]
else :
    result = maps[N][M]

print(result)
