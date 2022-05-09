# DP Level 3 - N으로 표현(내 풀이)
def solution(N, number):
    d = [0 for _ in range(10)]
    d[0] = 32001
    d[1] = 2 + (number - 11)
    for i in range(2, len(d)):
        d[i] = d[1] + 2

    if min(d) > 8:
        return -1
    else:
        return d[N]


# DP Level 3 - N으로 표현(찾은 풀이1)
def solution1(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = []
        for j in range(1, i): # i와 j로 다음 숫자의 조합을 나타냄.
            for k in dp[j]: # 각 조합으로 만들 수 있는 경우의 수
                for l in dp[i - j]:
                    temp.append(k + l) # 덧셈
                    if k - l >= 0:
                        temp.append(k - l) # 뺄셈
                    temp.append(k * l) # 곱셈
                    if l != 0 and k != 0:
                        temp.append(k // l) # 나눗셈
        temp.append(int(str(N) * i)) # N을 붙여서 만들 수 있는 경우의 수
        if number in temp:
            return i
        dp.append(list(set(temp)))

    return -1


# DP Level 3 - N으로 표현(찾은 풀이2)
def solution2(N, number):
    s = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):
            for x in s[i_half]:
                for y in s[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x)
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        s.append(case_set)

    return -1


# DP Level 3 - 정수 삼각형(내 풀이)
def solution3(t):
    answer = 0
    dp = [[], [t[0][0] + t[1][0], t[0][0] + t[1][1]]]
    print(dp)
    for i in range(len(t)-1):
        temp = []
        print('t:', t[i])
        # print('dp[{}]: {}'.format(i, dp[i]))
        for k in range(len(dp[i])):
            print('k:', k)
            for j in range(len(t[i])+1):
                if k >= len(dp[i]) or j >= len(t[i]):
                    break
                temp.append(dp[k][k] + t[i][j])
                temp.append(dp[k][k] + t[i][j+1])
                print('i:', i)
                print('j:', j)
                # print('dp[{}][{}]: {}'.format(i, k, dp[i][k]))
                print('t[{}][{}], t[{}][{}]: {}, {}'.format(i+1, j, i+1, j+1, t[i+1][j], t[i+1][j+1]))
                print('temp:', temp)

    print(dp)
    return answer


def solution4(t):
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                t[i][j] += t[i-1][0]
            elif j == len(t[i]) - 1:
                t[i][j] += t[i-1][j-1]
            else:
                t[i][j] += max(t[i-1][j-1], t[i-1][j])

    answer = max(t[-1])

    return answer

print(solution4([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # return 30