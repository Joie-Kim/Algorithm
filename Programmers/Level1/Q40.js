// Q40. [1차] 다트 게임

function solution(s) {
  let answer = 0;

  // 숫자 최소 1개, 최대 2개인 문자열을 기준으로 split
  // 괄호 안에 정규식을 넣었기 때문에 split한 기준도 배열에 포함됨
  let sArr = s.split(/(\d{1,2})/g);

  // 3번의 도전에서 각각 얻은 점수
  let score = { 0: 0, 1: 0, 2: 0, 3: 0 };

  // sArr을 순회하며 점수 확인
  let tryNum = 0; // 도전 횟수 (총 3회)
  for (let i = 1; i < sArr.length; i++) {
    // i가 짝수 : 옵션 문자열
    if (i % 2 === 0) {
      let num = sArr[i - 1];

      // S, D, T 비교
      switch (sArr[i][0]) {
        case "S":
          score[tryNum] += num ** 1;
          break;
        case "D":
          score[tryNum] += num ** 2;
          break;
        case "T":
          score[tryNum] += num ** 3;
          break;
        default:
      }

      // *, #이 있다면
      if (sArr[i][1]) {
        if (sArr[i][1] === "*") {
          // 현재 점수와 이전 점수를 2배
          score[tryNum] *= 2;
          score[tryNum - 1] *= 2;
        } else {
          // 현재 점수를 마이너스로
          score[tryNum] *= -1;
        }
      }
    } else {
      // i가 홀수 : 숫자 부분
      // 도전 횟수를 +1 함
      tryNum++;
    }
  }

  // 모든 도전에서 얻은 점수를 더함
  answer = score[1] + score[2] + score[3];
  return answer;
}

console.log(solution("1S2D*3T"));
console.log(solution("1D2S#10S"));
console.log(solution("1D2S0T"));
console.log(solution("1S*2T*3S"));
console.log(solution("1D#2S*3S"));
console.log(solution("1T2D3D#"));
console.log(solution("1D2S3T*"));
