# Graph

## 그래프 순회

> : 그래프 탐색이라고도 하며, 그래프의 각 정점을 방문하는 과정을 말한다.

그래프의 각 정점을 방문하는 그래프 순회(Graph Traversals)에는 크게 깊이 우선 탐색(Depth-First Search, DFS)과 너비 우선 탐색(Breadth-First Search, BFS)의 2가지 알고리즘이 있다.

DFS는 주로 스택이나 재귀로 구현하며, 백트래킹을 통해 뛰어난 효용을 보인다. 반면, BFS는 주로 큐로 구현하며, 그래프의 최단 경로를 구하는 문제에 사용된다.

그래프를 표현하는 방법에는 크게 인접 행렬(Adjacency Matrix)과 인접 리스트(Adjacency List)의 2가지 방법이 있다.

### 인접 행렬

인접 행렬은 그래프의 연결 관계를 `이차원 배열`로 나타내는 방식이다.

> 인접 행렬 adj[i][j] : 노드 i에서 노드 j로 가는 간선이 있다면 1, 없다면 0<br>
> (만약 간선에 가중치가 있는 그래프라면 1 대신 가중치 v를 넣어준다.)

유향 그래프가 아닌 무향 그래프일 경우에 인접 행렬이 `대각 성분(adj[i][j]에서 i == j 일 때)을 기준으로 대칭`인 성질을 갖게 된다.

- 장점

  - 구현이 쉬움
  - 노드 i와 노드 j가 연결되어 있는지 확인할 때, adj[i][j]만 확인하면 되기 때문에 O(1)이라는 시간 복잡도에 확인할 수 있음

- 단점
  - 전체 노드의 수가 V이고 간선의 개수가 E일 때, 노드 i에 연결된 모든 노드에 방문하면 O(V)의 시간이 걸림
    > 만약 V가 매우 많고, E가 매우 적다면 특정 노드와 연결된 노드를 찾기 위해 모든 노드를 확인하는 것이 비효율적일 것임 (V = 1,000,000,000, E = 2)

```jsx
// 노드 개수 : 4
// 간선 개수 : 5
// 각 간선의 양 끝 노드 리스트 : [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

function adjMatrix(n, e, edges) {
  let adj = Array.from({ length: n }, () => Array.from({ length: n }, () => 0));
  console.log(adj);

  for (let i = 0; i < e; i++) {
    const v = edges[i][0];
    const u = edges[i][1];

    adj[v - 1][u - 1] = 1;
    adj[u - 1][v - 1] = 1;
  }

  return adj;
}

console.log(
  adjMatrix(4, 5, [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [3, 4],
  ])
);
```

### 인접 리스트

인접 리스트는 그래프의 연결 관계를 출발 노드를 key로 하고, 도착 노드 리스트를 value로 하는 자료형을 사용한다.

> python에서는 `딕셔너리`를 사용해 구현했다.
> javascript에서는 `Map`을 사용해 구현할 수 있을 듯!

> 인접 행렬 adj[i] = [j1, j2, j3] : 노드 i와 연결된(노드 i에서 출발해서 도착하는) 노드 j1, j2, j3이 있다.

- 장점

  - 실제로 연결된 노드들에 대한 정보만 저장하기 때문에 간선의 개수에 비례하는 메모리만 차지함
  - 전체 노드의 수가 V이고 간선의 개수가 E일 때, 간선의 개수만큼만 확인 하면 되기 때문에 O(E)의 시간이 걸림

- 단점
  - 노드 i와 노드 j가 연결되어 있는지 알고 싶다면 adj[i] 리스트를 모두 순회하면 j를 갖는지 확인 해야 하기 때문에 시간복잡도가 O(V)임
    > 인접 행렬의 경우 O(1)

```jsx
// 노드 개수 : 4
// 간선 개수 : 5
// 각 간선의 양 끝 노드 리스트 : [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]

function adjList(n, e, edges) {
  const edgeMap = new Map();
  let v = 0;
  let u = 0;

  for (const edge of edges) {
    v = edge[0];
    u = edge[1];

    if (v in edgeMap) {
      edgeMap[v].push(u);
    } else {
      edgeMap[v] = [u];
    }

    if (u in edgeMap) {
      edgeMap[u].push[v];
    } else {
      edgeMap[u] = [v];
    }
  }

  return edgeMap;
}

console.log(
  adjList(4, 5, [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 3],
    [3, 4],
  ])
);
```
