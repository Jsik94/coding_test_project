"""

LCS

dp[i] i까지의 최대 길이

ASKDK
AKKASAAKAAD

SDK


21332
23231

"""


#init
s1 = input()
s2 = input()


len1 = len(s1)
len2 = len(s2)

maps = [[0] * (len2 + 1) for _ in range(len1 + 1)]



for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # 문자가 같으면  +1 , 다를땐 기존 중 최대
        if s1[i - 1] == s2[j - 1]:
            maps[i][j] = maps[i - 1][j - 1] + 1
        else:
            maps[i][j] = max(maps[i - 1][j], maps[i][j - 1])

print(maps[len2][len1])

