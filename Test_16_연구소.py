"""
14502







"""

# input 및 변수선언

import copy
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1] 



# 벽
def select_wall(start, count):
    global max_value


    if count == 3:
        sel_maps = copy.deepcopy(maps)
    
        for r in range(N):
            for c in range(M):
                spread(r, c, sel_maps)
        safe_counts = sum(i.count(0) for i in sel_maps)
        max_value = max(max_value, safe_counts)
        return True

    else:
        for i in range(start, N * M): 
            # 좌표 조합 
            r = i // M
            c = i % M
            
            if maps[r][c] == 0: 
                maps[r][c] = 1  
                select_wall(i, count + 1)  
                maps[r][c] = 0


def spread(r, c, sel_maps):
    #q바이러스 dfs
    if sel_maps[r][c] == 2:
        for dir in range(4):
            nx = r + dx[dir]
            ny = c + dy[dir]
            #범위 한 
            if nx >= 0 and nx < N and ny >= 0 and ny < M:  
                if sel_maps[nx][ny] == 0:
                    sel_maps[nx][ny] = 2
                    spread(nx, ny, sel_maps)


#init

N, M = map(int, input().strip().split())

maps = []

for i in range(N):
    L = list(map(int, input().strip().split()))
    maps.append(L)


max_value = 0

select_wall(0, 0)
print(max_value)
