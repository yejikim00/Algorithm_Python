n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

first_count = (m // (k+1)) * k + (m % (k+1))
second_count = m - first_count

result = first * first_count + second * second_count
print(result)