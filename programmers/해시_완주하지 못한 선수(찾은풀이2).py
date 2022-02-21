from collections import Counter

def solution(participant, completion):
    print(Counter(participant))
    print(Counter(completion))
    answer = Counter(participant) - Counter(completion)
    print(answer)
    print(answer.keys())
    return list(answer.keys())[0]    # 리스트 형태로 반환

participant = list(map(str, input().split()))
completion = list(map(str, input().split()))
print(solution(participant, completion))