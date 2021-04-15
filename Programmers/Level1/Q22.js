// Q22. 이상한 문자 만들기

function solution(s) {
  // 공백을 기준으로 단어로 분리
  let sArr = s.split(" ");

  // 인덱스가 짝수(0포함): 대문자로, 홀수: 소문자로
  for (let i = 0; i < sArr.length; i++) {
    let wArr = sArr[i].split("");

    for (let j = 0; j < wArr.length; j++) {
      if (j % 2 === 0) {
        wArr[j] = wArr[j].toUpperCase();
      } else {
        wArr[j] = wArr[j].toLowerCase();
      }
    }
    sArr[i] = wArr.join("");
  }

  return sArr.join(" ");
}

console.log(solution("try hello world"));
console.log(solution("TRY HELLO WORLD"));
console.log(solution("try   hello world"));
