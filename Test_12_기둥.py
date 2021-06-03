"""

조건
-바닥에 존재
-바로 밑에 기둥
-설치 왼쪽 지점에 보가 있음
-설치 지점에 보가 있음


보랑 기둥이랑 조건이 다름

기둥은 바닥이나 왼쪽에 보가 있어야하고
보는 양쪽 이다 보로 되어ㅣㅆ거나 기둥이 있어야됨


"""

def check(ans):
    for x , y , what in ans:
        # 기둥

        if what == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                return True
        # 보

        else:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans:
                return True
            if [x-1, y, 1] in ans and [x+1, y, 1] in ans:
                if [x-1, y-1, 0] in ans and [x+2, y-1, 0] in ans:
                    return True
    return False


def solution(n, build_frame):
    result = []

    for f in build_frame:
        x, y, equip, method = f
        #설치 삭제 분류
        if method == 1:
            result.append([x, y, equip])
            if check(result) == False:
                result.remove([x, y, equip])
        else:
            result.remove([x, y, equip])
            if check(result) == False:
                result.append([x, y, equip])

    result.sort()
    return result