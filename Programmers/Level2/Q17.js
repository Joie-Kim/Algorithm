// Q17. 숫자의 표현

function solution(n) {
  var answer = 0;

  function sub(num, result) {
    if (num > result) return;
    if (num === result) {
      answer += 1;
      return;
    }

    sub(num + 1, result - num);
  }

  for (let i = 1; i <= Math.floor(n / 2); i++) {
    sub(i, n);
  }

  return answer + 1;
}

// n의 약수 중 홀수인 것의 개수와 같다고 함.. (수학적으로)
/*
function expressions(num) {
  var answer = 0;

  for (var i = 1; i <= num; i++) {
    if (num % i == 0 && i % 2 == 1) answer++;
  }
  return answer;
}
*/
