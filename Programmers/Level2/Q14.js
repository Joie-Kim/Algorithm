// Q14. 피보나치 수

function solution(n) {
  var answer = 0;
  let result = [0, 1];

  function fib(n) {
    for (let i = 2; i <= n; i++) {
      result[i] = (result[i - 2] % 1234567) + (result[i - 1] % 1234567);
    }
    return result[n];
  }

  answer = fib(n) % 1234567;

  return answer;
}
