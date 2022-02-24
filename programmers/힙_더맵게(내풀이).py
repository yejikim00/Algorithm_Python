scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = 0
while scoville[0] < K:
    print(scoville)
    first = scoville[0]
    second = scoville[1]
    new_K = first + (second * 2)
    scoville.pop(0)
    scoville.pop(0)
    scoville.insert(0, new_K)
    print("update:", scoville)
    answer += 1
    scoville.sort()
    if len(scoville) == 1:
        answer = -1

print(answer)