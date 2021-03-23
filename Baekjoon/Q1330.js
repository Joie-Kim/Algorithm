/*
두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

- A가 B보다 큰 경우에는 '>'를 출력
- A가 B보다 작은 경우에는 '<'를 출력
- A와 B가 같은 경우에는 '=='를 출력
*/

const fs = require("fs");
// 꼭 정수로 바꿔 준다.
// 문자 대소 비교를 할 경우, 결과가 다르기 때문
// 예를 들어, 10과 2를 비교한다고 하면 정수일 때는 10이 크지만 문자열일 때는 2가 크다.
const inputData = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((value) => +value);

const [a, b] = inputData;

if (a > b) {
  console.log(">");
} else if (a < b) {
  console.log("<");
} else {
  console.log("==");
}
