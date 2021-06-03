"""

6-4 배열 원소 교체


1. n개의 배열 2개가 존재 k 번 바꿔치기 가능
2. 바꿔칠때는 배열의 순서 상관없음


sol.
A열 내림차순 정렬
B열 오름 차순정렬

k만큼 검사하여 b가 크면 이식

최댓값 구함

sol. sorted reverse=True 끝
"""


n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort()

#뒤에서 k 번 만큼 확인
for i in range(n-k,n):
    if a[i] <b[i]:
        a[i] = b[i]

print((sum(a)))