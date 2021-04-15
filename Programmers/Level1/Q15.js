// Q15. 서울에서 김서방 찾기

function solution(seoul) {
  const idx = seoul.indexOf("Kim");
  return `김서방은 ${idx}에 있다`;
}

console.log(solution(["Jane", "Kim"]));
