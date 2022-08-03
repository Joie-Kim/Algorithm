# link: https://www.acmicpc.net/problem/13549
# 다시 풀어볼 것

from collections import deque

def bfs():
    visited = [0] * 100001      # i 노드까지 가는 데에 걸린 총 시간을 저장
    q = deque()
    q.append(N)

    while q:
        cur_position = q.popleft()
        if cur_position == K:
            return visited[cur_position]
        for next_position in (cur_position - 1, cur_position + 1, cur_position * 2):
            if 0 <= next_position < 100001:
                if visited[next_position] == 0:
                    if next_position == cur_position * 2 and next_position != 0:    # 순간이동일 경우 (무한루프를 피하기 위해 0 조건도 넣음)
                        visited[next_position] = visited[cur_position]              # 순간이동은 0초 걸림
                        q.appendleft(next_position)                                 # 우선순위가 높기 때문에 
                    else:
                        visited[next_position] = visited[cur_position] + 1          # 순간이동이 아닐 경우, 1초 걸림
                        q.append(next_position)                                     # 우선순위가 순간이동보다 낮음

N, K = map(int, input().split())
print(bfs())