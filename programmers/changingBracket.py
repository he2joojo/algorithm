def solution(p):
    if p == '':
        return ''

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        for s in u:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        return answer


def check(p):
    for i in range(len(p)//2):
        p = p.replace('()', '')

    if p == '':
        return True

    return False


def divide(p):
    if len(p) == 0:
        return []

    bracket = {'(': 0, ')': 0}
    idx = 0

    for i in range(len(p)):
        bracket[p[i]] += 1
        if bracket['('] == bracket[')']:
            idx = i + 1
            break

    return [p[:idx], p[idx:]]


print(solution("()))((()"))
