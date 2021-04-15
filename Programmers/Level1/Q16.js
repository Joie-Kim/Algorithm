// Q16. 소수 찾기

// 시간 초과
/*
function solution(n) {
  let answer = 1;

  const isPrime = (x) => {
    // 소수 판별 함수
    for (let i = 2; i < x ** 0.5 + 1; i++) {
      if (x % i === 0) return false;
    }
    return true;
  };

  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      answer++;
    }
  }

  return answer;
}
*/

function solution(n) {
  let arr = Array.from({ length: n - 1 }, () => true);
  arr.unshift(false);
  arr.unshift(false);

  let primes = [];

  for (let i = 2; i < n + 1; i++) {
    if (arr[i]) {
      primes.push(i);

      let j = 2 * i;
      while (j < n + 1) {
        arr[j] = false;
        j += i;
      }
    }
  }

  return primes.length;
}

console.log(solution(10));
console.log(solution(5));
