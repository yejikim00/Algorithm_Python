import sys

N = int(sys.stdin.readline())

while True:
    if N == 1 or N == 3:
        print(-1)
        break

    elif (N % 5) % 2 == 0:
        print((N // 5) + (N % 5) // 2)
        break

    else:
        print((N // 5) - 1 + (N % 5 + 5) // 2)
        break