import math


def solution(n, k):
    # n을 k진수로 바꾸기
    tmp = ''
    while n:
        n, rest = divmod(n, k)
        tmp += str(rest)

    tmp = tmp[::-1]

    # 변환된 수 구하기
    tmp = tmp.split('0')
    n = [int(i) for i in tmp if i.isnumeric()]

    # 소수 구하기
    answer = []
    for i in n:
        if i == 1:
            continue
        if is_prime_number(i):
            answer.append(i)

    return len(answer)


def is_prime_number(n):
    root = math.ceil(math.sqrt(n))
    root = min(root,n-1)
    for i in range(2, root + 1):
        if n % i == 0:
            return False
    return True


print(solution(110011, 10))
