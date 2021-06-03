"""

8-3 개미 전사

1. n개의 배열이있을때 각 n개에 배열된 값 들 중 누적할 수 있는 최대합을 구한다.
2. 단 접근했다면 해당 배열의 인접배열은 접근 할 수 없다.

sol.

1. DP 테이블 생성 ,

2. 점화식 생성

n =1 --> n[1] 값

n = 2 -->
        max ( n[1], n[2])

n =3  -->
        max(n[2],n[1]+n[3])

n = k -->
        max(n[k-1] , n[k-2]+data[k])


12분
"""

n = int(input())

data = list(map(int,input().split()))

dp = [0] * 100

dp[0] = data[0]
dp[1] = max(data[0],data[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+data[i])

print(dp[n-1])