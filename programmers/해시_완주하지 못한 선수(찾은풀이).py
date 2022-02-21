def solution(participant, completion):
    participant.sort()
    print('participant:', participant)
    completion.sort()
    print('completion:', completion)
    for p, c in zip(participant, completion):
        print('p:', p, ', c:', c)
        if p != c:
            return p
    return participant[-1]


participant = list(map(str, input().split()))
completion = list(map(str, input().split()))
print(solution(participant, completion))