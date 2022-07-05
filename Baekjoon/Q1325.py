# link: https://www.acmicpc.net/problem/1325
from collections import deque

# 입력값 정리
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[b].append(a)

# bfs 함수 정의
def bfs(start):
    count = 1
    queue = deque([start])                          # 방문할 노드
    visited = [0 for _ in range(n+1)]               # 방문한 노드
    visited[start] = 1

    while queue:
        curNode = queue.popleft()
        for node in graph[curNode]:
            if visited[node] == 0:    # 해당 노드에 방문했는지 확인
                visited[node] = 1     # 해당 노드에 방문했음을 표시
                count += 1            # 방문한 노드 갯수 세기
                queue.append(node)    # queue(방문할 노드)에 넣기
    
    return count

# 최댓값만 넣기
answer = []
maxCount = 1

for i in range(1, n+1):
    count = bfs(i)
    if count > maxCount:
        maxCount = count
        answer.clear()
        answer.append(i)
    elif count == maxCount:
        answer.append(i)

print(*answer)