// Q30. 최대공약수와 최소공배수

function solution(n, m) {
  let answer = [];

  // 최대 공약수 구하는 함수
  const getGcd = (s, l) => {
    let sDiv = new Set();
    let lDiv = new Set();
    let div = [];

    // 작은 수의 약수 구하기 (제곱근까지)
    for (let i = 1; i <= s ** 0.5; i++) {
      if (s % i === 0) {
        sDiv.add(i);
        sDiv.add(Math.floor(s / i));
      }
    }

    // 큰 수의 약수 구하기 (제곱근까지)
    for (let i = 1; i <= l ** 0.5; i++) {
      if (l % i === 0) {
        lDiv.add(i);
        lDiv.add(Math.floor(l / i));
      }
    }

    // 작은 수의 약수 중 큰 수가 가지고 있는 걸 공약수로 함
    sDiv.forEach((n) => {
      if (lDiv.has(n)) {
        div.push(n);
      }
    });

    // 공약수 중 가장 큰 수를 리턴
    return Math.max(...div);
  };

  // 큰 수와 작은 수를 구분
  let larger = n >= m ? n : m;
  let smaller = n < m ? n : m;

  // 최대 공약수와 최소 공배수를 구해서
  let gcd = getGcd(smaller, larger);
  let lcm = (smaller * larger) / gcd;
  // answer 배열에 push
  answer.push(gcd);
  answer.push(lcm);

  return answer;
}

console.log(solution(3, 12));
console.log(solution(2, 5));
