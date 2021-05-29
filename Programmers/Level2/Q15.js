// Q15. 최솟값 만들기

function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  const answer = A.reduce((acc, cur, i) => acc + cur * B[i], 0);

  return answer;
}
