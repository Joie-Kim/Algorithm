function solution(numbers, target) {
  let answer = 0;
  const numLength = numbers.length;

  const dfs = (level, nSum) => {
    if (level === numLength) {
      if (nSum === target) {
        answer += 1;
      }
    } else {
      dfs(level + 1, nSum + numbers[level]);
      dfs(level + 1, nSum - numbers[level]);
    }
  };

  dfs(0, 0);
  return answer;
}

console.log(solution([1, 1, 1, 1, 1], 3));
