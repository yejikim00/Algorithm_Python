N = int(input())

five_coin = 0
two_coin = 0
result = 0

while N != 0:
    if N % 5 == 0:
        five_coin += N // 5
        result = five_coin + two_coin
        print(result)
        break

    elif N % 5 != 0:
        while True:
            N = N - 5
            five_coin += 1
            if N == 1:
                print(-1)
                N = 0
                break
            elif N % 2 == 0:
                two_coin = N // 2
                result = five_coin + two_coin
                print(result)
                N = 0
                break
            elif N % 2 != 0:
                continue