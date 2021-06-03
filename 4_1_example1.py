"""
구현문제
4-1 상하 좌우

N*N 행렬이 존재할 떄

입력에 따라 이동한 최종 좌표를 출력하시오


sol
입력받은 값에 따라 이동 단 범위를 벗어나는 구간은 무시할 것

입력값과 매핑되는 좌표를 찾아 넣고 해당시 누적치를 계산

범위가 초과하는지 확인하고 이상없으면 저장


"""

#init

result_cord = [1,1]

# 상 하 좌 우
cord = [ [-1,0],
         [1, 0],
         [0,-1],
         [0,1]]

#입력 매핑용
pointer = ['U','D','L','R']

#input line
n = int(input())

pointers = input().split()

for loc in  pointers:
    move_cord = [0, 0]
    for i in range(len(pointer)):
        if loc == pointer[i]:
            move_cord[0] = cord[i][0] + result_cord[0]
            move_cord[1] = cord[i][1] + result_cord[1]

    if move_cord[0] < 1 or move_cord[0] > n or move_cord[1] < 0 or move_cord[1] > n:
        continue

    result_cord[0] = move_cord[0]
    result_cord[1] = move_cord[1]


#output line

print(result_cord[0],result_cord[1])