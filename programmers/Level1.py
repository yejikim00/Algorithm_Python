# Leve1 - 신고 결과 받기: 내 풀이
def solution(id_list, report, k):
    answer = []
    users = []
    stop = []
    for r in report:
        users.append(r.split(' ')[0])
        stop.append(r.split(' ')[1])

    stop = set(stop)
    stop = list(stop)

    dic = {}

    for i in range(len(id_list)):
        if stop.count(id_list[i]) >= k:
            dic[id_list[i]] = stop.count(id_list[i])
        else:
            dic[id_list[i]] = 0

    return dic


# Level1 - 신고 결과 받기: 찾은 풀이
def solution1(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list} # 신고 당한 사람의 신고 당한 횟수

    for r in set(report):
        reports[r.split(' ')[1]] += 1

    for r in set(report):
        if reports[r.split(' ')[1]] >= k:
            answer[id_list.index(r.split(' ')[0])] += 1

    return answer


# print(solution1(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution1(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


# Level 1 - 로또의 최고 순위와 최저 순위: 내 풀이
def result_count(count):
    if count == 6:
        result = 1
    elif count == 5:
        result = 2
    elif count == 4:
        result = 3
    elif count == 3:
        result = 4
    elif count == 2:
        result = 5
    else:
        result = 6

    return result


def solution2(lottos, win_nums):
    answer = []
    count = 0
    num_zero = lottos.count(0)
    for l in lottos:
        if l in win_nums:
            count += 1

    answer.append(result_count(count))
    count += num_zero
    answer.append(result_count(count))
    answer.sort()
    return answer


# print(solution2([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# print(solution2([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# print(solution2([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))


# Level 1 - 로또의 최고 순위와 최저 순위: 찾은 풀이
def solution3(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1

    return [rank[cnt_0 + ans], rank[ans]]

print(solution3([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution3([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution3([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))