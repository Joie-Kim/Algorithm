/*
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
*/

const fs = require("fs");
const inputData = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((value) => +value);

const [a, b] = inputData;

console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(Math.floor(a / b)); // 결과 예시에서 소수점이 없었기 때문에
console.log(a % b);
