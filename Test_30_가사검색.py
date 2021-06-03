





def solution(words, queries):
    answer = []

    """
    words 단어수만 가지고 있는 리스트 구현
    
    """
    cnt_words = [len(i) for i in words]

    N = len(queries)

    for i in range(N):
        #접두사 True , 접미사 False
        flag = True
        #list 지금 queries에서 검색할 단어를 저장
        list = queries[i]
        #output 결과적으로 일치하는 단어의 갯수
        output = 0;
        # ? 갯수
        cnt_question = list.count("?")
        # 쿼리 단어 길이
        target_size = len(list)
        # ? 제외한 쿼리 단어길이
        target_range = len(list)-cnt_question
        # ? 제외한 쿼리 단어
        target_queries = []

        # 전체 검색일 때
        if target_size == cnt_question :
            answer.append(len(words))
            continue

        # 접미사일때
        if list[-1] =="?" :
            flag = False

        if flag :
            target_queries = list[-target_range:]
        else:
            target_queries = list[0: target_range]


        for j in range(len(words)):

            #비교할 단어
            compare = words[j]
            #비교할 단어 길이
            compare_size = len(compare)


            #사이즈 불일치 시 다음 검색
            if compare_size is not target_size :
                continue

            # 접미/두 판단
            if flag :
                compare_part = compare[-target_range:]
                if compare_part == target_queries:
                    output += 1

            else :
                compare_part = compare[0: target_range]
                if compare_part == target_queries:
                    output += 1

        answer.append(output)


    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries =["fro??", "????o", "fr???", "fro???", "pro?"]


list = [len(i) for i in words]

answer = solution(words,queries)
print(answer)