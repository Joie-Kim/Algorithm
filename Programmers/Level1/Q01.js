// Q01. 2개 뽑아서 더하기

function solution(numbers) {
  let answer = [];
  let sumSet = new Set();

  numbers.forEach((n, i) => {
    for (let j = i + 1; j < numbers.length; j++) {
      sumSet.add(n + numbers[j]);
    }
  });

  // sumSet.forEach((s) => answer.push(s));
  answer = [...sumSet];
  answer.sort((a, b) => a - b);

  return answer;
}

console.log(solution([2, 1, 3, 4, 1]));
console.log(solution([5, 0, 2, 7]));
