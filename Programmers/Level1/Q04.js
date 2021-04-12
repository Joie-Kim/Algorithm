// Q04. 2016년

/*
function solution(a, b) {
  let answer = "";
  const day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  const date30 = [4, 6, 9, 11];
  const date31 = [1, 3, 5, 7, 8, 10, 12];
  let sumDay = b - 1;

  for (let i = 1; i < a; i++) {
    if (date30.includes(i)) {
      sumDay += 30;
    } else if (date31.includes(i)) {
      sumDay += 31;
    } else {
      sumDay += 29;
    }
  }

  answer = day[sumDay % 7];

  return answer;
}
*/

function solution(a, b) {
  let answer = "";
  const day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"];
  const date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  let sumDay = b - 1;

  for (let i = 1; i < a; i++) {
    sumDay += date[i];
  }

  answer = day[sumDay % 7];

  return answer;
}

console.log(solution(5, 24));
console.log(solution(1, 2));
