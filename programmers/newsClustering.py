from collections import defaultdict


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    # 2개씩 짝짓기
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    for i in range(len(str1) - 1):
        tmp1 = str1[i]
        tmp2 = str1[i + 1]
        if tmp1.isalpha() and tmp2.isalpha():
            dict1[tmp1 + tmp2] += 1

    for i in range(len(str2) - 1):
        tmp1 = str2[i]
        tmp2 = str2[i + 1]
        if tmp1.isalpha() and tmp2.isalpha():
            dict2[tmp1 + tmp2] += 1

    inter = 0
    union = 0

    # 교집합 구하기
    for s in dict1:
        if s in dict2:
            inter += min(dict1[s], dict2[s])

    # 합집합 구하기
    for s in dict1:
        if s in dict2:
            union += max(dict1[s], dict2[s])
        else:
            union += dict1[s]

    for s in dict2:
        if s not in dict1:
            union += dict2[s]

    # 결과 반환하기
    answer = int((inter / union) * 65536) if inter > 0 else 65536
    return answer


print(solution("aa1+aa2", "AAAA12"))
