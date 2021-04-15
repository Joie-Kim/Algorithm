// Q29. [카카오 인턴] 키패드 누르기

function solution(numbers, hand) {
  // 키패드 배열
  const phone = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 0, "#"],
  ];
  // 왼손 처음 시작: *
  let lPosition = {
    x: 0,
    y: 3,
  };
  // 오른손 처음 시작: #
  let rPosition = {
    x: 2,
    y: 3,
  };
  let answer = "";

  // numbers 순회하며 탐색
  numbers.forEach((n) => {
    // 눌러야 하는 숫자의 위치를 나타낼 변수
    let nPosition = {
      x: 0, // 열 번호
      y: 0, // 행 번호
    };

    // phone 배열(키패트)을 순회하면서 x와 y좌표를 구함
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 3; j++) {
        if (phone[i][j] === n) {
          nPosition.x = j;
          nPosition.y = i;
        }
      }
    }

    // x 좌표가 0일 경우: 왼손으로 누름
    // x 좌표가 2일 경우: 오른손으로 누름
    // x 좌표가 1일 경우에는 판단을 해야 함
    if (nPosition.x === 0) {
      lPosition = nPosition;
      answer += "L";
    } else if (nPosition.x === 2) {
      rPosition = nPosition;
      answer += "R";
    } else {
      // 현재 손의 위치와 눌러야 하는 숫자의 위치를 빼서 거리를 계산 (x좌표, y좌표로 계산)
      let lDist =
        Math.abs(lPosition.x - nPosition.x) +
        Math.abs(lPosition.y - nPosition.y);
      console.log("lDist: " + lDist);
      let rDist =
        Math.abs(rPosition.x - nPosition.x) +
        Math.abs(rPosition.y - nPosition.y);
      console.log("rDist: " + rDist);

      // 거리가 가까운 것을 선택하고
      // 거리가 같을 겅우에는 손에 따라 선택
      if (lDist < rDist) {
        lPosition = nPosition;
        answer += "L";
      } else if (lDist > rDist) {
        rPosition = nPosition;
        answer += "R";
      } else {
        if (hand === "left") {
          lPosition = nPosition;
          answer += "L";
        } else {
          rPosition = nPosition;
          answer += "R";
        }
      }
    }
  });

  return answer;
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"));
console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));
console.log(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"));
