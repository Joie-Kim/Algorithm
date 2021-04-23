function solution(A) {
  let aSet = new Set();

  for (let i = 0; i < A.length; i++) {
    if (aSet.has(A[i])) {
      aSet.delete(A[i]);
    } else {
      aSet.add(A[i]);
    }
  }

  return [...aSet][0];
}
