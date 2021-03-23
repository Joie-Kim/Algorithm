/*
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
*/

const fs = require("fs");
const inputData = fs.readFileSync("/dev/stdin").toString().split(" ");

const [a, b] = inputData;
// 연산 할 때, Number 변환을 꼭 해줘야 함! + 연산은 문자열을 더하는 것도 되기 때문에
console.log(Number(a) + Number(b));

/*
const fs = require('fs')
// map을 이용해서 정수로 만들기
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value)

const [a, b] = inputData
// Number 함수를 사용하지 않아도 됨
console.log(a+b)
*/
