// Q06. 가운데 글자 가져오기

/*
function solution(s) {
  let answer = "";
  let len = s.length;

  if (len % 2 === 0) {
    answer = s.slice(len / 2 - 1, len / 2 + 1);
  } else {
    answer = s[Math.floor(len / 2)];
  }
  return answer;
}
*/

function solution(s) {
  let answer = "";
  let len = s.length;

  let div = Math.ceil(len / 2);

  answer = s.substring(div - 1, len % 2 === 0 ? div + 1 : div);

  return answer;
}

console.log(solution("abcde"));
console.log(solution("qwer"));
