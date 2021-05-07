// [2020 카카오 인턴십] 수식 최대화

function solution(expression) {
  let answers = new Set();

  // 숫자, 연산자 배열
  let nArray = expression.split(/[^\d]/g);
  for (let i = 0; i < nArray.length; i++) {
    nArray[i] = parseInt(nArray[i]);
  }
  let opArray = expression.split(/\d*/g);
  opArray = opArray.filter((e) => e !== "");

  // 연산자 우선 순위 구하기 (순열로)
  function getPermutaion(arr, r) {
    if (r === 1) return arr.map((value) => [value]);

    let result = [];

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
      const permutations = getPermutaion(rest, r - 1);
      const attached = permutations.map((perm) => [fixed, ...perm]);
      result.push(...attached);
    });
    return result;
  }

  // 연산자 중복 제외하고 우선순위 구함
  const opSet = new Set([...opArray]);
  const opPerm = getPermutaion([...opSet], opSet.size);

  // 우선순위에 따라 반복
  for (const ops of opPerm) {
    let copyNumber = [...nArray];
    let copyOp = [...opArray];
    for (let i = 0; i < ops.length; i++) {
      while (copyOp.includes(ops[i])) {
        const index = copyOp.indexOf(ops[i]);
        let result = 0;

        switch (ops[i]) {
          case "*":
            result = copyNumber[index] * copyNumber[index + 1];
            break;
          case "+":
            result = copyNumber[index] + copyNumber[index + 1];
            break;
          case "-":
            result = copyNumber[index] - copyNumber[index + 1];
            break;
          default:
            result = 0;
        }

        copyOp.splice(index, 1);
        copyNumber[index] = result;
        copyNumber.splice(index + 1, 1);
      }
    }
    answers.add(Math.abs(copyNumber[0]));
  }

  return Math.max(...answers);
}

console.log(solution("100-200*300-500+20"));
console.log(solution("50*6-3*2"));
