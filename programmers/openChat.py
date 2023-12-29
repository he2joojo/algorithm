def solution(record):
    # change가 있는 경우 {uid: 닉네임} 구하기
    nicknames = {}

    for log in record:
        log = log.split(" ")
        if log[0] != 'Leave':
            nicknames[log[1]] = log[2]

    # 결과 담기
    answer = []
    logs = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    for log in record:
        log = log.split(" ")
        if log[0] == 'Change':
            continue
        uid = log[1]
        nickname = nicknames[uid]
        answer.append(nickname + logs[log[0]])

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))