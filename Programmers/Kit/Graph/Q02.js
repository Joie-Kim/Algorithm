function solution(n, results) {
  let answer = 0;
  let wins = new Map();
  let loses = new Map();

  for (let i = 1; i <= n; i++) {
    wins[i] = new Set();
    loses[i] = new Set();
  }

  results.forEach((result) => {
    const [winner, loser] = result;

    wins[winner].add(loser);
    loses[loser].add(winner);
  });

  for (let i = 1; i <= n; i++) {
    for (const loser of wins[i]) {
      for (const winner of loses[i]) {
        loses[loser].add(winner);
      }
    }
    for (const winner of loses[i]) {
      for (const loser of wins[i]) {
        wins[winner].add(loser);
      }
    }
  }

  console.log(wins);
  console.log(loses);

  for (let i = 1; i <= n; i++) {
    if (wins[i].size + loses[i].size === n - 1) {
      answer++;
    }
  }

  return answer;
}

console.log(
  solution(5, [
    [4, 3],
    [4, 2],
    [3, 2],
    [1, 2],
    [2, 5],
  ])
);
