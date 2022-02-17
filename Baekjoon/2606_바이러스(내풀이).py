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

''' 
새로 찾은 풀이

n = int(input())
m = int(input())

matrix = [[0] * (n+1) for i in range(n+1)]
seen = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

result = []
def dfs(v):
    seen[v] = 1
    for i in range(1, n+1):
        if matrix[v][i] == 1 and seen[i] == 0:
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))
'''