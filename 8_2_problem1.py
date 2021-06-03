"""

8-2 1fh 만들기

1. X가 5,3,2 로 나누어 떨어지면 나눈다
2. X에서 1을 뺀다
3. 1이 나올때까지의 최소 연산 수
sol.

1. DP 테이블 생성 ,

2. 연산을 dp에  저장하면서 풀이


20분 이상
--> 재귀쓰는 버릇 못버림
"""





n = int(input())

dp = [0]*30000

dp[5] = 1
dp[3] = 1
dp[2] = 1

for i in range(2,n+1):


    # 먼저 뺀것과 나눈것 어느것이 효율적인지 비교해서 넣어야함
    dp[i] = dp[i-1]+1

    if i % 5 == 0:
        dp[i] = min(dp[i],dp[i // 5]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i],dp[i // 3]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i],dp[i // 2]+1)




print(dp[n])
