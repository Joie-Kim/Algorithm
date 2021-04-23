# DFS - BFS (그래프, 트리 탐색)

## DFS (깊이 우선 탐색)

DFS는 스택으로 구현하며, 재귀를 이용하면 좀 더 간단하게 구현할 수 있다.

아래 그래프를 탐색해 보자.

```jsx
const graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7: [3],
};
```

### 재귀 구조로 구현

모든 정점 v의 인접 유향(Directed) 간선들을 반복한다.

```jsx
function dfs(v, visited) {
  visited.push(v);
  for (const w of graph[v]) {
    if (!visited.includes(w)) {
      visited = dfs(w, visited);
    }
  }
  return visited;
}

console.log(dfs(1, [])); // 1 → 2 → 5 → 6 → 7 → 3 → 4
```

### 스택을 이용한 반복구조로 구현

스택을 이용해 모든 이접 간선을 추출하고 다시 도착점인 정점을 스택에 삽입하는 구조로 구현했다.

재귀로 구현한 것과 순서가 다른 결과가 출력 되는데, 그 이유는 재귀는 사전식 순서(Lexicographical Order)로 방문한 데 반해 반복 DFS는 역순으로 방문했다. (그림을 그려보면 명확하게 이해 감)

```jsx
function dfs(start) {
  let stack = [start];
  let visited = [];

  while (stack.length) {
    const v = stack.pop();

    if (!visited.includes(v)) {
      visited.push(v);
      for (const w of graph[v]) {
        stack.push(w);
      }
    }
  }

  return visited;
}

console.log(dfs(1)); // 1 → 4 → 3 → 5 → 7 → 6 → 2
```

---

## BFS (너비 우선 탐색)

최단 경로를 찾는 다익스트라 알고리즘 등에 매우 유용하게 쓰인다.

### 큐를 이용한 반복 구조로 구현

```jsx
function dfs(start) {
  let queue = [start];
  let visited = [];

  while (queue.length) {
    const v = queue.shift();

    if (!visited.includes(v)) {
      visited.push(v);
      for (const w of graph[v]) {
        queue.push(w);
      }
    }
  }

  return visited;
}

console.log(dfs(1)); // 1 → 2 → 3 → 4 → 5 → 6 → 7
```

---

## 백 트래킹

> 백트래킹(Backtracking)은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙)해 정답을 찾아가는 범용적인 알고리즘으로 `제약 충족 문제(Constraint Satisfaction Problems)`에 특히 유용하다.

백트래킹은 탐색을 하다가 더 갈 수 없으면 왔던 길을 되돌아가 다른 길을 찾는다는 데에서 유래했다. 백트래킹은 DFS와 같은 방식으로 탐색하는 모든 방법을 뜻하며, DFS는 백트래킹의 골격을 이루는 알고리즘이다.

백트래킹은 주로 재귀로 구현하며, 알고리즘마다 DFS 변형이 조금씩 일어나지만 기본적으로 모두 DFS 범주에 속한다.

백트래킹은 가보고 되돌아오고를 반복한다. 운이 좋으면 시행착오를 덜 거치고 목적지에 도착할 수 있지만, 최악의 경우에는 모든 경우를 다 거친 다음에 도착할 수 있다. 이 때문에 프루트 포스(완전 탐색)와 유사하지만, 한번 방문 후 가능성이 없는 경우에는 즉시 후보를 포기한다는 점에서 매번 같은 경로를 방문하는 브루트 포스와 차이가 있다.

> 트리 탐색에서 불필요한 부분을 버리는 것을 `가지치기(Pruning)`라고 하며, 이를 통해 탐색을 최적화 할 수 있다.

## 제약 충족 문제

백트래킹은 제약 충족 문제(Constraint Satisfaction Problems, CSP)를 풀이하는 데 필수적인 알고리즘이다.

> 제약 충족 문제란 수많은 제약 조건을 충적하는 상태를 찾아내는 수학 문제를 일컫는다.

제약 충족 문제는 대표적으로 스도쿠(Sudoku)처럼 1에서 9까지 숫자를 한 번만 넣는 정답을 찾아내는 모든 문제 유형을 말한다. 스도쿠 외에도 십자말 풀이, 8퀸 문제, 4색 문제 같은 퍼즐 문제와 배낭 문제, 문자열 파싱, 조합 최적화 문제 등이 모두 제약 충족 문제에 속한다.
