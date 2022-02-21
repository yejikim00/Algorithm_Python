def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if j[0:len(i)] == i:
                answer = False
                return answer
            else:
                answer = True
    return answer


phone_book = list(map(str, input().split()))
print('answer:', solution(phone_book))