def solution(program, flag_rules, commands):
    answer = []
    """
    flag 와 alias를 담기위한 dictionary
    """
    dic = {}
    alias_dict = {}

    """
    flag rule 정리
    
    """
    for i in flag_rules:
        tmp = i.split(" ")
        if len(tmp) == 2:
            name, argue = i.split(" ")
            dic[name] = argue
        #alias 인 경우만 따로 저장
        if len(tmp) == 3 and tmp[1] == "ALIAS":
            alias_dict[tmp[0]] = tmp[2]

    for i in commands:
        #각 명령마다 플래그 중복사용을 방지 하기 위한 리스트
        flag_list = []
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
                    # when it uses same flag
                    if command[j] in flag_list:
                        err_check = True
                        break
                    # save in list
                    flag_list.append(command[j])
                    flag_rule = dic[command[j]]
                    if flag_rule == "NULL":
                        isFlagArg = False
                    continue


                # if it uses ALIAS,
                elif command[j] in alias_dict:
                    # when it uses same flag
                    if alias_dict[command[j]] in flag_list:
                        err_check = True
                        break
                    flag_list.append(alias_dict[command[j]])
                    flag_rule = dic[alias_dict[command[j]]]
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

                if flag_rule == "STRINGS":
                    if command[j].isalpha():
                        continue
                    err_check = True

                if flag_rule == "NUMBER":
                    if command[j].isdigit():
                        isFlageArgue = False
                        continue
                    err_check = True

                if flag_rule == "NUMBERS":
                    if command[j].isdigit():
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

program="line"
flag_rules=["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
commands=["line -n 100 -s hi -e", "line -n 100 -e -num 150"]

print(solution(program,flag_rules,commands))