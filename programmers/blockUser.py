from itertools import permutations


def solution(user_id, banned_id):
    # 순열 리스트 구하기
    cases = list(permutations(user_id, len(banned_id)))
    answer = []
    for case in cases:
        if check(case, banned_id):
            case = set(case)    # set()해주면 숫자는 자동으로 정렬해줌
            if case not in answer:
                answer.append(case)

    return len(answer)


def check(users, blocks):
    for i in range(len(blocks)):
        block = blocks[i]
        user = users[i]
        if len(block) != len(user):
            return False
        for j in range(len(block)):
            if block[j] == '*':
                continue
            if block[j] != user[j]:
                return False

    return True


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
