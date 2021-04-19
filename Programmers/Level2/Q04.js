// Q04. 괄호 변환
/*
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
*/

function solution(p) {
  let answer = "";

  const reversePrt = (u) => {
    let result = "";
    let tmp = u.slice(1, u.length - 1);
    if (tmp === "") return result;

    for (let i = 0; i < tmp.length; i++) {
      if (tmp[i] === "(") {
        result += ")";
      } else {
        result += "(";
      }
    }

    return result;
  };

  const getParenthesis = (s) => {
    let result = "";
    if (s === "") return result;

    let u = "";
    let v = "";
    let left = 0;
    let right = 0;
    let stack = [];
    let check = false;

    let ptr = 0;
    while (ptr < s.length) {
      if (s[ptr] === ")") {
        let top = stack.pop();
        if (!top) {
          check = false;
        }
        right++;
      } else {
        stack.push("(");
        left++;
      }

      ptr++;

      if (left === right) {
        u = s.slice(0, ptr);
        v = s.slice(ptr);
        break;
      }
    }
    if (stack.length === 0) check = true;

    if (check) {
      result = u + getParenthesis(v);
    } else {
      result = "(" + getParenthesis(v) + ")" + reversePrt(u);
    }

    return result;
  };

  answer = getParenthesis(p);

  return answer;
}

console.log(solution("(()())()"));
console.log(solution(")("));
console.log(solution("()))((()"));