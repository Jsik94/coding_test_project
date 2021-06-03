
"""


2 가지

1)  홀수 일때

10 20 40

-> 10+20 ==> 30

-> 30 + 40 ==> 70

total 100

2)

10 20 40 50

10 + 20 => 30

i)
40 50 30
-> 30 90
-> 120

total 240

ii)
card
10 20 40 50

extra
30 90
-->
del 10 20
40 50 30
-> sort
30 40 50
50 70


30 40 50
-> 70 50
-> 120

120 70 30
total 220

"""


import heapq

N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

sum = 0

heapq.heapify(data)
while len(data) != 1:
    first = heapq.heappop(data)
    second = heapq.heappop(data)
    heapq.heappush(data,first+second)
    sum += first+second

print(sum)

