// Q34. 핸드폰 번호 가리기

function solution(s) {
  let last4Digits = s.slice(-4);
  let answer = last4Digits.padStart(s.length, "*");
  return answer;
}

// 정규식 사용하기
/*
function solution(s) {
  // \d: 숫자
  // x(?=y): 뒤에 y가 오는 x에만 대응
  let answer = s.replace(/\d(?=\d{4})/gi, "*");
  return answer;
}
*/
console.log(solution("01033334444"));
console.log(solution("027778888"));
