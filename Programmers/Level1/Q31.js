// Q31. 콜라츠 추측

function solution(n) {
  if (n === 1) return 0;
  let answer = 0;

  while (answer < 500) {
    if (n % 2 === 0) n /= 2;
    else n = n * 3 + 1;

    answer++;

    if (n === 1) break;
  }
  return answer === 500 ? -1 : answer;
}

console.log(solution(6));
console.log(solution(16));
console.log(solution(626331));
