
"""
그리디 알고리즘
3-3 1이 될때 까지

n,k 가 주어졌을 때 n 이 1이 될때까지  두 과정중 하나를 수행 하려고한다.
단, 2번째 연산은 n %k == 0 일때만 가능하다.

1. n에서 1을 뺀다
2. n을 k 로 나눈다,

n이 1이 될때까지 수행하는 반복 횟수의 최솟값을 구하시오

sol
두 조건을 나눈후 두 조건을 거칠때 횟수를 누적하여 출력 

"""


#input line

n, k = map(int,input().split())

result = 0 ;


while True:
    if n ==1 :
        break
    elif n%k==0:
        result +=1
        n/=k
    else:
        result +=1
        n-=1

#output line

print(result)
