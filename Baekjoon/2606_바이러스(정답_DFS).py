from sys import stdin

read = stdin.readline

dic = {}
for i in range(int(read())):  # 컴퓨터 개수 받아오기(7개) 즉 for문 반복 횟수를 입력받음. 그만큼 컴퓨터가 생성됨.
    dic[i + 1] = set()  # 그 수만큼 dic이라는 딕셔너리의 key 만들기, dic인의 i+1이 key이름. 연결된 컴퓨터들을 집합 연산자로 표현.
                        # key의 값(value)을 집합 형태로 저장.
for j in range(int(read())):  # 연결된 쌍 개수 입력받음. 6을 입력하니까 6쌍이 연결되어 있다는 것을 알려주고, 6번 반복해 그 6쌍을 적어줌.
    a, b = map(int, read().split())  # 쌍을 각각 작성해줌. a에 연결된 b, b에 연결된 a로 해당되는 key에 값으로 넣어줌.
    dic[a].add(b)                    # 이미 만들어진 집합에 값 추가.
    dic[b].add(a)


def dfs(start, dic):
    for i in dic[start]:
        print('i:', i)
        if i not in visited:
            visited.append(i)       # 이웃하게 연결되어 있는 곳을 탐색해 visited에 넣어줌.
            print(visited)
            dfs(i, dic)


visited = []
dfs(1, dic)
print(len(visited) - 1)     # 이미 감염되었던 1번 컴퓨터는 제외하기 위해 1을 뺴줌.
