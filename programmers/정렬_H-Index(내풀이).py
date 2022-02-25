def solution(citations):
    answer = []
    citations.sort(reverse=True)
    for i in range(len(citations)):
        h = citations[i]
        if h <= len(citations[i:]):
            answer.append(len(citations[i:]))
            print('answer:', answer)
    return answer[0]


citations = [3, 0, 1, 5, 6]
print(solution(citations))