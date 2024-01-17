from collections import deque


def solution(n, t, m, timetable):
    # 시간을 숫자로 바꾸고 정렬
    time = []
    for s in timetable:
        tmp = s.split(':')
        time.append(int(tmp[0]) * 60 + int(tmp[1]))

    time.sort()
    time = deque(time)

    # 버스 시간 구하기
    bus = deque()
    start = 9 * 60
    for i in range(n):
        bus.append(start + (t * i))

    # 막차시간보다 늦으면 삭제
    while time[-1] > bus[-1]:
        time.pop()
        if len(time) == 0:
            break

    # 앞 차 승객 삭제
    while len(bus) > 1 and len(time) >= 1:
        bus_time = bus.popleft()
        for i in range(m):
            if time[0] > bus_time:
                break
            time.popleft()

    # 막차 탑승시간 구하기
    hour = 0
    min = 0
    if len(time) < m:
        hour = bus[-1] // 60
        min = bus[-1] % 60
    else:
        tmp = time[m - 1] - 1
        hour = tmp // 60
        min = tmp % 60

    # 정답 형식 맞추기
    hour = str(hour)
    min = str(min)

    if len(hour) < 2:
        hour = '0' + hour

    if len(min) < 2:
        min = '0' + min

    return hour + ':' + min


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
