
"""



[   1 , 2,  3,  4,  5]
    0    0   0  0  0
    0       0   0  0





"""



def solution(food_times, k):
    times = k
    index = 0

    toggle = True

    while times!=0:

        if index == len(food_times):
            index = 0

        if food_times[index] < 1:
            index+=1
        else :
            food_times[index] -= 1
            index+=1
            times-=1

        if sum(food_times) ==0:
            toggle = False
            break
    if index == len(food_times):
        index = 0

    if toggle:
        if index +1 ==len(food_times):
            answer =1
        else:
            answer = index +1
    else :
        answer = -1
    return answer


food_times = list(map(int,input().split()))
target = int(input())


answer = solution(food_times,target)

print(answer)