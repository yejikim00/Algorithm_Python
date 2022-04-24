import sys
N = int(sys.stdin.readline())

stack = []

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] =="push":
        stack.append(order[1])

    elif order[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


''' 원본
import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
'''