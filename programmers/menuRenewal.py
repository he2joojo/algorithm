from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        menus = defaultdict(int)
        for order in orders:
            comb = list(combinations(order, i))
            for c in comb:
                c = list(c)
                c.sort()
                c = ''.join(c)
                menus[c] += 1
        tmp = sorted(menus, key=lambda x: -menus[x])
        # 후보가 없을 때
        if len(menus) == 0:
            continue
        # 2명 이상 주문하지 않았을때
        if menus[tmp[0]] < 2:
            continue
        # 가장 많이 주문한 조합이 여러개 일 때
        n = menus[tmp[0]]
        for j in range(len(tmp)):
            if menus[tmp[j]] == n:
                answer.append(tmp[j])

    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
