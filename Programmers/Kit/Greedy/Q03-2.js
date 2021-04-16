// 스택으로 그리디 구현

function solution(number, k) {
  let answer = "";
  let numArr = number.split(""); // number을 배열로 만듦
  let stack = [];
  let cnt = 0; // 제거된 숫자의 갯수

  // numArr을 순회
  for (let i = 0; i < numArr.length; i++) {
    // 스택에 숫자를 넣음
    stack.push(numArr[i]);

    // push된 숫자를 가리키는 인덱스
    let idx = stack.length - 1;

    // 인덱스가 0보다 크고,
    // 이전에 추가된 숫자가 지금 추가된 숫자보다 작을 경우
    while (idx > 0 && stack[idx - 1] < stack[idx]) {
      // 숫자를 교환하고
      let tmp = stack[idx];
      stack[idx] = stack[idx - 1];
      stack[idx - 1] = tmp;

      stack.pop(); // 스택에서 제거

      idx -= 1; // 인덱스 위치 변경
      cnt++; // 제거된 숫자의 갯수 증가

      // 만약 제거된 숫자의 갯수가 k와 일치하면
      if (cnt === k) {
        // 스택에 있는 숫자와 남은 숫자들을 합쳐서 리턴
        answer = stack.join("") + numArr.slice(i + 1).join("");
        return answer;
      }
    }
  }

  // numArr 순회를 모두 마쳤는데, 아직 k개의 숫자를 제거하지 못 한 경우
  if (cnt < k) {
    // 스택의 모든 숫자가 n[i-1] >= n[i]인 상황
    answer = stack.slice(0, stack.length - (k - cnt)).join("");
  }

  return answer;
}

console.log(solution("1924", 2));
console.log(solution("1231234", 3));
console.log(solution("4177252841", 4));
console.log(solution("99991", 3));
