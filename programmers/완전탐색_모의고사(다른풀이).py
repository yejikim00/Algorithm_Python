def one(arr1: list, count: int):
    return arr1[count % 5]


def two(arr2: list, count: int, j: int):
    if count % 2 == 0:
        return 2
    else:
        return arr2[j % 4]


def three(arr3: list, count: int, last: int):
    if count % 2 == 1:
        return last
    else:
        return arr3[count % 5]


def solution(answers):
    answer = []
    count = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 3, 4, 5]
    arr3 = [3, 1, 2, 4, 5]
    count1 = 0
    count2 = 0
    count3 = 0
    last = arr3[0]
    j = 0

    for i in range(len(answers)):
        if answers[i] == one(arr1, i):
            count1 += 1

        t = two(arr2, i, j)
        if answers[i] == t:
            count2 += 1
            if t != 2:
                j += 1

        last = three(arr3, i, last)
        if answers[i] == last:
            count3 += 1

    count += [count1, count2, count3]
    for i in range(len(count)):
        if count.count(max(count)) >= 2:
            answer.append(i + 1)
        else:
            answer = []
            answer.append(count.index(max(count)) + 1)
    return answer
print(solution([1,2,3,4,5]))