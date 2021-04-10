function solution(routes) {
  let answer = 0;
  let len = routes.length;
  let check = Array.from({ length: len }, () => 0);
  let camera = 0;

  // 진입 시점을 기준으로 내림차순 정렬
  routes.sort((a, b) => b[0] - a[0]);

  // routes 순회
  routes.forEach((r, i) => {
    // check 배열이 0인 인덱스를 찾음
    if (check[i] === 0) {
      camera = r[0]; // camera 위치 지정
      check[i] = 1; // check 배열에 표시
      answer++; // camera 개수 더함
    }
    // 해당 camera 위치가 차량 이동 범위 내에 있는지 확인
    for (let j = i; j < len; j++) {
      if (check[j] === 0 && routes[j][0] <= camera && camera <= routes[j][1]) {
        check[j] = 1; // check 배열에 표시
      }
    }
  });
  return answer;
}

console.log(
  solution([
    [-20, 15],
    [-14, -5],
    [-18, -13],
    [-5, -3],
  ])
);
