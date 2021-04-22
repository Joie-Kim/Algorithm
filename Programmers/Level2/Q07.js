// Q07. 올바른 괄호

function solution(s) {
  let stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(s[i]);
    } else {
      const top = stack.pop();
      if (top !== "(") return false;
    }
  }

  return stack.length ? false : true;
}

console.log(solution("()()"));
console.log(solution("(())()"));
console.log(solution(")()("));
console.log(solution("(()("));
