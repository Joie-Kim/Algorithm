# link: https://www.acmicpc.net/problem/1967

from collections import deque

n = int(input())
tree = {i:[] for i in range(n+1)}     # 특정 노드를 key로, 연결된 노드 및 가중치를 value로 갖는 딕셔너리 (node: 1 ~ n / keyError 해결을 위해 0부터 시작)
for _ in range(n-1):
  a,b,weight = map(int, input().split())
  tree[a].append((b,weight))
  tree[b].append((a,weight))

def bfs(s):
  queue = deque()
  queue.append((s,0))
  visited = [0]*n     # 인덱스 0 = 노드 넘버 1
  visited[s-1] = 1    # 따라서 '노드 넘버 -1'을 해준다.

  result = [0,0]
  while queue:
    cur,cnt = queue.popleft()
    for node in tree[cur]:
      next_node,value = node[0],node[1]
      if visited[next_node - 1] == 0:
        visited[next_node - 1] = 1
        queue.append((next_node,cnt+value))
        if result[1] < cnt + value:
          result[0] = next_node
          result[1] = cnt + value

  return result

a=bfs(1)
b=bfs(a[0])
print(b[1])
