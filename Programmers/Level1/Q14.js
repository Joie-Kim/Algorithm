// Q14. 문자열 다루기 기본

/*
function solution(s) {
  const reg = /[^0-9]/g;
  if (reg.test(s)) {
    return false;
  } else if (s.length !== 4 && s.length !== 6) {
    return false;
  }

  return true;
}
*/

function solution(s) {
  // \d === [0-9]
  // ^: 처음, $: 끝
  const reg = /^\d{4}$|^\d{6}$/g;

  return reg.test(s);
}

console.log(solution("a234"));
console.log(solution("1234"));
