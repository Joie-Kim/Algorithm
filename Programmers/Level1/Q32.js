// Q32. 평균 구하기

function solution(arr) {
  let answer = 0;
  answer = arr.reduce((acc, cur) => acc + cur, 0) / arr.length;
  return answer;
}

console.log(solution([1, 2, 3, 4]));
console.log(solution([5, 5]));
