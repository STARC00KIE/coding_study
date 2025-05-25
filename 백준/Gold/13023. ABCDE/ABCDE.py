# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 친구 관계 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
found = False  # 조건을 만족하는지 여부

def dfs(v, depth):
    global found
    if depth == 5:  # 깊이 5 = 친구 5명 사슬 찾음
        found = True
        return

    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
            if found:  # 이미 찾았으면 바로 종료
                return
    visited[v] = False  # 백트래킹

# 모든 사람을 시작점으로 DFS 시도
for i in range(n):
    dfs(i, 1)  # 시작 노드는 depth 1로 시작
    if found:
        break

# 결과 출력
print(1 if found else 0)