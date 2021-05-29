// Q16. 최댓값과 최솟값

function solution(s) {
  const arr = s.split(" ");
  const maxN = Math.max(...arr);
  const minN = Math.min(...arr);

  return minN + " " + maxN;
}
