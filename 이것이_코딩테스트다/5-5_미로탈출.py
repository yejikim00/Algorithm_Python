n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))       # 공백 없이 붙어서 입력!

count = 0
def bfs(x, y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 2

