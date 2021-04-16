// Q33. 하샤드 수

function solution(n) {
  let nCopy = n;
  let nSum = 0;

  while (nCopy > 0) {
    nSum += nCopy % 10;
    nCopy = Math.floor(nCopy / 10);
  }

  return n % nSum === 0 ? true : false;
}

console.log(solution(10));
console.log(solution(11));
console.log(solution(12));
console.log(solution(13));
