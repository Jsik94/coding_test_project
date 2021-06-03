"""

괄호변환


"""



# 두개만 들어가야함
def isbalanced(s):
    chk=0
    # 짝수개면 0 나옴
    for c in s:
        if c=='(':
            chk+=1
        elif c==')':
            chk-=1

    if chk==0:
        return True
    else:
        return False



# 올바른 괄호 문자열인지 체크하는 함수
def iscorrect(s):
    stack=[]
    stack.append(s[0])
    for i in range(1,len(s)):
        # 스택에 들어가는경우  아예없거나 , 끝났거나 (이전이 닫힌괄호), 진행중 (이전과 모양이 같음 )
        if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False


def solution(p):
    answer = ''
    u=""
    v=""

    #없으면 반환
    if len(p)==0 or iscorrect(p):
        return p

    # 2개씩 균형 체크
    for i in range(2,len(p)+1,2):
        # 문자열 2개씩 넣어서 확인
        if isbalanced(p[0:i]):
            # u에 문자열 반환
            u=p[0:i]
            v=p[i:len(p)]
            break
    # u가 올바른 괄호 문자열일 때
    if iscorrect(u):
        #v 로 나머지 재귀 수행
        answer+=u+solution(v)

    # u가 올바른 괄호 문자열이 아닐 때
    else:
        # 문자열에 붙이고 수행
        answer+='('+solution(v)+')'

        #reverse
        for c in u[1:-1]:
            if c=='(':
                answer+=')'
            else:
                answer+='('

    return answer