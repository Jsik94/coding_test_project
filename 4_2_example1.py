

"""
구현문제
4-2 시각

00 : 00 : 00 - N:59:59 까지 중 3이 하나라도 들어가는 경우의 수를 구하라

시 분 초 의 시각마다 3이될때 cnt +1

sol
시 분 초 마다 돌면서 3이 나오면 count 하도록 구현

"""


#input line
n = int(input())
count = 0 ;

##range 왜쓰는지는 찾아볼것
#시
for h in range(n+1):
    #분
    for min in range(60):
        #초
        for sec in range(60):
            ## 3이 들어가서 false 가 나오지않으면 무조건 카운트
            if str(h).find('3') !=-1 or str(min).find('3')!=-1 or str(sec).find('3')!=-1:
                count +=1



#output line

print(count)