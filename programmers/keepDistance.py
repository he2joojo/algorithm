def solution(places):
    answer = [1, 1, 1, 1, 1]

    # 가로줄 POP 검사
    for i, place in enumerate(places):
        for line in place:
            if 'POP' in line:
                answer[i] = 0
                break

    # 세로줄 POP 검사
    for i, place in enumerate(places):
        if answer[i] == 0:
            continue
        for x in range(5):
            tmp = ''
            for y in range(5):
                tmp += place[y][x]
            if 'POP' in tmp:
                answer[i] = 0
                break

    # 시계방향으로 검사
    for i, place in enumerate(places):
        if answer[i] == 0:
            continue
        for x in range(1, 5):
            for y in range(1, 5):
                tmp = place[x][y] + place[x][y-1] + place[x-1][y-1] + place[x-1][y]
                if tmp.count('P') <= 1:
                    continue
                elif tmp.count('P') > 2:
                    answer[i] = 0
                    break
                elif tmp != 'PXPX' and tmp != 'XPXP':
                    answer[i] = 0
                    break
            if answer[i] == 0:
                break

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
