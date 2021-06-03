"""
8-5

n개의 화폐갯수 , k 값을  주어졌을땨
화폐조합으로   k 를 만드는 최대 값


sol.
큰놈부터 다쓰고
안돼면 작은놈쓰고
그래도 0안나오면 -1

k = 1 일 때
n코인으로 계산값을 f 라 할 때
dp[1] = min(f(1),f(2),f(n-1),f(n))

dp[2] = coin 조합

k 가 되었을때  k +코인은 가능 ,

"""




n , k = list(map(int,input().split()))

coin = []

for i in range(n):
    coin.append(int(input()))

dp = [99999]*(k+1)

dp[0] = 0

# 코인만큼 다 한번씩 확인하되, 최소만 가져갈 것

for i in range(n):
    for j in range(coin[i],k+1):
        if dp[j-coin[i]] != 99999:
            dp[j] = min (dp[j],dp[j-coin[i]]+1)

if dp[k] == 99999:
    print(-1)
else:
    print(dp[k])

