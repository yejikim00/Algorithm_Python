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
    reports = {x: 0 for x in id_list}  # 신고 당한 사람의 신고 당한 횟수

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


# print(solution3([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# print(solution3([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# print(solution3([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))


# Level 1 - 신규 아이디 추천: 내 풀이
def solution4(new_id):
    answer = ''
    id_list = [new_id[i] for i in range(len(new_id))]
    correct_id = [45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 95]
    delete_id = []
    for i in range(len(id_list)):
        if ord(id_list[i]) >= 65 and ord(id_list[i]) <= 90:
            id_list[i] = chr(ord(id_list[i]) + 32)
        if ord(id_list[i]) not in correct_id:
            delete_id.append(i)
        if i != len(id_list) - 1:
            if ord(id_list[i]) == 46 and ord(id_list[i + 1]) == 46:
                delete_id.append(i)
        if i == 0 or i == len(id_list):
            if ord(id_list[i]) == 46:
                delete_id.append(i)
        if id_list is False:
            id_list.append('a')
        # if len(id_list) >= 16:
        #     id_list = id_list[:15]
        #     if ord(id_list[-1]) == 46:
        #         id_list = id_list[:-1]
        # if len(id_list) <= 2:
        #     while len(id_list) < 3:
        #         id_list.append(id_list[-1])

        for i in delete_id[:]:
            id_list.remove(id_list[i])
        answer = ''.join(id_list)
    return answer


# Level 1 - 신규 아이디 추천: 찾은 풀이1
def solution5(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # 5단계
    answer = 'a' if answer == '' else answer

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) < 3:
        answer = answer + answer[-1] * (3 - len(answer))

    return answer


# Level 1 - 신규 아이디 추천: 찾은 풀이2
# 정규식 표현 사용
import re


def solution6(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub('[^a-z\d\-_.]', '', new_id)

    # 3단계
    new_id = re.sub('\.+', '.', new_id)

    # 4단계
    new_id = re.sub('^[.]|[.]$', '', new_id)

    # 5단계, 6단계 자르기
    new_id = 'a' if len(new_id) == 0 else new_id[:15]

    # 6단계 나머지
    new_id = re.sub('[.]$', '', new_id)

    # 7단계
    new_id = new_id if len(new_id) > 2 else new_id + new_id[-1] * (3-len(new_id))

    return new_id


# print(solution6("...!@BaT#*..y.abcdefghijklm"))
# print(solution6("z-+.^."))
# print(solution6("=.="))
# print(solution6("123_.def"))
# print(solution6("abcdefghijklmn.p"))



# Level 1 - 숫자 문자열과 영단어: 내 풀이
def solution7(s):
    answer = 0
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for n in num:
        if n in s:
            s = s.replace(n, str(num.index(n)))

    answer = int(s)

    return answer


# print(solution7("one4seveneight"))
# print(solution7("23four5six7"))
# print(solution7("2three45sixseven"))
# print(solution7("123"))



# Level 1 - 숫자 문자열과 영단어: 찾은 풀이
def solution8(s):
    num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    answer = s

    for key, value in num_dic.items():
        answer = answer.replace(key, value)

    return int(answer)


# print(solution8("one4seveneight"))
# print(solution8("23four5six7"))
# print(solution8("2three45sixseven"))
# print(solution8("123"))



# Level 1 - 키패드 누르기: 내 풀이
def solution9(numbers, hand):
    answer = ''
    r = 0
    l = 0

    for num in numbers:
        if num % 3 == 1:
            answer = answer + 'L'
            l = num

        elif num % 3 == 0:
            answer = answer + 'R'
            r = num

        else:
            if l % 3 == 2 and r % 3 == 2:
                num = 10
                if abs(l - num) > abs(r - num):
                    answer = answer + 'R'
                    r = num
                elif abs(l - num) < abs(r - num):
                    answer = answer + 'L'
                    l = num
                elif abs(l - num) == abs(r - num):
                    if hand == 'right':
                        answer = answer + 'R'
                        r = num
                    elif hand == 'left':
                        answer = answer + 'L'
                        l = num
            else:
                if abs(l - num) > abs(r - num):
                    answer = answer + 'R'
                    r = num
                elif abs(l - num) < abs(r - num):
                    answer = answer + 'L'
                    l = num
                elif abs(l - num) == abs(r - num):
                    if hand == 'right':
                        answer = answer + 'R'
                        r = num
                    elif hand == 'left':
                        answer = answer + 'L'
                        l = num

    return answer



# Level 1 - 키패드 누르기: 찾은 풀이1
def solution10(numbers, hand):
    answer = ''
    l = 10
    r = 12

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            l = n

        elif n in [3, 6, 9]:
            answer += 'R'
            r = n

        else:
            if n == 0:
                n = 11

            l_dis = abs(l - n) // 3 + abs(l - n) % 3
            r_dis = abs(r - n) // 3 + abs(r - n) % 3

            if l_dis > r_dis:
                answer += 'R'
                r = n

            elif l_dis < r_dis:
                answer += 'L'
                l = n

            else:
                if hand == 'right':
                    answer += 'R'
                    r = n
                else:
                    answer += 'L'
                    l = n

    return answer


# Level 1 - 키패드 누르기: 찾은 풀이2
def solution11(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

print(solution11([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution11([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution11([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))