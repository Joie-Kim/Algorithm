// Q11. N개의 최소공배수

function solution(arr) {
  // 최대공약수 구하기 (유클리드 호제법)
  function getGcd(a, b) {
    if (b === 0) {
      return a;
    } else {
      return getGcd(b, a % b);
    }
  }

  // 최소공배수 구하기 (두 수의 곱 / 최대공약수)
  let lcm = (arr[0] * arr[1]) / getGcd(arr[0], arr[1]);
  for (let i = 2; i < arr.length; i++) {
    lcm = (lcm * arr[i]) / getGcd(lcm, arr[i]);
  }

  return lcm;
}
