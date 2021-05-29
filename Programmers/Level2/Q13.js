// Q13. 행렬의 곱셈

function solution(arr1, arr2) {
  var answer = [];

  arr1.forEach((a) => {
    let results = [];

    for (let i = 0; i < arr2[0].length; i++) {
      let result = 0;
      a.forEach((v, j) => {
        result += v * arr2[j][i];
      });
      results.push(result);
    }

    answer.push(results);
  });

  return answer;
}
