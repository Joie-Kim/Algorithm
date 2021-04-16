function solution(priorities, location) {
  let answer = 0;
  let queue = priorities.map((p, i) => {
    return [i, p];
  });

  while (queue.length != 0) {
    let J = queue.shift();

    if (queue.filter((q) => q[1] > J[1]).length > 0) {
      queue.push(J);
    } else {
      answer += 1;
      if (J[0] === location) {
        return answer;
      }
    }
  }
}

console.log(solution([2, 1, 3, 2], 2));
console.log(solution([1, 1, 9, 1, 1, 1], 0));
