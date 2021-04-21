function solution(N, number) {
  if (N === number) return 1;
  let calc = Array.from({ length: 8 }, () => new Set());

  // i+1개의 숫자를 사용한 경우를 탐색
  for (let i = 0; i < 8; i++) {
    calc[i].add(Number(String(N).repeat(i + 1)));
    if (i === 0) continue; // 숫자 한 개 사용한 경우 끝

    for (let j = 0; j < i; j++) {
      for (const n1 of calc[j]) {
        for (const n2 of calc[i - (j + 1)]) {
          calc[i].add(n1 + n2);
          calc[i].add(n1 - n2);
          calc[i].add(n1 * n2);
          calc[i].add(Math.floor(n1 / n2)); // js에서는 n2가 0일 경우 infinity 처리
        }
      }
    }

    if (calc[i].has(number)) return i + 1;
  }

  return -1;
}

console.log(solution(5, 12));
console.log(solution(2, 11));
