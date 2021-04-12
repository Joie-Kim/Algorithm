// 시간 초과

function solution(number, k) {
  let answer = "";
  let numArr = number.split(""); // number 문자열을 배열로 변환
  let idx = 0; // numArr을 탐색할 인덱스
  let maxNums = []; // 범위 내에서 큰 수를 담을 배열
  let newLen = number.length - k; // k개의 숫자를 제외한 새로운 숫자의 길이

  while (true) {
    // k개의 수를 모두 제거 했으면
    if (maxNums.length === newLen) {
      // 문자열로 만들어서 리턴
      answer = maxNums.join("");
      return answer;
    }

    let sliceNum = numArr.slice(idx, k + 1); // 범위만큼 자른 배열
    let maxNum = ""; // 범위 내에서 큰 수

    if (sliceNum.includes("9")) {
      // 만약 숫자 '9'가 있으면
      // 그게 최대 수이기 때문에 max 연산 하지 않음
      maxNum = "9";
    } else {
      // spread operator 이용해서 배열 내 최대 수 구하기
      // 숫자형을 반환하기 때문에 문자형으로 바꿔줌
      maxNum = String(Math.max(...sliceNum));
    }

    // 큰 수를 배열에 넣음
    maxNums.push(maxNum);

    // 기존 인덱스에 slice 배열의 인덱스를 더함 (기존 배열에 중복되는 수가 있을 경우, 가장 처음 등장하는 요소의 인덱스를 반환하기 때문에)
    // +1 해서 다음 인덱스로 이동
    idx += sliceNum.indexOf(maxNum) + 1;

    // k를 늘려서 비교 범위 이동
    k++;
  }
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
