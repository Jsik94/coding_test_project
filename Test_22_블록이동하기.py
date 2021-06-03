

"""
90도 돌릴수 있는 경우의 수

중심 좌표를 기준

case 1:
        0 0
        0 1
        -> (-1,-1), (-1,0) , (0,-1)
case 2:
        0 1
        0 0
        -> (0,-1), (1,-1) ,(1,0)
case 3:
        0 0
        1 0
        -> (-1,0), (-1,1),(0,1)
case 4:
        1 0
        0 0
        -> (0.1),(1,1) ,(1,0)
"""

from collections import deque

case = [[(-1,-1), (-1,0) , (0,-1)],[(0,-1), (1,-1) ,(1,0)],[(-1,0), (-1,1),(0,1)],[(0.1),(1,1) ,(1,0)]]

def bound (maps,x,y):
    if (x>0 and x <= N and y>0 and y <=N):
        if (maps[x][y]==0):
            return True
    return False


def check_rotate(cord):
    x,y = cord
    for way in case:
        toggle =True
        for cordinate in way:
            dx,dy = cordinate
            nx = x +dx
            ny = y +dy
            #하나라도 바운더리에 들어가지 않는다면 아웃
            if bound(nx,ny) is False :
                toggle= False
                break;
        #True 라면회전 가능



def solution (board):
    N = len(board)
    maps=[[]*(N+1) for _ in range(N+1)]
    visit=[[]*(N+1) for _ in range(N+1)]

    #init
    for i in range(N):
        for j in range(N):
            maps[i+1][j+1] = board[i][j]

    """
    현재 head와 tail을 que 에 넣고
        4방향 탐색 이동
            이동 조건 
                1) 범위 안에 head와 tail이 모두 들어와야함
        
        4방향을 이동해도 방법이 없을경우 회전
            회전 조건
                case 4개중 1개 만족해야함        
    
    """



    answer=0


    return answer


