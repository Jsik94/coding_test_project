def solution(brown, yellow):
    total = brown + yellow
    col, row = 0, 0
    start = 3

    while True:
        print("<----- status ---->")
        print("row : ",row," co; : " ,col)
        # 나머지가 없다면
        if total % start == 0:
            col = start
            row = total / start

            if (row - 2) * (col - 2) == yellow:
                break
            else:
                start = start + 1
        else:
            start = start+1
            continue

    answer = [row, col]

    return answer



brown = 24
yellow = 24

result = solution(brown,yellow)

print(result)