// Q36. x만큼 간격이 있는 n개의 숫자

/*
function solution(x, n) {
  let answer = [x];
  let newX = x;
  while (answer.length < n) {
    newX += x;
    answer.push(newX);
  }
  return answer;
}
*/

// from을 사용해서 배열을 채워보자
function solution(x, n) {
  // 인덱스+1에 x를 곱해서 구함
  let answer = Array.from({ length: n }, (v, i) => (i + 1) * x);
  return answer;
}

console.log(solution(2, 5));
console.log(solution(4, 3));
console.log(solution(-4, 2));
