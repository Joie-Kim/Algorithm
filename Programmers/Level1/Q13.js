// Q13. 문자열 내림차순으로 배치하기

function solution(s) {
  let answer = "";

  answer = s
    .split("")
    .sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    .join("");
  return answer;
}

console.log(solution("Zbcdefg"));
