from collections import defaultdict
from math import ceil


def solution(fees, records):
    # 차 번호: [입출차 시간] 구하기
    record_dict = defaultdict(list)

    for s in records:
        s = s.split(" ")
        car = int(s[1])
        tmp = s[0].split(':')
        hour = int(tmp[0]) * 60
        minute = int(tmp[1])
        time = hour + minute
        if len(record_dict[car]) % 2 == 0:
            time *= -1
        record_dict[car].append(time)

    # 차 번호: 총 주차시간 구하기
    last_time = (23 * 60) + 59

    for car in record_dict:
        record = record_dict[car]
        if len(record) % 2 != 0:
            record_dict[car].append(last_time)

    time_dict = {k: sum(record_dict[k]) for k in record_dict}

    # 차 번호: 주차 요금 구하기
    fee_dict = {}

    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    for car, total in time_dict.items():
        if total <= basic_time:
            fee_dict[car] = basic_fee
            continue
        total -= basic_time
        over_time = ceil(total / unit_time)
        fee_dict[car] = basic_fee + (over_time * unit_fee)

    # 결과 반환하기
    answer = []
    order = sorted(fee_dict)
    for car in order:
        answer.append(fee_dict[car])

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
