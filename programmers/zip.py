def solution(msg):
    letter = {chr(65 + i): i + 1 for i in range(26)}
    answer = []

    while msg not in letter:
        w_c = msg[0]
        idx = 0
        while w_c in letter:
            idx += 1
            w_c += msg[idx]
        letter[w_c] = len(letter) + 1
        w = w_c[:-1]
        answer.append(letter[w])
        msg = msg[idx:]

    answer.append(letter[msg])

    return answer


print(solution('KAKAO'))