#### 피보나치 수열 호출되는 함수 확인 ####

d = [0] * 100
def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = pibo(x-1) + pibo(x-2)

    return d[x]

# pibo(6)


#### 피보나치 수열 반복문 - 보텀업 방식 ####
def pibo_for():
    d = [0] * 100
    # 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
    d[1] = 1
    d[2] = 1
    n = 99

    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])

# pibo_for()


#### 1로 만들기 ####
# def solution1():
#     x = int(input())
#     count = 0
#

def answer1():
    x = int(input())
    d = [0] * 30001

    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        print('d[' + str(i) + ']: ' + str(d[i]))
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
            print('d[' + str(i) + ' // 2] + 1: ' + str(d[i//2] + 1))
            print('2일 때 d[' + str(i) + ']:' + str(min(d[i], d[i // 2] + 1)))

        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
            print('d[' + str(i) + ' // 3] + 1: ' + str(d[i // 3] + 1))
            print('3일 때 d[' + str(i) + ']:' + str(min(d[i], d[i // 3] + 1)))

        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
            print('d[' + str(i) + ' // 5] + 1: ' + str(d[i // 5] + 1))
            print('5일 때 d[' + str(i) + ']:' + str(min(d[i], d[i // 5] + 1)))

    return d[x]



#### 개미 전사 ####
def solution2(n, num):
    # n = int(input())
    # num = list(map(int, input().split()))
    dp = []
    i = 0
    j = 0

    # while len(dp) != len(num)-2:
    for i in range(len(num)):
        for j in range(i, len(num)):
            print('i: {}, j: {}, num[i]: {}, num[j]: {}, i-j: {}'.format(i, j, num[i], num[j], abs(i-j)))
            if abs(i-j) > 1:
                if len(dp) == i+1:
                    print('dp[i]: {}, num[j]: {}'.format(dp[i], num[j]))
                    dp[i].append(sum(dp[i]) + num[j])
                    print('if dp:', dp)
                else:
                    dp.append([num[i]+num[j]])
                    print('else dp:', dp)

    return dp


def answer2(N, num):
    d = [0] * 100

    d[0] = num[0]
    d[1] = max(num[0], num[1])

    for i in range(2, N):
        d[i] = max(d[i-1], d[i-2] + num[i])

    return d[N-1]


# print(answer2(4, [1, 3, 1, 5]))


### 바닥 공사 ### --> 성공 answer와 동일~!
def solution3():
    N = int(input())
    dp = [0] * 1000
    dp[0] = 1
    dp[1] = 3

    for i in range(2, len(dp)):
        dp[i] = (2*dp[i-2] + dp[i-1]) % 796796

    return dp[N-1]

# print(solution3())


### 효율적인 화폐 구성 ###
def solution4():
    N, M = map(int, input().split())
    coin = []
    dp = [10001] * M+1

    for _ in range(N):
        c = int(input())
        coin.append(c)
        dp[c] = 1
        for i in range(1, M+1):
            if i % c == 0:
                dp[i] = min(dp[i], i//c)

    print(dp[1:M+1])

# print(solution4())


def answer4():
    # 정수 N, M 입력받기
    N, M = map(int, input().split())
    # N개의 화폐 단위 정보 입력받기
    array = []
    for i in range(N):
        array.append(int(input()))

    # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [10001] * (M+1)

    # 다이나믹 프로그래밍 진행(보텀업)
    d[0] = 0 # 0원은 아무것도 필요하지 않으니 0개로 입력한다.
    for i in range(N): # i = 화폐 단위에 해당되는 인덱스 ex) i=2, 2
        for j in range(array[i], M+1): # j = 금액 ex)1, 2, ..., 7
            if d[j - array[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j-array[i]]+1)

    # 계산된 출력
    if d[M] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
        print(-1)
    else:
        print(d[M])

answer4()