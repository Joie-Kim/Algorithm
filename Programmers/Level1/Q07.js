// Q07. 같은 숫자는 싫어

/*
function solution(arr) {
  let answer = [];
  let len = 0;

  arr.forEach((n) => {
    len = answer.length;

    if (len === 0 || answer[len - 1] !== n) {
      answer.push(n);
    }
  });

  return answer;
}
*/

function solution(arr) {
  let answer = [];

  answer = arr.filter((n, i) => n !== arr[i + 1]);

  return answer;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));
console.log(solution([4, 4, 4, 3, 3]));
