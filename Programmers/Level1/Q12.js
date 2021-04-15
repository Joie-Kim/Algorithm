// Q12. 문자열 내 p와 y의 개수

/*
function solution(s) {
  let pArr = [];
  let yArr = [];

  s = s.toLowerCase();

  let sArr = s.split("").sort((a, b) => a - b);

  pArr = sArr.filter((c) => c === "p");
  yArr = sArr.filter((c) => c === "y");

  if (pArr.length === yArr.length) {
    return true;
  } else {
    return false;
  }
}
*/

function solution(s) {
  return (
    s.toLowerCase().split("p").length === s.toLowerCase().split("y").length
  );
}

console.log(solution("pPoooyY"));
console.log(solution("pabPoooycdY"));
console.log(solution("Pyy"));
console.log(solution("ABc"));
