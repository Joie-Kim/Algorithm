// Q19. 시저 암호

function solution(s, n) {
  let answer = "";

  // A-Z : 65 ~ 90
  // a-z : 97 ~ 122
  // 공백 : 32
  for (let i = 0; i < s.length; i++) {
    let unicode = s.charCodeAt(i);

    if (unicode === 32) {
      // 공백 확인
      answer += " ";
    } else if (65 <= unicode && unicode <= 90) {
      // 대문자 확인
      if (n > 90 - unicode) {
        // 이동할 수 있는 길이가 n보다 짧으면
        // 끝까지 이동하고 남은 길이만큼 더해준다.
        answer += String.fromCharCode(64 + (n - (90 - unicode)));
      } else {
        answer += String.fromCharCode(unicode + n);
      }
    } else if (97 <= unicode <= 122) {
      // 소문자 확인
      if (n > 122 - unicode) {
        // 이동할 수 있는 길이가 n보다 짧으면
        // 끝까지 이동하고 남은 길이만큼 더해준다.
        answer += String.fromCharCode(96 + (n - (122 - unicode)));
      } else {
        answer += String.fromCharCode(unicode + n);
      }
    }
  }
  return answer;
}

console.log(solution("AB", 25));
console.log(solution("a", 1));
console.log(solution("z", 1));
console.log(solution("Z", 1));
console.log(solution("a B z", 4));
