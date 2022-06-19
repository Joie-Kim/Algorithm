// link: https://programmers.co.kr/learn/courses/30/lessons/49994

function solution(dirs) {
  const move = { U: [0, 1], D: [0, -1], R: [1, 0], L: [-1, 0] };
  let curPoint = [0, 0];
  let visited = new Set();

  for (let dir of dirs) {
    const nextX = curPoint[0] + move[dir][0];
    const nextY = curPoint[1] + move[dir][1];

    if (Math.abs(nextX) > 5 || Math.abs(nextY) > 5) continue;

    visited.add('' + curPoint[0] + curPoint[1] + nextX + nextY);
    visited.add('' + nextX + nextY + curPoint[0] + curPoint[1]);

    curPoint = [nextX, nextY];
  }

  return visited.size / 2;
}
