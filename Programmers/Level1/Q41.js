// Q41. 소수 만들기

function solution(nums) {
  let answer = 0;

  function isPrime(x) {
    for (let i = 2; i <= x ** 0.5; i++) {
      if (x % i === 0) {
        return false;
      }
    }
    return true;
  }

  function getCombination(arr, r) {
    let result = [];
    const n = arr.length;

    if (r === 1) return arr.map((value) => [value]);

    for (let i = 0; i < n; i++) {
      let fixed = arr[i];
      let rest = arr.slice(i + 1);
      let combinations = getCombination(rest, r - 1);
      let attached = combinations.map((comb) => [fixed, ...comb]);
      result.push(...attached);
    }

    return result;
  }

  let combArr = getCombination(nums, 3);

  for (const comb of combArr) {
    const sum = comb.reduce((acc, cur) => acc + cur, 0);
    const flag = isPrime(sum);
    if (flag === true) answer += 1;
  }

  return answer;
}
