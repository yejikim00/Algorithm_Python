'''
import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push_front":
        deq.appendleft(order[1])

    elif order[0] == "push_back":
        deq.append(order[1])

    elif order[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

    elif order[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())

    elif order[0] == "size":
        print(len(deq))

    elif order[0] == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif order[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif order[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
'''

import sys

def push_front(x, deq):
    tmp = [x]
    tmp.extend(deq)  # 기존의 tmp 리스트에 deq 리스트를 더한다.
    deq = tmp
    return deq

def push_back(x, deq):
    deq.append(x)
    return deq

def pop_front(deq):
    if deq:
        print(deq.pop(0))
    else:
        print(-1)

def pop_back(deq):
    if deq:
        print(deq.pop())
    else:
        print(-1)

def size(deq):
    print(len(deq))

def empty(deq):
    if not deq:
        print(1)
    else:
        print(0)

def front(deq):
    if deq:
        print(deq[0])
    else:
        print(-1)

def back(deq):
    if deq:
        print(deq[-1])
    else:
        print(-1)

statements_dict = {
    'push_front': push_front,
    'push_back': push_back,
    'pop_front': pop_front,
    'pop_back': pop_back,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

N = int(sys.stdin.readline())
deq = []

for _ in range(N):
    statement = input().split(" ")

    if len(statement) == 1:
        cmd = statement[0]
        statements_dict[cmd](deq)
    else:
        cmd, x = statement
        deq = statements_dict[cmd](x, deq)