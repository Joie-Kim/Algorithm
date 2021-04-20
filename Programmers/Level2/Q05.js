// Q05. 순위 검색

// 시간 초과를 개선했음
function solution(info, query) {
  let infoDict = {};
  let answer = [];

  // 경우의 수를 key로 하는 Dict를 만드는 함수
  const setInfoDict = (arr, score, start) => {
    const key = arr.join("");
    const value = infoDict[key];

    if (value) {
      infoDict[key].push(score);
    } else {
      infoDict[key] = [score];
    }

    for (let i = start; i < arr.length; i++) {
      const tmp = [...arr];
      tmp[i] = "-";
      setInfoDict(tmp, score, i + 1);
    }
  };

  for (let i = 0; i < info.length; i++) {
    const option = info[i].split(" ");
    const score = Number(option.pop());
    setInfoDict(option, score, 0);
  }

  // infoDict[key]에 값을 넣을 때마다 정렬을 했었는데, 한 번에 정렬하도록 개선
  for (const key in infoDict) {
    infoDict[key].sort((a, b) => a - b);
  }

  for (let i = 0; i < query.length; i++) {
    const option = query[i].replace(/ and /g, " ").split(" ");
    const score = option.pop();
    const key = option.join("");
    const arr = infoDict[key]; // 이전에는 arr 선언 없이 사용 했는데, 계속 찾는 게 효율적이지 않을 거 같아 개선

    if (arr) {
      let start = 0;
      let end = arr.length - 1;
      while (start < end) {
        const mid = Math.floor((start + end) / 2);
        if (arr[mid] >= score) {
          end = mid;
        } else {
          start = mid + 1;
        }
      }
      const result = arr.length - end;
      answer.push(result);
    } else {
      answer.push(0);
    }
  }
  return answer;
}

console.log(
  solution(
    [
      "java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260",
      "java backend junior chicken 80",
      "python backend senior chicken 50",
    ],
    [
      "java and backend and junior and pizza 100",
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150",
      "- and - and - and chicken 100",
      "- and - and - and - 150",
    ]
  )
);
