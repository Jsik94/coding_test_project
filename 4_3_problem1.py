"""
구현문제
4-3 왕실의 나이트

8*8 행렬이 존재할 떄

시작 위치에서 나이트가 이동할 수 있는 경우의 수를 출력하라


sol
상하좌우처럼 ㅇ8가지 경우의 수 중  체스판을 벗어나지 않는 범위만 count


"""

#init

count = 0

#경우의 수 8 가지
cord = [ [-2,1],[-2,-1],
         [2, 1],[2,-1],
         [1,-2],[-1,-2],
         [1,2],[-1,2]]


#input line
cur_cord = input()

# 시작은 1,1
x = ord(cur_cord[0]) - ord('a')+1
y = int(cur_cord[1])

for n in range(len(cord)):
    tmp_x = x + cord[n][0]
    tmp_y = y + cord[n][1]
    if tmp_x > 0 and tmp_x < 9 and tmp_y > 0 and tmp_y < 9 :
        count+=1

#output line
print(count)