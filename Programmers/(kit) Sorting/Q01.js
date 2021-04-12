function solution(array, commands) {
  let answer = [];

  commands.forEach((c) =>
    answer.push(array.slice(c[0] - 1, c[1]).sort((a, b) => a - b)[c[2] - 1])
  );
  return answer;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
