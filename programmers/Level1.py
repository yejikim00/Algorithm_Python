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


print(solution1(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution1(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))