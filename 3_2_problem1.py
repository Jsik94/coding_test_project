

"""
그리디 알고리즘
3-2 숫자 카드 게임

n , k 행렬에서 가장 높은 카드를 뽑되, 아래와 같은 룰을 통해 뽑는다

1. 행을 고르고 카드를 선택하며, 고른 행에서 가장 낮은 수를 선택한다.

2. 그 가장 낮은 숫자가 최종적으로 높아야한다.


sol.
결론적으로 가장 높은 숫자를 뽑으려면 고르려는 행이 가장 숫자가 낮은 것들중에서 높아야함

줄에서 최솟값들 중 최대하나를 선택

"""


#input line
n , k = map(int,input().split())

result = 0

for i in range(k):
    data = map(int,input().split())
    line_data = min(data)
    if result < line_data:
        result = line_data


#output line


print(result)