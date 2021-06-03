
def bineary(dic, tar, start, end):
    if start > end:
        return 0
    dic = list(dic)
    mid = (start + end) // 2
    if dic[mid][0] == tar:
        return dic[mid][1]
    elif dic[mid][0] > tar:
        return bineary(dic, tar, start, mid - 1)
    elif dic[mid][0] < tar:
        return bineary(dic, tar, mid + 1, end)


n = int(input())
a = []
b = []
c = []
d = []

resultset=[]
for i in range(n):
    data = list(map(int,input().split()))
    a.append(data[0])
    b.append(data[1])
    c.append(data[2])
    d.append(data[3])

result = 0

"""
a 와 b 로 나오는 semi result 값의 조합을 다 구함 


"""
answer = dict()

for i in range(n):
    for j in range(n):
        if a[i]+b[j] in answer:
            #기존에 있음
            answer[(a[i]+b[j])] +=1

        else:
            #새로 추가
            answer[(a[i]+b[j])] = 1

answer = sorted(answer.items())


for i in range(n):
    for j in range(n):
        flag = False
        target = (c[i] + d[j]) * (-1)
        tmp = bineary(answer,target,0,len(answer)-1)
        if tmp != 0:
            result += tmp
            flag = True
        if flag:
            continue

    if flag:
        continue

# while i < len(c):
#     while j < len(d):
#         target = (c[i]+d[j]) *(-1)
#         if target in answer:
#             result +=answer[target]
#
#         j+=1
#     i+=1

"""
comment 
다음주  또또 리트 

"""

print(result)