function solution(numbers) {
  let answer = "";
  let mapNums = numbers
    .map((n, i) => [String(n).repeat(3), i])
    .sort()
    .reverse();

  answer = mapNums.map((n) => numbers[n[1]]).join("");
  return answer[0] === "0" ? "0" : answer;
}

console.log(solution([6, 10, 2]));
console.log(solution([3, 30, 34, 5, 9]));
console.log(solution([0, 0, 0, 0, 0]));
