"""문제 설명
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

34분

while 트럭이 다 지나갈때 까지

    1.차를 하나 큐에서 뺀다
    2.차를 브릿지에 올려 놓는다.
    3.다음 차를 뒤에 올려놓을 수 있는지 확인
        3-1. 다음차를 올려놓을 수 없다면, ( 다음 차를 올려놓을 수 없는 조건 : 브릿지 무게 보다 다음차까지의 무게합이 무겁다, 브릿지 길이 만큼 차가 있다.)
                3-1-1. 다음차를 올려 놧을 때 무게가 max 다
                    ->  맨앞차가 나갈때 까지 움직인다
                3-1-2. 브릿지의 차가 꽉 찼다.
                    -> 맨앞차가 나갈때까지 움직인다
        3-3, 다음차를 올려놓을 수 있다면,
        넘어감

---> 마지막 트럭이 지날때 while 문제됨






"""


def solution(bridge_length, weight, truck_weights):
    bridge = [0] *bridge_length
    timer = 0

    # 다리가 없어 질때까지 1초 단위 진행
    while bridge :
        timer= timer+1
        bridge.pop(0)
        if truck_weights == [] :
            continue
        #다리 무게를 넘지 않는 선에서 트럭 올림
        if truck_weights[0]+sum(bridge) <= weight :
            bridge.append(truck_weights[0])
            truck_weights.pop((0))
        else :
            bridge.append(0)

    answer = timer
    return answer



bridge = 100
weight =100
truck = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge,weight,truck))


""""
삽질의 흔적
  #toggle =True
    # 
    # while cars:
    #     if toggle:
    #         current_car = cars.popleft()
    #     #현재 다리위에 있는 총 무게
    # 
    #     total_weight =total_weight+current_car
    #     location = 0
    #     time = timer
    # 
    # 
    #     # 현재 차의 무게 , 현재 위치
    #     info = [ current_car ,location]
    # 
    #     #다리에 트럭을 올릴 수 있다면
    #     if total_weight <= bridge_length:
    #         que.append(info)
    # 
    #     #1초씩 트럭 이동
    #     timer += 1
    #     for i in len(que):
    #         que[i][1] += 1
    #         # 브릿지를 초과하지 않을때만 que에 다시 넣음
    #         if que[i][1] <= bridge_length:
    #             que.append(que[i])
    #             que.popleft()
    #         else:
    #             que.popleft()
    # 
    # 
    # 
    #     # que.append(car)
    #     # while que :
    #     #     #1초 이동
    #     #     current_car_weight ,current_car_location , current_car_timer = que.popleft()
    #     #     timer += 1
    #     #     current_car_location+=1
    #     #     current_car_timer = timer
    #     #     if current_car_location > 2 :
    #     #         total =
    # 

"""