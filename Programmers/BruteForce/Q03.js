function solution(brown, yellow) {
  let answer = [];
  let tDiv = []; // brown + yellow의 약수
  let yDiv = []; // yellow의 약수

  // 약수 구하는 함수
  const getDiv = (num, dList) => {
    let i = 1;
    while (i * i <= num) {
      if (num % i === 0) {
        dList.push([num / i, i]);
      }
      i += 1;
    }
  };

  // 약수 구하기
  getDiv(brown + yellow, tDiv);
  getDiv(yellow, yDiv);

  for (let i = 0; i < yDiv.length; i++) {
    for (let j = 0; j < tDiv.length; j++) {
      if (yDiv[i][0] + 2 <= tDiv[j][0] && yDiv[i][1] + 2 <= tDiv[j][1]) {
        answer.push(tDiv[j][0]);
        answer.push(tDiv[j][1]);
        return answer;
      }
    }
  }
}

console.log(solution(10, 2));
console.log(solution(8, 1));
console.log(solution(24, 24));
