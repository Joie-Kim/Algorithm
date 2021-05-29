// Q18. 땅따먹기

function solution(land) {
  var answer = 0;
  var len = land.length;

  for (var i = len - 2; i >= 0; i--) {
    land[i][0] =
      Math.max(land[i + 1][1], land[i + 1][2], land[i + 1][3]) + land[i][0];
    land[i][1] =
      Math.max(land[i + 1][0], land[i + 1][2], land[i + 1][3]) + land[i][1];
    land[i][2] =
      Math.max(land[i + 1][0], land[i + 1][1], land[i + 1][3]) + land[i][2];
    land[i][3] =
      Math.max(land[i + 1][0], land[i + 1][1], land[i + 1][2]) + land[i][3];
  }

  answer = Math.max(...land[0]);
  return answer;
}

// 동적 프로그래밍 이용
// (i, 0)에서 출발해 얻을 수 있는 최댓값은 max((i+1, 1), (i+1, 2), (i+1, 3)) + (i, 0)의 값
// land에 최댓값을 저장해둔다.
