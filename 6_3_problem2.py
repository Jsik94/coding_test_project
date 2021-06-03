"""

6-2 성적 출력


1. N개수 입력
2. 이름 성적 입력
3. 성적이 낮은 순서로 출력
내림차순으로 정렬

sol. sorted reverse=True 끝
"""

n = int(input())

data= []

for i in range(n):
    name , score = list(input().split())
    data.append((name,score))


"""
키를 기준으로 정렬할 때, lambda 함수를 사용하여 새롭게 정의한 키(custom key function, logic)를 사용할 수도 있습니다.

"""
data.sort(key = lambda  score: score[1])
#data =sorted(data, keys =lambda score: score[1])

for score in data :
    print(score[0])