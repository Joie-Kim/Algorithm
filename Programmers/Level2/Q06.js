// Q06. 가장 큰 정사각형 찾기

// 다이나믹 프로그래밍으로 풀어야 한다.
function solution(board) {
  let row = board[0].length;
  let column = board.length;
  let width = 0; // 정사각형의 width

  // 보드가 1x1일 때
  if (row === 1 && column === 1) {
    if (board[0].includes(1)) return 1;
    else return 0;
  }

  // 내 위치에서 왼쪽, 왼쪽 상단, 상단의 값을 확인 해서 만들 수 있는 정사각형의 너비를 저장
  for (let i = 1; i < column; i++) {
    for (let j = 1; j < row; j++) {
      if (board[i][j] > 0) {
        const minValue = Math.min(
          board[i][j - 1],
          board[i - 1][j - 1],
          board[i - 1][j]
        );
        board[i][j] = minValue + 1; // 정사각형의 최소 너비는 1 (자기 자신으로 만들 수 있음)
      }

      if (width < board[i][j]) {
        width = board[i][j];
      }
    }
  }

  return width * width;
}

console.log(
  solution([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 0],
  ])
);
console.log(
  solution([
    [0, 0, 1, 1],
    [1, 1, 1, 1],
  ])
);
