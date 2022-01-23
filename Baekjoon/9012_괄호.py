T = int(input())

for _ in range(T):
    ps = input()
    sum = 0
    vps = list(ps)
    for j in vps:
        if j == "(":
            sum += 1
        elif j == ")":
            sum -= 1
        if sum < 0:
            print("NO")
            break
    if sum == 0:
        print("YES")
    elif sum > 0:
        print("NO")