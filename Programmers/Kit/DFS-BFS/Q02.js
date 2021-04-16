function solution(n, computers) {
  let answer = 0;
  let queue = [];
  let visited = [];

  // 방문 배열은 0으로 초기화
  for (let i = 0; i < n; i++) {
    visited.push(0);
  }

  // 모든 노드를 방문하면 반복문 종료
  while (visited.includes(0)) {
    let x = visited.indexOf(0);
    queue.push(x);

    // 네트워크 판별
    while (queue.length > 0) {
      let node = queue.shift();
      visited[node] = 1;

      for (let i = 0; i < n; i++) {
        if (computers[node][i] === 1 && visited[i] === 0) {
          queue.push(i);
        }
      }
    }

    answer += 1;
  }
  return answer;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
);
console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ])
);
