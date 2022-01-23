N, K = map(int, input().split())
result = 0

while True:
    target = (N // K) * K
    print("target:", target)
    result += (N - target)
    print("result:", result)
    N = target
    print("N:", N)

    if N < K:
        break

    result += 1
    N //= K

result += (N - 1)
print(result)