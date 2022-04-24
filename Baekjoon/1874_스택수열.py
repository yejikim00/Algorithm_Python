def solution():
    n = int(input())
    num = [i for i in range(1, n + 1)]
    arr = []
    # ans = []
    result = []
    stack = []
    answer = []

    for i in range(n):
        x = int(input())
        arr.append(x)
        # ans.append(x)

    while stack:
        stack.append(num[0])
        result.append("+")

        for i in range(arr):
            while arr[i] != stack[-1]:
                stack.append(num[0])
                num.pop(0)
                result.append("+")

            answer.append(stack[-1])
            stack.pop()
            num.pop(0)
            result.append("-")

    if arr == answer:
        for r in result:
            print(r)
    else:
        print("NO")


def answer1():
    n = int(input())
    count = 0
    stack = []
    result = []
    no_message = True

    for i in range(0, n):
        x = int(input())

        while count < x:
            count += 1
            stack.append(count)
            result.append("+")

        if stack[-1] == x:
            stack.pop()
            result.append("-")
        else:
            no_message = False
            continue

    if not no_message:
        print("NO")
    else:
        print("\n".join(result))

answer1()