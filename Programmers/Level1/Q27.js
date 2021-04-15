// Q27. 제일 작은 수 제거하기

/*
function solution(arr) {
  if (arr.len === 1) return -1;
  let answer = [];
  let sorted = [...arr];

  sorted.sort((a, b) => a - b);

  answer = arr.filter((n) => n !== sorted[0]);

  return answer;
}
*/

// Math.min을 사용해서 최소값을 구해보자
function solution(arr) {
  if (arr.length === 1) return [-1];

  let minN = Math.min(...arr);
  arr.splice(arr.indexOf(minN), 1);

  return arr;
}

console.log(solution([4, 3, 2, 1]));
console.log(solution([10]));
