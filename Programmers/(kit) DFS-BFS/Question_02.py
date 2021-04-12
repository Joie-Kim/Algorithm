def solution(n, computers):
    answer = 0
    queue = []          # 방문할 노드
    visited = [0] * n   # 방문한 노드

    while 0 in visited:         # 방문하지 않은 노드가 있다면
        x = visited.index(0)    # 방문하지 않은 노드를 찾아서 x에 저장 (인덱스 값)
        queue.append(x)         # 해당 노드를 queue에 넣음 (곧 방문할 것)
        
        while queue:
            node = queue.pop(0)
            visited[node] = 1                                   # 해당 노드에 방문했음을 표시
            for i in range(n):                                  # 해당 노드와 인접한 노드들을 확인
                if computers[node][i] == 1 and visited[i] == 0: # 인접하고, 방문하지 않은 노드이면
                    queue.append(i)                             # queue(방문할 노드)에 넣음
                                                                # 해당 노드와 연결된 노드를 모두 검사하고 나면
        answer += 1                                             # 네트워크 개수 1개 증가

    return answer