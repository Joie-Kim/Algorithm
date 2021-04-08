function solution(n, lost, reserve) {
  let student = Array.from({ length: n }, () => 1);

  lost.forEach((lStuendt) => {
    student[lStuendt - 1] -= 1;
  });
  reserve.forEach((rStudent) => {
    student[rStudent - 1] += 1;
  });

  for (let i = 0; i < n; i++) {
    if (student[i] === 0) {
      if (student[i + 1] === 2) {
        student[i] += 1;
        student[i + 1] -= 1;
      } else if (student[i - 1] === 2) {
        student[i] += 1;
        student[i - 1] -= 1;
      }
    }
  }

  student = student.filter((s) => s !== 0);

  return student.length;
}

console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));
console.log(solution(3, [3], [1]));
