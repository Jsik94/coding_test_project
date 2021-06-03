"""

럭키스트레이트


"""

target = input()

first = 0
second = 0
for i in range(0, len(target)):
    if i < len(target)/2 :
        first += int(target[i])
    else:
        second += int(target[i])

if first == second:
    print("LUCKY")
else :
    print("READY")