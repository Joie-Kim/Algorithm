// Q35. 행렬의 덧셈

function solution(arr1, arr2) {
  let answer = [];

  for (let i = 0; i < arr1.length; i++) {
    //let subAnswer = [];
    answer[i] = [];
    for (let j = 0; j < arr1[i].length; j++) {
      //subAnswer.push(arr1[i][j] + arr2[i][j]);
      answer[i].push(arr1[i][j] + arr2[i][j]);
    }
    //answer.push(subAnswer);
  }
  return answer;
}

console.log(
  solution(
    [
      [1, 2],
      [2, 3],
    ],
    [
      [3, 4],
      [5, 6],
    ]
  )
);
console.log(solution([[1], [2]], [[3], [4]]));
