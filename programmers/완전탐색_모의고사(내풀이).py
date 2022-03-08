def solution(answers):
    answer = []
    count = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1 = 0
    count2 = 0
    count3 = 0

    j = 0
    for i in range(len(answers)):

        if i > len(num1) - 1:
            if answers[i] == num1[j]:
                count1 += 1
                j += 1
        else:
            if answers[i] == num1[i]:
                count1 += 1

    k = 0
    for i in range(len(answers)):
        if i > len(num2) - 1:
            if answers[i] == num2[k]:
                count2 += 1
                k += 1
        else:
            if answers[i] == num2[i]:
                count2 += 1
    l = 0
    for i in range(len(answers)):
        if i > len(num3) - 1:
            if answers[i] == num3[l]:
                count3 += 1
                l += 1
        else:
            if answers[i] == num3[i]:
                count3 += 1

    count.extend([count1, count2, count3])
    for i in range(len(count)):
        if count.count(max(count)) >= 2:
            answer.append(i + 1)
        else:
            answer = []
            answer.append(count.index(max(count)) + 1)
    return answer