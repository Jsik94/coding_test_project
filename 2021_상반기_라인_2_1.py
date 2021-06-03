def solution(program, flag_rules, commands):
    answer = []
   
    dic = {}

    """
    flag rule 정리
    
    """
    for i in flag_rules:
        tmp = i.split(" ")
        if len(tmp) == 2:
            name, argue = i.split(" ")
            dic[name] = argue

    for i in commands:
  
        command = i.split(" ")

        # program check
        if not (command[0] == program):
            answer.append(False)
            continue
        command.pop(0)

        # flag 확인을 위한 초기값
        #입력형식에 맞지 않으면 err_check = True 반환
        err_check = False
        #해당 flag의 규칙을 반환
        flag_rule = ""
        #flag 인지 flag arguments인지 분기를 나누기위한 flag
        isFlagArg = False

        # flag-rule check
        for j in range(len(command)):
            if err_check:
                break

            # FlagMode
            if command[j][0] == '-':
                isFlagArg = True
                if command[j] in dic:
                    flag_rule = dic[command[j]]
                    if flag_rule == "NULL":
                        isFlagArg = False
                    continue

                # there is no command
                else:
                    err_check = True
                    break;


            # ArgueMode
            if isFlagArg:

                if flag_rule == "STRING":
                    if command[j].isalpha():
                        isFlagArg = False
                        continue
                    err_check = True


                if flag_rule == "NUMBER":
                    if command[j].isdigit():
                        isFlageArgue = False
                        continue
                    err_check = True

            else:
                err_check = True
                break

        if err_check:
            answer.append(False)
        else:
            answer.append(True)

    return answer
