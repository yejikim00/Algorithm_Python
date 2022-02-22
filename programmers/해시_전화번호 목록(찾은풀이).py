def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    print(list(zip(phone_book, phone_book[1:])))
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

phone_book = list(map(str, input().split()))
print('answer:', solution(phone_book))