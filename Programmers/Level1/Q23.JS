// Q23. 자릿수 더하기

/*
function solution(n) {
  let len = String(n).length;
  let answer = 0;

  let quot = 0;
  let curN = n;
  for (let i = len - 1; i >= 0; i--) {
    curN -= quot * 10 ** (i + 1);
    quot = Math.floor(curN / 10 ** i);
    answer += quot;
  }
  return answer;
}
*/

// 좀 더 쉽게 숫자로 풀기
/*
function solution(n) {
  let answer = 0;

  while (n > 0) {
    answer += n % 10;
    n = Math.floor(n / 10);
  }
  return answer;
}
*/

// 문자열로 풀기
function solution(n) {
  let answer = 0;
  let nArr = [...(n + "")]; // 이렇게 숫자를 문자로 바꿀 수 있다.

  answer = nArr.reduce((acc, cur) => acc + parseInt(cur), 0); // 문자를 숫자로 바꿔서 더한다.
  return answer;
}

console.log(solution(123));
console.log(solution(987));
