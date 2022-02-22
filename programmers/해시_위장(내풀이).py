def solution(clothes):
    dic = {}
    arr = []
    name = set()
    for i in range(len(clothes)):
        name.add(clothes[i][1])
        dic.update({clothes[i][1]: ""})
    print('name:', name)
    for i in name:
        for j in range(len(clothes)):
            print('name:', i)
            print('clothes[i][1]:', clothes[j][1])
            if clothes[j][1] == i:
                arr.append([clothes[j][0]])
                print(arr)
            dic[j] = arr

    return dic


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
