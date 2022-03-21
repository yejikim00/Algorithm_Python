# 선택 정렬 소스 코드
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        print('min_index:', min_index)
        for j in range(i+1, len(array)):
            print('j:', j)
            print(array[min_index], array[j])
            if array[min_index] > array[j]:
                min_index = j
                print('min_index:', min_index)
        array[i], array[min_index] = array[min_index], array[i]

    return array

# print(selection_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8])


# 삽입 정렬 소스 코드
def insertion_sort(array):
    for i in range(1, len(array)):
        print('i:', i)
        for j in range(i, 0, -1):
            print('j:', j)
            print(array[j], array[j-1])
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                print('pass')
                break
        print(array)
    return array

# print(insertion_sort([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))



# 퀵 정렬
def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(array, 0, len(array)-1)
# print(array)

def quick_sort_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    print('left_side:', left_side)
    right_side = [x for x in tail if x > pivot]
    print('right_side:', right_side)

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

# print(quick_sort_python([5, 7, 9, 0, 3, 1, 6, 2, 4, 8]))


# 파이썬 정렬 라이브러리
# sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
# print(result)

# sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
# print(array)


# key값 매개변수
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def settings(data):
    return data[1]

result = sorted(array, key=settings)
# print(result)

# 실전문제1 위에서 아래로
def ex1():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    arr = reversed(sorted(arr))
    for i in arr:
        print(i, end=' ')

# ex1()


# 실전문제 2 성적이 낮은 순서로 학생 출력하기
def ex2():
    n = int(input())
    dic = []

    for i in range(n):
        a, b = input().split()
        dic.append([a, int(b)])

    def settings(data):
        return data[1]

    answer = sorted(dic, key=settings)

    for i in answer:
        print(i[0], end= ' ')

ex2()