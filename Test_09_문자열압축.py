"""





"""
import math

def solution(s):
    #절반 이하의 길이까지만 검색할 것임


    max_len= math.floor(len(s)/2)+1
    word_cnt=1

    answer = 999999999999999999999999999

    if len(s) == 1:
        answer = 1
        return answer


    for compare_idx in range(1,max_len):
        total = ""
        compare_word = s[:compare_idx]

        for i in range(compare_idx,len(s),compare_idx):
                #맞으면 숫자추가
            if s[i:i+compare_idx] == compare_word:
                word_cnt+=1
            else :
                #아니면 지금 문자를 비교문자로 변경
                if word_cnt ==1:
                    word_cnt =""
                total += str(word_cnt)+compare_word
                compare_word = s[i:i+compare_idx]
                word_cnt=1

        if word_cnt == 1:
            word_cnt = ""
        total += str(word_cnt) + compare_word
        word_cnt = 1
        answer = min(answer,len(total))

    return answer


target = input()

answer = solution(target)

print(answer)