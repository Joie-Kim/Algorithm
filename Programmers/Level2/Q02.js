// Q02. 문자열 압축

function solution(s) {
  if (s.length === 1) return 1;
  let answer = [];

  for (let i = 1; i <= Math.floor(s.length / 2); i++) {
    let left = 0;
    let right = i;
    let compString = "";
    let cnt = 1;
    while (true) {
      if (s.substring(left, left + i) === s.substring(right, right + i)) {
        cnt++;
      } else {
        compString +=
          cnt === 1
            ? s.substring(left, left + i)
            : cnt + s.substring(left, left + i);
        cnt = 1;
        left = right;
      }
      right += i;

      if (right > s.length - 1) {
        compString +=
          cnt === 1
            ? s.substring(left, left + i)
            : cnt + s.substring(left, left + i);
        break;
      }
    }
    answer.push(compString.length);
  }
  return Math.min(...answer);
}

console.log(solution("aabbaccc"));
console.log(solution("ababcdcdababcdcd"));
console.log(solution("abcabcdede"));
console.log(solution("abcabcabcabcdededededede"));
console.log(solution("xababcdcdababcdcd"));
