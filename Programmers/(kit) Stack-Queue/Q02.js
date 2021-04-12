function solution(progresses, speeds) {
  let answer = [];

  progresses.forEach((p, i) => {
    const s = speeds[i];
    const workDay = Math.ceil((100 - p) / s);
    if (answer.length === 0 || answer[0][0] < workDay) {
      answer.unshift([workDay, 1]);
    } else {
      answer[0][1] += 1;
      console.log("else");
    }
  });

  return answer.map((a) => a[1]).reverse();
}

console.log(solution([93, 30, 55, 50], [1, 30, 5, 40]));
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]));
console.log(solution([2, 2, 1, 2], [1, 1, 1, 1]));
console.log(solution([99, 99, 99], [1, 1, 1]));
console.log(solution([0, 0, 0], [1, 1, 1]));
console.log(solution([0, 0, 0, 0], [100, 50, 34, 25]));
console.log(solution([5, 5, 5], [21, 25, 20]));
