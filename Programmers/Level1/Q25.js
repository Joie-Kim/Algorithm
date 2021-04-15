// Q25. 정수 내림차순으로 배치하기

function solution(n) {
  let answer = 0;
  let nArr = [...(n + "")];

  nArr.sort((a, b) => b - a);
  answer = parsInt(nArr.join(""));

  return answer;
}

// 배열을 숫자로 구성할 수도 있다.
/*
function solution(n) {
  let answer = 0;
  let nArr = [];

  // 숫자로 배열 만들기
  while (n > 0) {
    nArr.push(n % 10);
    n = Math.floor(n / 10);
  }

  // 내림차순 정렬
  nArr.sort((a, b) => b - a);
  answer = parsInt(nArr.join(""));

  return answer;
}
*/

console.log(solution(118372));
