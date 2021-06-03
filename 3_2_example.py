

"""
그리디 알고리즘
3-2  큰 수의 법칙
n , m , k 가 있을 때

n번 만큼 다음줄에 입력값을 받고
m개의 배열에 k번 큰수를 넣고 그다음 숫자를 넣고 다시 큰수를 넣는 식

"""

# 공백에 따른 입력 방식 알아 둘것
#input line
n , m , k  = map(int,input().split())
result = 0 ;
data = list(map(int,input().split()))

data.sort()


while True:
    for i in range(k):
        if m == 0:
            break

        # 가장 큰 수
        result +=  data[n-1]
        m -= 1

    if m == 0:
        break

    result += data[n-2]
    m-=1

#output line

print(result)