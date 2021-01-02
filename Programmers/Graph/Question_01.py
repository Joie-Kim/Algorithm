from collections import deque, defaultdict

def solution(n, edge):
    edges = defaultdict(list)               # {x: []} : x에 연결된 노드 리스트 / 딕셔너리 기본값을 list로 초기화
    dists = {i:0 for i in range(1, n+1)}    # i:n : 1번 노드부터 i번 노드까지의 거리 n

    for u, v in edge:       # 연결된 노드를 찾음
        edges[u].append(v)  # 양방향이기 때문에 모두 넣어줌
        edges[v].append(u)

    q = deque(edges[1])     # bfs를 위한 deque
    dist = 1                # bfs를 하는 현재의 1번 노드와의 거리

    while q:                        # bfs
        size = len(q)
        for _ in range(size):
            v = q.popleft()
            if dists[v] == 0:       # 아직 방문하지 않은 노드라면
                dists[v] = dist     # 현재의 1번 노드와의 거리를 넣어주고
                for w in edges[v]:  # 해당 노드와 연결된 노드를
                    q.append(w)     # 탐색할 노드(deque)에 넣어준다.
        dist += 1

    del dists[1]                            # 1번 노드에 대한 정보는 필요 없으므로 삭제
    dists_val = list(dists.values())        # dists의 values를 리스트로 만듦

    return dists_val.count(max(dists_val))  # 최댓값의 개수를 반환