computer = int(input())
link = int(input())

graph = []
for i in range(link):
    graph.append(list(map(int, input().split())))


def dfs(graph, v, visited):
    global count
    count = 0
    visited[v] = True

    for j in graph[v-2]:
        if not visited[j]:
            count += 1
            dfs(graph, j, visited)


visited = [False] * (computer + 1)
dfs(graph, 1, visited)
print(count)