from collections import defaultdict


def solution(s):
    s = s.replace("{", "").replace("}", "")
    nums = list(map(int, s.split(",")))

    dic = defaultdict(int)
    for n in nums:
        dic[n] += 1

    return sorted(dic, key=lambda x: -dic[x])

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))