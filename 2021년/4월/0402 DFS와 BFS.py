# 백준1260_DFS와 BFS_bfs, dfs_실버 2
# 옛날에 풀어본 문제 다시 풀어봄

from collections import deque

def dfs(v):
    dfs_count.append(v)
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i)

def bfs(v):
    move = deque()
    move.append(v)
    while move:
        new_v = move.popleft()
        bfs_count.append(new_v)
        for i in range(1,n+1):
            if visited[i] == 0 and graph[new_v][i] == 1:
                visited[i] = 1
                move.append(i)
                

n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
dfs_count = []
bfs_count = []
for i in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited[v] = 1
dfs(v)
visited = [0]*(n+1)
visited[v] = 1
bfs(v)
print(*dfs_count)
print(*bfs_count)