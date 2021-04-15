// Q11.폰켓몬

function solution(nums) {
  let getSize = nums.length / 2;

  // set에 담아서 중복된 걸 없앤다.
  // 만약 nums.length/2 보다 큰 경우에는 nums.length/2가 최댓값

  let numSet = new Set(nums);

  return numSet.size > getSize ? getSize : numSet.size;
}

console.log(solution([3, 1, 2, 3]));
console.log(solution([3, 3, 3, 2, 2, 4]));
console.log(solution([3, 3, 3, 2, 2, 2]));
