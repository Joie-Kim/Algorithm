function solution(n, costs) {
  let answer = 0;

  // 비용이 적은 순으로 정렬
  costs.sort((c1, c2) => c1[2] - c2[2]);
  // 방문한 노드를 중복없이 저장
  let visited = new Set().add(costs[0][0]);

  // 방문한 노드의 수가 전체 노드의 수와 같아지면 순회 종료
  while (visited.size !== n) {
    // costs 순회
    for (let i = 0; i < costs.length; i++) {
      // 만약 출발지와 도착지 모두 방문한 노드에 있을 경우, 건너뜀
      // 순환을 막기 위해서
      if (visited.has(costs[i][0]) && visited.has(costs[i][1])) continue;
      // 만약 출발지와 도착지 중 하나가 이미 방문한 노드라면 (즉, 경로가 이어진다면)
      if (visited.has(costs[i][0]) || visited.has(costs[i][1])) {
        // 방문한 노드에 추가하고
        visited.add(costs[i][0]);
        visited.add(costs[i][1]);
        // 비용을 추가함
        answer += costs[i][2];
        // 그리고 처음부터 다시 순회하기 위해 for문을 빠져나옴
        break;
      }
    }
  }

  return answer;
}

console.log(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ])
);
console.log(
  solution(5, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 3],
    [2, 3, 8],
    [3, 4, 1],
  ])
);
console.log(
  solution(6, [
    [0, 1, 5],
    [0, 3, 2],
    [0, 4, 3],
    [1, 4, 1],
    [3, 4, 10],
    [1, 2, 2],
    [2, 5, 3],
    [4, 5, 4],
  ])
);
