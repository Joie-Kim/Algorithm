// Q03. 신규 아이디 추천

/*
function solution(new_id) {
  let answer = "";

  // 1단계: 소문자로 치환
  new_id = new_id.toLowerCase();
  console.log(new_id);

  // 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
  let reg = /[^\w-_.]/g;
  new_id = new_id.replace(reg, "");
  console.log(new_id);

  // 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
  reg = /[.]{2,}/g;
  new_id = new_id.replace(reg, ".");
  console.log(new_id);

  // 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
  reg = /^\.|\.$/g;
  new_id = new_id.replace(reg, "");
  console.log(new_id);

  // 5단계: 빈 문자열이라면, new_id에 "a"를 대입
  reg = /^$/g;
  new_id = new_id.replace(reg, "a");
  console.log(new_id);

  // 6단계: 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
  // 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
  new_id = new_id.slice(0, 15);
  reg = /\.$/g;
  new_id = new_id.replace(reg, "");
  console.log(new_id);

  // 7단계: 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
  answer = new_id;
  if (new_id.length <= 2) {
    answer += new_id[new_id.length - 1].repeat(3 - new_id.length);
  }

  return answer;
}
*/

function solution(new_id) {
  let answer = "";

  answer = new_id
    .toLowerCase() // 1
    .replace(/[^\w-_.]/g, "") // 2
    .replace(/[.]{2,}/g, ".") // 3
    .replace(/^\.|\.$/g, "") // 4
    .replace(/^$/g, "a") // 5
    .slice(0, 15)
    .replace(/\.$/g, ""); // 6

  // 7단계: 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
  const len = answer.length;
  //return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
  return answer.padEnd(3, answer[len - 1]);
}

console.log(solution("...!@BaT#*..y.abcdefghijklm"));
console.log(solution("z-+.^."));
console.log(solution("=.="));
console.log(solution("123_.def"));
console.log(solution("abcdefghijklmn.p"));
