"""

7-4 떡볶이 떡 만들기

1. 떡 갯수 n  개와 목표 길이 m 이 주어진다
2. 다음줄에 n갯수만큼의 떡 길이가 주어진다
3. M만큼 가져가기위해 n가지의 떡을 자르는 절단기 길이의 최댓값을 구하라

sol.

1. 제일 큰떡놈을 고른다

2.  큰놈 기준으로 이진탐색을 하여  m 이 나올때가지 반복

3. 결과 도출


"""




n,m = list(map(int,input().split()))

data = list(map(int,input().split()))

start = 0 ;
large = max(data)
answer = 0 ;

while start <= large:

    target = 0 ;
    mid = (start+large)//2
    for i in data:
        if i > mid:
            target += i- mid


    if target > m :
        start = mid + 1
    elif target < m :
        large = mid - 1
    elif target == m :
        answer = mid ;
        break

print(answer);