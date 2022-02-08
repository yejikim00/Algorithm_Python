n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문한 곳은 1로 처리.
        dfs(x, y-1) # 좌
        dfs(x-1, y) # 상
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True # 상, 하, 좌, 우 모두 1이면 결국 return False로 스택에 쌓였던 함수들이 빠져나와 맨 처음 dfs 함수로 돌아와 retun으로 True 값을 가지고 마지막 함수를 빠져 나간다.
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(n, m):
            result += 1

print(result)