/*
(세 자리 수) × (세 자리 수) 과정마다 출력하고, 맨 마지막에 결과를 출력하는 프로그램을 작성하시오.

ex)
input:
472
385
---
output:
2360
3776
1416
181720
*/

const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().split("\n");

const [a, b] = inputData;
let positionNumber = 0;
let result = 0;

for (let i = b.length - 1; i >= 0; i--) {
  const subResult = b[i] * a;
  console.log(subResult);

  result += subResult * Math.pow(10, positionNumber);
  positionNumber++;
}

console.log(result);
