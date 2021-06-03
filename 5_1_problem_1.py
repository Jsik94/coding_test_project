
"""
DFS
5-1 음료수 얼려먹기

1. 벽은 1 빈공간은 0 으로 표시
2. 빈공간이 상하좌우로 이어진 곳은 하나로봄

출력 얼음 의 갯수


sol. 탐색문제

1. 방문하지 않은 곳 , 빈공간인 곳 시작
1-1. 현재 위치 방문 찍고
2. 상하좌우 탐색 (칸 안에 있고 0인곳) 재귀



"""
#define


move_kind = [ [-1,0],
               [0,1],
               [1,0],
               [0,-1]]


def dfs (x,y):
    global row ,col
    # 범위 맞고 loc ==0 이며 visit [0] 인곳
    if x < 0 or x > row or y < 0 or y > col:
        return False

    #방문 한곳이거나 0 이 아닌 경우
    if visit[x][y] != 0 or loc[x][y] != 0:
        return False

    #방문점 찍고
    visit[x][y] = 1 ;

    for n in range (4):
        next_x = x + move_kind[n][0];
        next_y = y + move_kind[n][1];

        dfs(next_x,next_y)


    #여기까지 온경우 --> 갈수있는 모든 탐색을 마친 경우
    return True;

#input line
row,col = map(int,input().split())

loc =[]

#지형정보
for i in range(row):
    loc.append((list(map(int,input().split()))))



#방문용 좌표
visit = [[0 for j in range(col)] for i in range(row)]


result = 0

for i in range(row):
    for j in range(col):
        if dfs(i,j) == True:
            result +=1



#output line

print(result)

