// [2020 카카오 인턴십] 경주로 건설

function solution(board) {
  const n = board.length;
  // 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
  // 되돌아갈 수 없음. 따라서 예전 방향과 새로운 방향이 2차이 나면 안 됨
  // (ex. 오른쪽(0)으로 이동한 경우 왼쪽(2)으로 이동할 수 없음)
  const direction = [0, 1, 3];
  // bfs한 값을 저장할 큐
  let queue = [[0, 0, null, 0]]; // x좌표, y좌표, 방향, 비용

  // 벽을 판단하는 함수
  // 벽이 아니면 true, 벽이면 false
  function checkWall([x, y]) {
    return (
      x >= 0 &&
      x < n &&
      y >= 0 &&
      y < n &&
      !(x === 0 && y === 0) &&
      board[y][x] !== 1
    );
  }

  while (queue.length) {
    let [x, y, dir, cost] = queue.shift();
    if (board[y][x] >= cost || board[y][x] === 0) {
      board[y][x] = cost;
      direction.forEach((k) => {
        let d = (dir + k) % 4;
        let a = d === 0 ? x + 1 : d === 2 ? x - 1 : x;
        let b = d === 1 ? y + 1 : d === 3 ? y - 1 : y;
        if (checkWall([a, b])) {
          queue.push([
            a,
            b,
            d,
            k === 0 || dir === null ? cost + 100 : cost + 600,
          ]);
        }
      });
    }
  }

  return board[n - 1][n - 1];
}

console.log(
  solution([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 0],
  ])
);
console.log(
  solution([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
  ])
);
