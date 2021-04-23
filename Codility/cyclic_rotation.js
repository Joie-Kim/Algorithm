function solution(A, K) {
  let result = [];

  A.forEach((a, i) => (result[(i + K) % A.length] = a));

  return result;
}
