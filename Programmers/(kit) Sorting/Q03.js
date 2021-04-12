function solution(citations) {
  // 1. 논문 인용수가 높은 순으로 정렬
  citations.sort((a, b) => b - a);

  // 2. 논문 인용수가 논문수보다 적어질 때를 찾음
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] < i + 1) {
      return i;
    }
  }
  return citations.length;
}

console.log(solution([3, 0, 6, 1, 5])); //3
console.log(solution([12, 11, 10, 9, 8, 1])); //5
console.log(solution([6, 6, 6, 6, 6, 1])); //5
console.log(solution([4, 4, 4])); //3
console.log(solution([4, 4, 4, 5, 0, 1, 2, 3])); //4
console.log(solution([10, 11, 12, 13])); //4
console.log(solution([3, 0, 6, 1, 5])); //3
console.log(solution([0, 0, 1, 1])); //1
console.log(solution([0, 1])); //1
console.log(solution([10, 9, 4, 1, 1])); //3
