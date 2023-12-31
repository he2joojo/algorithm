def solution(m, n, board):
    # 보드 행과 열 바꾸기
    board2 = [[] for i in range(n)]

    for i in range(m):
        for j in range(n):
            s = board[(m-1)-i][j]
            board2[j].append(s)

    # 1) 자신 아래 행에 똑같은 반복 문자 있는지 확인, 인덱스 저장
    # 2) 한 바퀴 반복 후 저장된 인덱스 제거
    # 3) 다시 1번부터 반복
    # 4) 한 바퀴 반복 후 저장된 인덱스 없으면 개수 return
    remove = set()
    answer = 0

    while True:
        for i in range(n-1):
            for j in range(len(board2[i])-1):
                chr1 = board2[i][j]
                chr2 = board2[i][j + 1]
                if chr1 != chr2:
                    continue
                if len(board2[i+1]) < j+2:
                    continue
                if board2[i+1][j] == board2[i+1][j+1] == chr1 == chr2:
                    remove.add((i, j))
                    remove.add((i, j+1))
                    remove.add((i+1, j))
                    remove.add((i+1, j+1))
        if len(remove) == 0:
            break
        remove = list(remove)
        remove.sort()
        for p in remove[::-1]:
            del board2[p[0]][p[1]]
            answer += 1
        remove = set()

    return answer


print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
