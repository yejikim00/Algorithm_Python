# import sys
#
# N = int(sys.stdin.readline())
# num = []
# count = 0
#
# for i in range(N):
#     num.append(i+1)
#
# for j in range(len(num)-1):
#     num.append(num[count+1])
#     count+=2
#
# print(num[-1])

# deque 이용
import sys
from collections import deque

N = int(sys.stdin.readline())
deq = deque(list(range(1, N+1)))

while len(deq) > 1:
    deq.popleft()
    # deq.append(deq.popleft())
    deq.rotate(-1)
    print(deq)

print(deq[0])