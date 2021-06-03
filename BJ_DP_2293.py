"""
https://www.acmicpc.net/problem/2293

전 1 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	4 MB	30372	13067	9707	43.410%
문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.


1 2 5 -> 10

0 1 2 3 ~~~~ 10


 하나로만 될수 있는 방법
 한개 이상을 조합하는 방법

 k = n + m
 10 =  7 + 3

 DP[0] = 1

"""


n, target = map(int,input().split())

coin =[0]*(n)
for i in range(n):
    coin[i] = int(input())


DP = [0] * (target+1)

coin.sort(reverse=True)


DP[0] = 1
#코인만큼 확인
for i in range(len(coin)):
    #해당 코인 값+ target-해당코인 제거하고 값
    for j in range(coin[i],target+1):
        if (j-coin[i] < 0):
            continue
        DP[j] += DP[j-coin[i]]


print(DP[target])