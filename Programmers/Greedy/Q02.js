function solution(name) {
  let answer = 0;
  let len = name.length;
  let cntChange = Array.from({ length: len }, () => 0); // 문자 변경 횟수를 담은 배열

  // 문자 변경 횟수 넣기 (조이스틱 위, 아래 움직이는 횟수)
  for (let i = 0; i < len; i++) {
    cntChange[i] = Math.min(
      name.charCodeAt(i) - "A".charCodeAt(0),
      "Z".charCodeAt(0) - name.charCodeAt(i) + 1
    );
  }

  // 조이스틱이 움직이는 횟수 세기
  let idx = 0;
  while (true) {
    answer += cntChange[idx]; // 조이스틱이 위, 아래로 움직인 횟수 더하기
    cntChange[idx] = 0; // 사용한 값은 0으로 변경
    if (cntChange.reduce((sum, cur) => sum + cur) === 0) return answer; // 모든 문자 탐색 완료

    let left = idx; // 왼쪽으로 이동했을 때, 인덱스 위치
    let lCnt = 0; // 왼쪽으로 이동한 횟수
    let right = idx; // 오른쪽으로 이동했을 때, 인덱스 위치
    let rCnt = 0; // 오른쪽으로 이동한 횟수

    // 0이 아닌 수('A'가 아닌 아직 변경 전의 문자)를 찾을 때까지 반복
    while (cntChange[left] === 0) {
      // 왼쪽으로 이동
      if (left === 0) left = len;
      left--;
      lCnt++;
    }
    while (cntChange[right] === 0) {
      // 오른쪽으로 이동
      right++;
      rCnt++;
      if (right === len) right = 0;
    }

    // 이동 횟수를 비교해서 더 적은 수를 answer에 더함
    lCnt < rCnt ? (answer += lCnt) : (answer += rCnt);
    // 이동 횟수를 비교해서 인덱스 위치 변경
    lCnt < rCnt ? (idx = left) : (idx = right);
  }
}

console.log(solution("JEROEN"));
console.log(solution("JAN"));
