"""

6-2 위에서 아래로


1. N개수 입력
2. 수입력
3. 정렬
내림차순으로 정렬

sol. sorted reverse=True 끝
"""

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data=sorted(data,reverse=True)

for i in data:
    print(i)
