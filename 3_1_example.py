
"""
그리디 알고리즘
3-1  동전 갯수 구하기
500 , 100 ,50 ,10 인 동전이 있을 때
가장 적게 동전으로 값을 한산 하시오.
단, 모든 수는 10의 배수 임.

"""




# initialize
list =[500, 100, 50 ,10]
cnt = 0

#data input line
n = int(input());


for coin in list:
    cnt += n //coin
    n %= coin

print(cnt)