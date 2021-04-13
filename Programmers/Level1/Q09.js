// Q09. 두 정수 사이의 합

function solution(a, b) {
  if (a > b) {
    answer = (a * (a + 1)) / 2 - ((b - 1) * b) / 2;
  } else if (a < b) {
    answer = (b * (b + 1)) / 2 - ((a - 1) * a) / 2;
  } else {
    answer = a;
  }

  return answer;
}

console.log(solution(3, 5));
console.log(solution(3, 3));
console.log(solution(5, 3));
