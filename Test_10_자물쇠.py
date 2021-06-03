"""

key N *N

Lock M * M


M <= N

K는 회전 가능  돌려서 빈곳이 없어야함

자물쇠 영역 외는 신경쓰지 않음


"""
import copy


# 자물쇠범위에 1이 하나로도 비면 false
def check(len_key, len_lock, check_table):
    start_index = len_key - 1
    end_index = start_index + len_lock
    toggle = True

    for i in range(start_index, end_index):
        for j in range(start_index, end_index):
            if check_table[i][j] != 1:
                toggle = False
                break
        if not toggle:
            break

    if toggle:
        return True
    else:
        return False


# 해당 위치를 기준으로 lock 사이즈만큼 확장테이블에 넣음
def add(lock, check_table, loc_x, loc_y):
    len_lock = int(len(lock))
    for i in range(len_lock):
        for j in range(len_lock):
            check_table[loc_x + i][loc_y + j] = lock[i][j]

    return check_table


# 회전
def rotate(m):
    N = len(m)

    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N - 1 - r] = m[r][c]

    return ret


def solution(key, lock):
    len_key = int(len(key))
    len_lock = int(len(lock))

    # 테이블 확장
    extended_size = int((len_key - 1) * 2) + int(len_lock)
    extended_lock = [[0] * (extended_size) for _ in range(extended_size)]

    for i in range(len_lock):
        for j in range(len_lock):
            extended_lock[i + len_key - 1][j + len_key - 1] = lock[i][j]

    # 비교용 사본 ??깊은 복사 질의
    copy_lock = copy.deepcopy(extended_lock)

    result = False
    for k in range(4):
        key = rotate(key)
        for i in range(0, extended_size - len_key):
            for j in range(0, extended_size - len_key):
                loc_x, loc_y = i, j
                copy_lock = add(key, copy_lock, loc_x, loc_y)

                if check(len_key, len_lock, copy_lock):
                    result = True
                if result:
                    break
            if result:
                break

    answer = result
    return answer


# 예제셋업
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# len_key = len(key)
# len_lock = len(lock)
#
# extended_size = int((len_key-1)*2) +int(len_lock)
#
# extended_lock = [[0]*(extended_size) for _ in range(extended_size)]
#
# for i in range(len_lock):
#     for j in range(len_lock):
#         extended_lock[i+len_key-1][j+len_key-1] = lock[i][j]
#
#
# for i in extended_lock:
#     print(i)
#
# print(check(len_key,len_lock,extended_lock))

if solution(key, lock):
    print("열림")

else:
    print("안열림")
