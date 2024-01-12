def solution(s):
    answer = len(s)

    for n in range(1, len(s)//2+1):
        new_zip = ''
        tmp = s[:n]
        num = 1
        i = n
        while i < len(s):
            if (i+n) >= len(s):
                if tmp == s[i:]:
                    num += 1
                else:
                    tmp += s[i:]
                break
            if tmp == s[i:i + n]:
                num += 1
            else:
                new_zip += str(num) + tmp if num > 1 else tmp
                tmp = s[i:i + n]
                num = 1
            i += n
        new_zip += str(num) + tmp if num > 1 else tmp
        answer = min(answer, len(new_zip))

    return answer


print(solution("aabbaccc"))
