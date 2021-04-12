// Q05. 3진법 뒤집기

/*
function solution(n) {
  let answer = 0;

  //n = n.toString(3).split("").reverse().join("");
  n = [...n.toString(3)].reverse().join("");
  answer = parseInt(n, 3);

  return answer;
}
*/

function solution(n) {
  let answer = [];

  while (n !== 0) {
    answer.unshift(n % 3);
    n = Math.floor(n / 3);
  }

  return answer.reduce((acc, cur, i) => acc + cur * Math.pow(3, i), 0);
}

console.log(solution(45));
console.log(solution(125));
