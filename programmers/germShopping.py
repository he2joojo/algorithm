from collections import defaultdict


def solution(gems):
    size = len(set(gems))
    cart = defaultdict(int)
    cart[gems[0]] += 1
    left = 0
    right = 0
    answer = [0, len(gems)-1]

    while left < len(gems) and right < len(gems):
        # 모든 종류 보석이 담겼을 때
        if len(cart) == size:
            # 더 효율적인지 확인
            if (right - left) < (answer[1] - answer[0]):
                answer = [left, right]
            # left 이동해서 중복 줄이기
            if cart[gems[left]] == 1:
                del cart[gems[left]]
            else:
                cart[gems[left]] -= 1
            left += 1
        # right 이동해서 보석 채우기
        else:
            right += 1
            if right == len(gems):
                break
            cart[gems[right]] += 1

    return [answer[0] + 1, answer[1] + 1]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
