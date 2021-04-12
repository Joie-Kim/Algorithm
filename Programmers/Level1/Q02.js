// Q02. 크레인 인형뽑기 게임

function solution(board, moves) {
  let answer = 0;
  let len = board.length;
  let stack = [];

  moves.forEach((moveIdx) => {
    for (let i = 0; i < len; i++) {
      let doll = board[i][moveIdx - 1];
      board[i][moveIdx - 1] = 0;

      if (doll === 0) {
        continue;
      } else {
        if (stack.length !== 0 && stack[stack.length - 1] === doll) {
          stack.pop();
          answer += 2;
        } else {
          stack.push(doll);
        }

        break;
      }
    }
  });

  return answer;
}

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
);
