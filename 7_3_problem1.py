"""

7-3 부품찾기

1. n을 입력받고 다음 줄에 n만큼 숫자를 받음
2. M만큼 입력받고 다음 줄에 m만큼 숫자를 받음
3. M이 있는지 각각 확인하여 yes , no 출력


sol.
1. 이진탐색


2. 파이썬 특징 사용


"""


n = int(input())

data = list(map(int,input().split()))

m = int(input())
target = list(map(int,input().split()))

## 1
def binary (data,result,start,end):
    if start > end :
        return None

    mid = (start+end)//2

    if(data[mid] == result):
        return mid

    elif data[mid] > result:
        return binary(data,result,start,mid-1)

    else:
        return binary(data,result,mid+1,end)


for i in target:
    answer = binary(data,i,0,n-1)
    if answer:
        print('yes')
    else:
        print('no')

#
# data.sort()

# # 2
# for i in target:
#     if i in data:
#         print('yes')
#     else:
#         print('no')

