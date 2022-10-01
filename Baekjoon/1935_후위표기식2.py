import sys

def solution():
    answer = 0
    N = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip()
    op = ['+', '-', '*', '/']
    n = []
    num = []

    for _ in range(N):
        n.append(int(sys.stdin.readline()))

    for l in lst:
        if l not in op:
            num.append(n.pop(0))
        else:
            b = num.pop()
            a = num.pop()
            if l == '+':
                answer = a + b
            elif l == '-':
                answer = a - b
            elif l == '*':
                answer = a * b
            elif l == '/':
                answer = a / b

            num.append(answer)

    return answer

# print(solution())


def solution_answer():
    N = int(input())
    lst = list(input())
    num = [int(input()) for i in range(N)]

    stack = []

    for l in lst:
        if 'A' <= l <= 'Z':
            stack.append(num[ord(l) - ord('A')])
        else:
            str2 = stack.pop()
            str1 = stack.pop()

            if l == '+':
                stack.append(str1 + str2)
            elif l == '-':
                stack.append(str1 - str2)
            elif l == '*':
                stack.append(str1 * str2)
            elif l == '/':
                stack.append(str1 / str2)

    print('%.2f' %stack[0])

solution_answer()