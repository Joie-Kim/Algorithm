// Q44. 약수의 개수와 덧셈

function solution(left, right) {
  var answer = 0;

  function isEven(x) {
    let result = new Set();
    for (let i = 1; i <= x ** 0.5; i++) {
      if (x % i === 0) {
        result.add(x / i);
        result.add(i);
      }
    }

    if (result.size % 2 === 0) return true;
    else return false;
  }

  for (let i = left; i <= right; i++) {
    answer += i * (isEven(i) ? 1 : -1);
  }

  return answer;
}

// 제곱근이 정수인 경우, 무조건 홀수 (약수는 항상 짝이 존재하기 때문)
// 그걸 이용한 풀이
/*
function solution(left, right) {
    var answer = 0;
    for (let i = left; i <= right; i++) {
        if (Number.isInteger(Math.sqrt(i))) {
            answer -= i;
        } else {
            answer += i;
        }
    }
    return answer;
}
*/
