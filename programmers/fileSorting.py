def solution(files):
    # 파일을 head, number, tail 나누기
    sorted_file = {}
    for file in files:
        sorted_file[file] = sort(file)

    # 반복문 돌며 정렬
    for i in range(len(files)-1):
        for j in range(len(files)-1, i, -1):
            back = sorted_file[files[j]]
            front = sorted_file[files[j-1]]
            if front[0].lower() > back[0].lower():  # head 비교
                tmp = files[j]
                files[j] = files[j - 1]
                files[j - 1] = tmp
                continue
            if front[0].lower() == back[0].lower() and front[1] > back[1]:  # head 같을 때, number 비교
                tmp = files[j]
                files[j] = files[j - 1]
                files[j - 1] = tmp

    return files


def sort(file):
    head = ''
    number = ''

    while file[0].isnumeric() is False:
        head += file[0]
        file = file[1:]

    while file[0].isnumeric():
        number += file[0]
        file = file[1:]
        if file == '':
            break

    tail = file

    return [head, int(number), tail]


print(solution(["F-15"]))
