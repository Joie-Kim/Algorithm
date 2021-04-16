// Q39. 실패율

function solution(n, stages) {
  let answer = [];
  let fail = Array.from({ length: n }, () => 0); // 실패율을 담을 배열

  // 현재 도전 중인 스테이지의 수
  let cntStages = stages.reduce((allStg, stg) => {
    if (stg in allStg) {
      allStg[stg]++;
    } else {
      allStg[stg] = 1;
    }
    return allStg;
  }, {});

  // 실패율 계산
  let acc = 0; // 누적 통과 인원수
  for (let i = 1; i <= n; i++) {
    // 현재 도전 중인 스테이지이면
    if (i in cntStages) {
      fail[i - 1] = cntStages[i] / (stages.length - acc);
      acc += cntStages[i];
    }
  }

  // 인덱스를 유지하면서 정렬해야 하기 때문에
  // 인덱스와 값을 가진 객체를 만들었음
  let failMap = fail.map((f, i) => ({
    index: i + 1,
    value: f,
  }));
  // 객체 값을 기준으로 내림차순 정렬
  failMap.sort((a, b) => b.value - a.value);
  // 정렬된 배열의 인덱스 값을 answer에 push
  failMap.forEach((f) => {
    answer.push(f.index);
  });

  return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(4, [4, 4, 4, 4, 4]));
