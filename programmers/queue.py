from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    maximum = max(queue1 + queue2)

    # 총 합이 홀수면 -1
    if (sum1 + sum2) % 2 != 0:
        return -1

    # 가장 큰 수가 나머지 합보다 크면 -1
    if maximum > (sum1 + sum2 - maximum):
        return -1

    # 반복해서 숫자 교환하기
    que1 = deque(queue1)
    que2 = deque(queue2)
    count = 0

    for i in range(len(queue1)*2+3): # 왜 반복횟수에 +3을 해줘야만 정답이 나오는지 모르겠음
        if sum1 == sum2:
            return count
        elif sum1 > sum2:
            tmp = que1.popleft()
            que2.append(tmp)
            sum1 += -tmp
            sum2 += tmp
            count += 1
        else:
            tmp = que2.popleft()
            que1.append(tmp)
            sum1 += tmp
            sum2 += -tmp
            count += 1

    return -1


print(solution([2,4],[4,2]))
