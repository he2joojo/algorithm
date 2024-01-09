from itertools import permutations


def solution(expression):
    # 수식과 숫자 분리하기
    nums = []
    exs = []
    tmp = ''

    for s in expression:
        if s.isnumeric():
            tmp += s
        else:
            exs.append(s)
            nums.append(int(tmp))
            tmp = ''
    nums.append(int(tmp))

    # 연산하기
    tmp = list(set(exs))
    comb = list(permutations(tmp, len(tmp)))
    answer = 0

    for s in comb:
        nums2 = nums[:]
        exs2 = exs[:]
        for ex in s:
            if ex == '*':
                nums2, exs2 = multiple(nums2, exs2)
            elif ex == '+':
                nums2, exs2 = add(nums2, exs2)
            else:
                nums2, exs2 = minus(nums2, exs2)
        if abs(nums2[0]) > answer:
            answer = abs(nums2[0])

    return answer


def multiple(nums, exs):
    remove = []
    for i in range(len(exs)):
        if exs[i] != '*':
            continue
        nums[i + 1] = nums[i] * nums[i + 1]
        remove.append(i)

    for i in remove[-1::-1]:
        del nums[i]
        del exs[i]

    return nums, exs


def add(nums, exs):
    remove = []
    for i in range(len(exs)):
        if exs[i] != '+':
            continue
        nums[i + 1] = nums[i] + nums[i + 1]
        remove.append(i)

    for i in remove[-1::-1]:
        del nums[i]
        del exs[i]

    return nums, exs


def minus(nums, exs):
    remove = []
    for i in range(len(exs)):
        if exs[i] != '-':
            continue
        nums[i + 1] = nums[i] - nums[i + 1]
        remove.append(i)

    for i in remove[-1::-1]:
        del nums[i]
        del exs[i]

    return nums, exs
