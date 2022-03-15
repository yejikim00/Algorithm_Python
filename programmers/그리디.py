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

