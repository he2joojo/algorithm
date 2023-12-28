def solution(n, t, m, p):
    # len(total_number) >= t*m 까지 숫자 구해서 더하기
    total_numbers = '0'
    tmp = 1

    while len(total_numbers) <= t * m:
        total_numbers += change_10_to_n(tmp, n)
        tmp += 1

    # 순서에 해당하는 문자만 answer에 담기
    answer = ''
    for i in range(t):
        idx = (p - 1) + (m * i)
        answer += total_numbers[idx]

    return answer


def change_10_to_n(number, k):
    nums_to_chr = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    answer = ''
    while number > 0:
        number, rest = divmod(number, k)
        answer += nums_to_chr[rest]

    return answer[::-1]


print(solution(16,16,2,1))
