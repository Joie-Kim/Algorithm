function solution(answers) {
  // 찍은 값
  const persons = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  // 점수 모아두는 배열
  let scores = [];
  // 최고 점수
  let maxScore = 0;
  let answer = [];

  // 점수를 확인하는 함수
  const checkAnswer = (answer, mine) => {
    let score = 0;

    answer.forEach((a, i) => {
      const n = i % mine.length;
      if (a === mine[n]) {
        score += 1;
      }
    });

    return score;
  };

  // 체점하기
  persons.forEach((p) => {
    scores.push(checkAnswer(answers, p));
  });

  // 최고점수 구하기
  scores.forEach((s) => {
    if (maxScore < s) {
      maxScore = s;
    }
  });

  // 최고 점수와 같은 사람 찾기
  scores.forEach((s, i) => {
    if (s === maxScore) {
      answer.push(i + 1);
    }
  });

  return answer;
}

console.log(solution([1, 2, 3, 4, 5]));
console.log(solution([1, 3, 2, 4, 2]));
console.log(solution([3, 3, 1, 1, 1, 1, 2, 3, 4, 5]));
