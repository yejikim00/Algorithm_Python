# 순차 탐색 소스코드
def sequential_search(n, target, array):
    # 각 원소 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i+1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

def sequential():
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    input_data = input().split()
    n = int(input_data[0])  # 원소의 개수
    target = input_data[1]  # 찾고자 하는 문자열

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    array = input().split()

    # 순차 탐색 수행 결과 출력
    print(sequential_search(n, target, array))

# sequential()

# 이진 탐색 - 재귀 함수 이용
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

def binary():
    # n(원소의 개수)과 target(찾고자 하는 문자열) 입력받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result+1)

# binary()

# 이진 탐색 코드 - 반복문 이용
def binary_search_for(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1

    return None

def binary_for():
    # n(원소의 개수)과 target(찾고자 하는 문자열) 입력 받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))

    # 이진탐색 수행 결과 출력
    result = binary_search_for(array, target, 0, n-1)
    if result == None:
        print('원소가 존재하지 않습니다.')
    else:
        print(result+1)

# binary_for()

# 부품 찾기
import sys

def solution1_binary(array, target, start, end):
    array.sort()
    mid = (start + end) // 2

    if start > end:
        print('no')
        return 'no'

    if array[mid] == target:
        print('yes')
        return 'yes'
    elif array[mid] > target:
        solution1_binary(array, target, start, mid-1)
    else:
        solution1_binary(array, target, mid+1, end)

def solution1_binary_search(array, target, start, end):
    array.sort()
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return 'no'

def solution1():
    n = int(input())
    array = list(map(int, input().split()))
    m = int(input())
    find = list(map(int, input().split()))
    answer = []

    for t in find:
        answer.append(solution1_binary_search(array, t, 0, n-1))
    return answer

# answer = solution1()
# for a in answer:
#     print(a, end=' ')


def answer1():
    n = int(input())
    array = [0] * 10

    for i in input().split():
        array[int(i)] = 1

    print(array)

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if array[i] == 1:
            print('yes', end=' ')
        else:
            print('no', end=' ')

def answer2():
    n = int(input())
    array = set(map(int, input().split()))

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if i in array:
            print('yes', end=' ')
        else:
            print('no', end=' ')