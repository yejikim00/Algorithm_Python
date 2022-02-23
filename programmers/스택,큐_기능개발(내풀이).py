def solution(progresses, speeds):
    answer = []
    day = []
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        if remain % s == 0:
            day.append(remain // s)
        else:
            day.append(remain // s + 1)

    count = 1
    for i in range(len(day)):
        if i + 1 == len(day):
            answer.append(count)
            break
        if day[i] >= day[i + 1]:
            count += 1
        else:
            answer.append(count)
            count = 1

    return answer