// Q21. 약수의 합

function solution(n) {
  if (n === 0) return 0;
  let answer = 0;
  let nSet = new Set();

  for (let i = 1; i <= n ** 0.5; i++) {
    if (n % i === 0) {
      nSet.add(i);
      nSet.add(Math.floor(n / i));
    }
  }

  nSet.forEach((n) => (answer += n));
  return answer;
}

console.log(solution(12));
console.log(solution(5));
