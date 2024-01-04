def solution(m, musicinfos):
    time = {}
    sequence = {}
    index = {}
    # 시간, 제목, 악보 분리하기
    for i, info in enumerate(musicinfos):
        info = info.split(',')
        title = info[2]
        time[title] = calculate_time(info[1]) - calculate_time(info[0])
        sequence[title] = info[3]
        index[title] = i

    # 악보 바꾸기
    replaced = {'A#': '0', 'C#': '1', 'D#': '2', 'F#': '3', 'G#': '4'}
    for title, song in sequence.items():
        for s in replaced:
            song = song.replace(s, replaced[s])
        t = time[title]
        played = (song * (t // len(song))) + song[:t % len(song)]
        sequence[title] = played

    # 일치하는지 확인
    answer = []
    for s in replaced:
        m = m.replace(s, replaced[s])

    for title, song in sequence.items():
        idx = song.find(m)
        if idx == -1:
            continue
        answer.append([time[title], index[title], title])

    # 정답 반환하기
    if len(answer) == 0:
        return '(None)'

    if len(answer) == 1:
        return answer[0][2]

    answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    return answer[0][2]


def calculate_time(time):
    h = int(time.split(':')[0])
    m = int(time.split(':')[1])

    return (h * 60) + m


print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
