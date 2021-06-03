#init
N = int(input())
data=list(map(int,input().split()))
data.sort()
if int(len(data)%2) == 0 :
    print(data[int(len(data)/2)-1])
else:
    print(data[int((len(data)-1)/2)])



# # 안테나 위치가 i일때 거리총합
# answer = []
# for i in data:
#     sum = 0
#     for j in data:
#         sum += abs(i -j)
#
#     answer.append((i,sum))
#
# answer.sort(key= lambda x:x[1])
# print(answer)