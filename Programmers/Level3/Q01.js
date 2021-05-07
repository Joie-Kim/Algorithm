// [2020 카카오 인턴십] 보석 쇼핑

function solution(gems) {
  let answer = [];
  const gemsSize = gems.length;
  const gemsTypeSize = new Set(gems).size;
  let gemsMap = new Map();
  gemsMap.set(gems[0], 1);

  let left = 0;
  let right = 0;
  while (left < gemsSize && right < gemsSize) {
    if (gemsMap.size < gemsTypeSize) {
      right++;
      gemsMap.set(gems[right], (gemsMap.get(gems[right]) || 0) + 1);
    } else {
      answer.push([left + 1, right + 1]);
      gemsMap.set(gems[left], gemsMap.get(gems[left]) - 1);
      if (gemsMap.get(gems[left]) === 0) gemsMap.delete(gems[left]);
      left++;
    }
  }

  answer.sort((a, b) => {
    if (a[1] - a[0] === b[1] - b[0]) {
      return a[0] - b[0];
    } else {
      return a[1] - a[0] - (b[1] - b[0]);
    }
  });

  return answer[0];
}

console.log(
  solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
);
console.log(solution(["AA", "AB", "AC", "AA", "AC"]));
console.log(solution(["XYZ", "XYZ", "XYZ"]));
console.log(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]));
