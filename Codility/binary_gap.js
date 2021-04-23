function solution(N) {
  const stringN = String(N.toString(2)); // N을 이진법으로 바꾼 뒤에 문자열로 변환
  if (stringN.length <= 2) return 0; // 문자열의 길이가 2 이하면 binary gap이 생길 수 없음
  if (!stringN.includes("0")) return 0; // 문자열에 0이 없을 경우 binary gap이 생길 수 없음

  const zeroArr = stringN.split(/(?:1)/g); // 1을 기준으로 문자열을 자름

  // split 결과 배열에 들어가는 빈문자열 제거
  for (let i = 0; i < zeroArr.length; i++) {
    if (zeroArr[i] === "") {
      zeroArr.splice(i, 1);
    }
  }

  // 문자열의 마지막 문자가 1이 아닐 경우, 해당 원소는 binary gap이 될 수 없음
  if (stringN[stringN.length - 1] !== "1") {
    zeroArr.pop(); // 마지막 원소 제거
  }
  // 배열이 비었을 경우, binary gap 후보가 없다는 뜻
  if (zeroArr.length === 0) return 0;

  // 길이를 기준으로 정렬 (내림차순)
  zeroArr.sort((a, b) => b.length - a.length);

  // 가장 긴 길이를 반환함
  return zeroArr[0].length;
}
