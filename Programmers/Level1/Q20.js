// Q20. 내적

/*
function solution(a, b) {
  let len = a.length;
  let answer = 0;

  for (let i = 0; i < len; i++) {
    answer += a[i] * b[i];
  }
  return answer;
}
*/

// 누적 값을 구할 땐, reduce를 사용하자
function solution(a, b) {
  let answer = 0;

  answer = a.reduce((acc, cur, i) => acc + cur * b[i], 0);
  return answer;
}

console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
console.log(solution([-1, 0, 1], [1, 0, -1]));
