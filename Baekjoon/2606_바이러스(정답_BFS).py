from sys import stdin
from collections import deque

read = stdin.readline

dic = {}
for i in range(int(read())):
    dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print('v:', v)
        for i in dic[v]:
            print('i:', i)
            if i not in visited:
                visited.append(i)
                queue.append(i)
                print(visited)

visited = []
bfs(1, dic)
print(len(visited) - 1)