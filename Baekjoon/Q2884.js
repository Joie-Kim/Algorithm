/*
설정한 알람 시각이 주어졌을 때, [45분 일찍 알람 설정하기]를 적용한다면 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
이것은 현재 설정한 알람 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력)
*/

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  const h = Number(input[0]);
  const m = Number(input[1]);

  let newH = 0;
  let newM = 0;

  if (m < 45) {
    newH = h === 0 ? 23 : h - 1;
    newM = m + 60 - 45;
  } else {
    newH = h;
    newM = m - 45;
  }

  console.log(`${newH} ${newM}`);
});
