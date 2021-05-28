// Q45. 에산

function solution(d, budget) {
  var answer = 0;

  d.sort((a, b) => a - b);
  d.forEach((e) => {
    if (e <= budget) {
      budget -= e;
      answer++;
    }
  });

  return answer;
}
