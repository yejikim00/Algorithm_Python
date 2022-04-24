import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque()

for i in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        deq.append(order[1])

    elif order[0] == "pop":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

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

# deque 사용 x
# import sys
#
# N = int(sys.stdin.readline())
# count = 0
# queue = []
#
# for i in range(N):
#     order = sys.stdin.readline().split()
#
#     if order[0] == "push":
#         queue.append(order[1])
#
#     elif order[0] == "pop":
#         if len(queue) > count:
#             print(queue[count])
#             count += 1
#         else:
#             print(-1)
#
#     elif order[0] == "size":
#         print(len(queue) - count)
#
#     elif order[0] == "empty":
#         if len(queue) == count:
#             print(1)
#             count = 0
#             queue = []
#         else:
#             print(0)
#
#     elif order[0] == "front":
#         if len(queue) > count:
#             print(queue[count])
#         else:
#             print(-1)
#
#     elif order[0] == "back":
#         if len(queue) > count:
#             print(queue[-1])
#         else:
#             print(-1)