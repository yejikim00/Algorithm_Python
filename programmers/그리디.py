# 그리디 Level 1 체육복 - 내 풀이
def solution1(n, lost, reserve):
    answer = [i + 1 for i in range(n)]
    while lost or reserve:
        if reserve[0] + 1 in lost:
            print('+1 in - reserve[0]:', reserve[0])
            lost.remove(reserve[0] + 1)
            print('lost:', lost)
            del reserve[0]
            print('reserve:', reserve)

        elif reserve[0] - 1 in lost:
            print('-1 in - reserve[0]:', reserve[0])
            lost.remove(reserve[0] - 1)
            print('lost:', lost)
            del reserve[0]
            print('reserve:', reserve)

        else:
            for i in lost:
                print('lost i:', i)
                if i in answer:
                    answer.remove(i)
                    lost.remove(i)

        if len(reserve) == 0 or len(lost) == 0:
            break

    print(answer)
    for i in answer:
        if i in lost:
            print('i:', i)
            answer.remove(i)
            print('answer:', answer)

    return len(answer)

# 그리디 Level 1 체육복 - 찾은 풀이
def solution2(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    return n - len(set_lost)

# 그리디 Level 2 조이스틱 - 내 풀이
def solution3(name):
    asci = [ord(i) for i in name]

    count = 0
    for i in range(len(asci)):
        if asci[i] == 65:
            count += 1
        elif (asci[i] - 65) > 13:
            count += 26 - (asci[i] - 65)
        else:
            count += asci[i] - 65
    return asci

# 그리디 Level 2 조이스틱 - 찾은 풀이
def solution4(name):
    # 상하 조정으로 알파벳 바꾸기
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    print(change)
    while True:
        # 바꾼 알파벳의 횟수 answer에 저장 후 값 0으로 변환. 바꾼 알파벳 구분을 위해.
        print('0.', 'idx:', idx)
        answer += change[idx]
        print('1.', answer)
        change[idx] = 0
        print('2.', change)
        if sum(change) == 0:
            return answer

        # 좌우 이동방향 정하기
        left, right = 1, 1
        print('change[idx-left]:', change[idx-left])
        print('change[idx-right]:', change[idx - right])
        while change[idx - left] == 0:
            left += 1       # 왼쪽으로 갔을 때
            print('3.', 'idx:', idx, 'left:', left)
        while change[idx + right] == 0:
            right += 1
            print('4.', 'idx:', idx, 'right:', right)

        # 위치(인덱스) 조정
        if left < right:
            answer += left
            idx += -left
            print('5.', 'left:', left, 'idx:', idx, 'answer:', answer)
        else:
            answer += right
            idx += right
            print('6.', 'right:', right, 'idx:', idx, 'answer:', answer)

    return answer

# 그리디 Level 2 큰 수 만들기 - 내 풀이
from itertools import combinations

def solution5(number, k):
    arr_com = list(combinations(number, len(number) - k))
    arr = []
    for i in arr_com:
        arr.append((''.join(i)))
    return max(arr)


def combination(arr, r):
    # 1.
    used = [0 for _ in range(len(arr))]

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return

        # 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0

    generate([])


def solution6(number, k):
    answer = []
    num = [n for n in number]
    choice = len(number) - k
    arr = combination(num, choice)
    for i in arr:
        print(i)
    # for i in arr:
    #     for j in i:
    #         answer.append(''.join(j))

    return arr

# 그리디 Level 2 큰 수 찾기 - 찾은 풀이
def solution7(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(number) - k])

print(solution7("41772854", 2))