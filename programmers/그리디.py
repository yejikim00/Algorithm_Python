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

# print(solution7("41772854", 2))

# 그리디 Level 2 구명보트 - 내 풀이
def solution8(people, limit):
    answer = 0
    save = []
    people.sort()

    for i in range(len(people)):
        save.append(people[i])
        if sum(save) > limit:
            people.pop(i)
            save.pop()
            answer += 1
        elif sum(save) == limit:
            answer += 1
            save.clear()

    answer += len(people)
    return answer

# 그리디 Level 2 구명보트 - 찾은 풀이
def solution9(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1

        answer += 1

    return answer


# 그리디 Level 3 - 섬 연결하기(내 풀이)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution10(n, costs):
    edges = []
    result = 0
    parent = [0] * (n+1)

    for i in range(1, n+1):
        parent[i] = i

    for edge in costs:
        a, b, cost = edge
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    return result


# 그리디 Level 3 - 섬 연결하기(찾은 풀이1)
def find_11(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def solution11(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parent = [i for i in range(n)]
    bridges = 0

    for cost, a, b in edges:
        if find_11(parent, a) != find_11(parent, b):
            answer += cost
            parent[find_11(parent, a)] = b
            bridges += 1
        if bridges == n-1:
            break

    return answer


# 그리디 Level 3 - 섬 연결하기(찾은 풀이2)
def solution12(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 비용 기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합

    # Kruskal 알고리즘 이용
    while len(connect) != n:
        print(connect)
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break

    return answer


