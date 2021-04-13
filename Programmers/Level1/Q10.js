// Q10. 문자열 내 마음대로 정렬하기

function solution(strings, n) {
  let answer = [];

  let mapped = strings.map((s, i) => {
    return { index: i, value: s[n] };
  });

  mapped.sort((a, b) => {
    if (a.value > b.value) {
      return 1;
    }
    if (a.value < b.value) {
      return -1;
    }
    if (a.value === b.value) {
      return strings[a.index] < strings[b.index]
        ? -1
        : strings[a.index] > strings[b.index]
        ? 1
        : 0;
    }
  });

  answer = mapped.map((s) => {
    return strings[s.index];
  });

  return answer;
}

console.log(solution(["sun", "bed", "car"], 1));
console.log(solution(["abce", "abcd", "cdx"], 2));
