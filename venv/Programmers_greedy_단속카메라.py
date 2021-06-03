
import copy

def checkin (route,location):

    if route[0] <= location <= route[1]:
        return True
    else:
        return False

def possible_list(standard,compare):

    p_list = []
    result_list=[]
    for i in range(standard[0],standard[1]+1):
        p_list.append(i)
    print(p_list)

    for i in p_list:
        if checkin(compare,i) is True:
            print("possible")
            result_list.append(i)

    return result_list

def largest_idx (routes):
    max = 0
    idx = 0
    for i in range(len(routes)):
        length = routes[i][1] - routes[i][0]
        if max <= length :
            idx = i
            max = length

    return idx

routes =[ [-14,-5], [-18,-13], [-5,-3],[-20,15]]


passed = [False] * len(routes)

camera = 0

print(largest_idx(routes))

print(possible_list(routes[3],[3]))


while True:

    #4곳다 카메라가 잡을 수 있으면 아웃
    if passed.count(True) is len(routes):
        break

    idx = largest_idx(routes)
    standard = routes.pop(idx)

    camera += 1
    passed[idx] =True

    setup = possible_list(standard,standard)

    copied = copy.deepcopy(routes)

    while copied is not False:
        #더이상 겹치는 것이 없다면
        if setup is False:
            break;
        result=  possible_list(standard,copied[0])
        if result is not False:
            standard
            copied.pop(0)


""""
가장 긴놈을 찾는다

가장 긴놈을 리스트에서 꺼냄

그다음 나머지중 들어갈 수 있는 놈이 있는지 확인 

"""