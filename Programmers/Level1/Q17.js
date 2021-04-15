// Q17. 수박수박수박수박수박수?

function solution(n) {
  let answer = "수박".repeat(Math.floor(n / 2));
  return n % 2 !== 0 ? answer + "수" : answer;
}

console.log(solution(3));
console.log(solution(4));
