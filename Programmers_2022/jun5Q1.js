// link: https://programmers.co.kr/learn/courses/30/lessons/77485

function solution(rows, columns, queries) {
  let arr = Array.from(new Array(rows + 1), () => new Array(columns + 1).fill(0));
  let answer = [];

  for (let i = 1; i <= rows; i++) {
    for (let j = 1; j <= columns; j++) {
      arr[i][j] = (i - 1) * columns + j;
    }
  }

  for (let query of queries) {
    const [x1, y1, x2, y2] = query;
    const stack = [];

    for (let j = y1; j < y2; j++) stack.push(arr[x1][j]);
    for (let i = x1; i < x2; i++) stack.push(arr[i][y2]);
    for (let j = y2; j > y1; j--) stack.push(arr[x2][j]);
    for (let i = x2; i > x1; i--) stack.push(arr[i][y1]);

    const temp = stack.pop();
    stack.unshift(temp); // 배열 맨 앞에 값 추가
    answer.push(Math.min(...stack));

    for (let j = y1; j < y2; j++) arr[x1][j] = stack.shift(); // 배열 맨 앞 값 제거
    for (let i = x1; i < x2; i++) arr[i][y2] = stack.shift();
    for (let j = y2; j > y1; j--) arr[x2][j] = stack.shift();
    for (let i = x2; i > x1; i--) arr[i][y1] = stack.shift();
  }

  return answer;
}
