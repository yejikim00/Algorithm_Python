def solution(participant, completion):
    for i in range(len(participant)):
        if completion.count(participant[i]) == 0:
            answer = participant[i]
        if participant.count(participant[i]) >= 2 and completion.count(participant[i]) == int(participant.count(participant[i])-1):
            answer = participant[i]
    return answer


participant = list(map(str, input().split()))
completion = list(map(str, input().split()))
print(solution(participant, completion))