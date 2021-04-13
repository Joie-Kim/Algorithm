// Q08. 나누어 떨어지는 숫자 배열

/*
function solution(arr, divisor) {
  let answer = [];

  arr.forEach((n) => {
    if (n % divisor === 0) {
      answer.push(n);
    }
  });
  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}
*/

function solution(arr, divisor) {
  let answer = [];

  answer = arr.filter((n) => n % divisor === 0);

  return answer.length ? answer.sort((a, b) => a - b) : [-1];
}

console.log(solution([5, 9, 7, 10], 5));
console.log(solution([2, 36, 1, 3], 1));
console.log(solution([3, 2, 6], 10));
