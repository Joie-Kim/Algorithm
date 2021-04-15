// Q26. 정수 제곱근 판별

function solution(n) {
  if (n ** 0.5 === Math.floor(n ** 0.5)) {
    return (n ** 0.5 + 1) ** 2;
  } else {
    return -1;
  }
}

// isInteger을 사용할 수도 있다.
/*
function solution(n) {
  if (Number.isInteger(n ** 0.5)) {
    return (n ** 0.5 + 1) ** 2;
  } else {
    return -1;
  }
}
*/

console.log(solution(121));
console.log(solution(3));
