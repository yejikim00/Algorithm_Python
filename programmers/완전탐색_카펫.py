import math


def make_list(num, new_list):
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            new_list.append([num // i, i])
    return new_list


def solution1(brown, yellow):
    area = brown + yellow
    yellow_list = []
    cm_list = []
    result = 0

    cm_list = reversed(make_list(area, cm_list))
    yellow_list = reversed(make_list(yellow, yellow_list))

    for x, y in zip(cm_list, yellow_list):
        print('x:', x, 'y:', y)
        for i, j in zip(x, y):
            print('i:', i, 'j:', j)
            if i - j == 2:
                result = x

    return result

def solution2(brown, yellow):
    for i in range(1, int(math.sqrt(yellow)+1)):
        if yellow % i == 0:
            x = yellow // i
            y = i
            if (x*2 + y*2) + 4 == brown:
                answer = [x+2, y+2]
                break

    return answer

# print(solution1(24, 24))
print(solution2(18, 6))
