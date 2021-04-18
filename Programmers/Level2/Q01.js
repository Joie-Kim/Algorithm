// Q01. 124 나라의 숫자

// 시간 초과
// 정수 n이 최대 5억까지 될 수 있기 때문에 parseInt() 했을 때, 정수의 최댓값이 넘어갈 수 있겠다.
// parsInt() 부분을 수정해서 통과했음
/*
function solution(n) {
  const numList = [1, 2];
  let answer = " ";

  const getNum = (num, result) => {
    let quot = Math.floor(num / 3);
    let remain = num % 3;
    let subResult = result;

    // num이 0일 경우 재귀를 끝낸다.
    if (num === 0) return subResult;

    // 만약 num이 3의 배수이면, num-1을 변경한 수에 +2한다.
    if (num % 3 === 0) {
      let pre = getNum(num - 1, subResult);
      //subResult += parseInt(pre) + 2;
      subResult += pre.length === 1 ? "4" : pre.slice(0, pre.length - 1) + "4";
    } else {
      // 재귀함수로 문자열을 받아와서 현재 값에 더하고,
      subResult += getNum(quot, subResult);
      // 나머지에 해당하는 숫자를 더한다.
      switch (remain) {
        case 1:
          subResult += numList[0];
          break;
        case 2:
          subResult += numList[1];
          break;
        default:
          subResult += "";
      } // switch
    } // if-else

    return subResult;
  };

  return getNum(n, answer).trim();
}
*/

// 이 방법이 내가 푼 풀이보다 3배 빨랐다.
// 내가 푼 풀이 : 약 0.15ms 소요
// 해당 풀이 : 약 0.05ms 소요
function solution(n) {
  const numList = [4, 1, 2];
  let answer = "";

  while (n) {
    // 기존 문자열 앞에 새로운 문자열을 더한다.
    answer = numList[n % 3] + answer;
    // n이 3의 배수인 경우 n-1한 수로 계산을 해야 하기 때문에 아래처럼 해준다.
    // n이 3의 배수가 아닌 경우 n-1을 해도 몫이 같기 때문에 조건을 따로 두지 않아도 된다.
    n = Math.floor((n - 1) / 3);
  }

  return answer;
}

console.log(solution(1));
console.log(solution(2));
console.log(solution(3));
console.log(solution(513));
