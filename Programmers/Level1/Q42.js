// Q42. 음양 더하기

/*
function solution(absolutes, signs) {
  var answer = absolutes.reduce((acc, cur, i) => {
    if (signs[i] === false) cur *= -1;
    return acc + cur;
  }, 0);

  return answer;
}
*/

// 삼항 연산자 이용해서 좀 더 깔끔하게 정리
function solution(absolutes, signs) {
  var answer = absolutes.reduce(
    (acc, cur, i) => acc + cur * (signs[i] ? 1 : -1),
    0
  );

  return answer;
}
