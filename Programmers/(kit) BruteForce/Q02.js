function solution(numbers) {
  let answer = 0;
  let prime = new Set();
  let prev_elements = [];

  // 소수인지 판별하는 함수
  const isPrime = (x) => {
    if (x === 0 || x === 1) return false;

    let i = 2;
    while (i * i <= x) {
      if (x % i === 0) return false;
      i += 1;
    }
    return true;
  };

  // 순열을 만들고, 소수인 것만 집합에 넣음 (재귀)
  const dfs = (elements) => {
    for (let i = 0; i < elements.length; i++) {
      let next_elements = [...elements];
      next_elements.splice(i, 1);
      prev_elements.push(elements[i]);

      dfs(next_elements);

      if (isPrime(Number(prev_elements.join("")))) {
        prime.add(Number(prev_elements.join("")));
      }

      prev_elements.pop();
    }
  };

  dfs(numbers);
  return prime.size;
}

console.log(solution("17"));
console.log(solution("011"));
