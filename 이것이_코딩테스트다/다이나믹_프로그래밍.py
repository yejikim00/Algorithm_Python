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

# print(answer1())