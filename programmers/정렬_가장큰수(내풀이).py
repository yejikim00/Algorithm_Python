def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    answer = ''.join(numbers)
    return answer