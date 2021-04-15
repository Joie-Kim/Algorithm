// Q18. 문자열을 정수로 바꾸기

/*
function solution(s) {
  let isMinus = s.includes("-" ? true : false);

  return isMinus ? parseInt(s.slice[1]) : parseInt(s);
}
*/

// 자바스크립트는 동적 언어라서
// 문자를 숫자로 나누면서 자동으로 숫자로 파싱 됨..
function solution(s) {
  return s / 1;
}

console.log(solution("1234"));
console.log(solution("-1234"));
