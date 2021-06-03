"""
문자열 뒤집기


문자열을 뒤집어서 0이나 1로 만들 수있는 최소 횟수 구하기

12분

"""

case = input()

zero_cnt =0
one_cnt = 0
standart = case[0]
for i in range(1,len(case)):
    #같은 숫자면 continue
    if case[i-1] == case[i]:
        continue
    else :
        if case[i] == '1':
            zero_cnt +=1
        else :
            one_cnt +=1


print(max(one_cnt,zero_cnt))