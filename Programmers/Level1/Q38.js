// Q38. [1차] 비밀지도

function solution(n, arr1, arr2) {
  let answer = [];

  // 배열에 있는 숫자를 십진법에서 이진법으로 변경하는 함수
  // s.toString(2)를 사용하면 쉽게 이진법으로 변환 가능
  function getCode(arr) {
    let codeArr = [];

    arr.forEach((num) => {
      let code = [];
      while (num > 0) {
        code.unshift(num % 2);
        num = Math.floor(num / 2);
      }
      codeArr.push(code.join("").padStart(n, "0").split(""));
    });

    return codeArr;
  }

  // 지도 1, 2
  let map1 = getCode(arr1);
  let map2 = getCode(arr2);
  // let map1 = arr1.map((a) => a.toString(2).padStart(n, 0));
  // let map2 = arr2.map((a) => a.toString(2).padStart(n, 0));

  // 지도를 비교
  for (let i = 0; i < n; i++) {
    let subAnswer = Array.from({ length: n }, () => " ");
    for (let j = 0; j < n; j++) {
      if (map1[i][j] | map2[i][j]) {
        subAnswer[j] = "#";
      }
    }
    answer.push(subAnswer.join(""));
  }

  return answer;
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
console.log(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]));
