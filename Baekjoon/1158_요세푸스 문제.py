# import numpy as np
#
# N = int(input())
# K = int(input())
# arr = []
#
# for i in range(N):
#     arr.append(i + 1)
#
# print(arr)
#
# while len(arr) != 0:
#     for i in arr:
#         if i % K == 0:
#             print(i)
#             del arr[i-1]
#             print(arr)

# 풀이 1)
# N, K = map(int, input().split())
# circular_list = []
# answer = []
#
# for i in range(N) :
#     circular_list.append(i+1)
#
# popNum = 0
#
# while len(circular_list) > 0:
#     popNum = (popNum + (K-1)) % len(circular_list)
#     print("popNum:" + str(popNum) + ", K: " + str(K) + ", len(list): " + str(len(circular_list)))
#     popElement = circular_list.pop(popNum)
#     answer.append(str(popElement))
#
# print("<%s>" %(", ".join(answer)))

# 풀이 2)
N, K = map(int, input().split())
list = []
answer = []

for i in range(N):
    list.append(i + 1)

num = 0
while len(list) > 0:
    num = (num + (K - 1)) % len(list)
    answer.append(str(list[num]))
    list.pop(num)

print("<" + ", ".join(answer) + ">")

