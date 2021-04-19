// Q03. 메뉴 리뉴얼

// 예시 코드는 모두 통과
// 하지만 실행했을 때 3개의 테스트코드에서 런타임 에러 발생
/*
function solution(orders, course) {
  let answer = [];

  // 조합을 구하는 함수
  const getCombination = (arr, r) => {
    let n = arr.length;
    let results = [];

    if (r === 1) return arr.map((value) => [value]);

    for (let i = 0; i < n; i++) {
      let fixed = arr[i];
      let rest = arr.slice(i + 1);
      let combinations = getCombination(rest, r - 1);
      let attached = combinations.map((comb) => [fixed, ...comb]);
      results.push(...attached);
    }

    return results;
  };

  // course를 순회하며 탐색
  for (let i = 0; i < course.length; i++) {
    let num = course[i]; // 코스 요리 숫자

    // 코스 요리 숫자 이상의 주문만 배열에 넣음
    let arr = [];
    orders.forEach((s) => {
      if (s.length >= num) {
        arr.push(s.split(""));
      }
    });
    // 만약 배열의 길이(주문의 수)가 2보다 작으면 순회 종료
    if (arr.length < 2) break;

    // 주문에 있는 메뉴들을 중복 없이 집합에 넣음
    let menuSet = new Set();

    arr.forEach((order) => {
      for (let i = 0; i < order.length; i++) {
        menuSet.add(order[i]);
      }
    });

    // 집합을 배열로 변경
    let menuArr = Array(...menuSet);

    // 해당 메뉴들의 조합을 구합
    let combArr = getCombination(menuArr, num);

    // 어떤 조합을 가지고 있는 주문의 수를 셈
    // combArr의 인덱스 == cntComb의 인덱스
    let cntComb = [];
    for (let i = 0; i < combArr.length; i++) {
      let cnt = 0;
      for (let k = 0; k < arr.length; k++) {
        let flag = 0;
        for (let j = 0; j < num; j++) {
          if (arr[k].includes(combArr[i][j])) {
            flag++;
          }
        }
        if (flag === num) cnt++;
      }

      cntComb.push(cnt);
    }

    // 인덱스를 알기 위해 Map
    let combMap = cntComb.map((v, i) => ({
      index: i,
      value: v,
    }));

    // 내림차순으로 정렬하고, 첫 번째 값을 최댓값으로 지정
    combMap.sort((a, b) => b.value - a.value);
    let maxValue = combMap[0].value;

    // 그 수가 2 이상일 때만 추가
    if (maxValue >= 2) {
      // combMap을 순회하면서 탐색
      combMap.forEach((v) => {
        // 탐색한 것의 value가 최댓값일 경우
        if (v.value === maxValue) {
          let ans = combArr[v.index].sort().join("");
          answer.push(ans);
        }
      });
    }
  }

  return answer.sort();
}
*/

// 개선한 버전
// 테스트 통과, 시간 효율 개선
// 이전 코드의 문제는 각각 주문마다 조합을 구하고, 그 조합 배열과 주문 배열을 순회하면서 탐색했다는 것이다.
// 개선한 코드에서는 각각 주문마다 조합을 구할 때, 갯수를 셌다. 그럼 나중에 탐색을 할 필요가 없어진다.
function solution(orders, course) {
  let candidate = {}; // 코스 조합 후보

  // 조합 구하는 함수
  const getCombination = (arr, r, num) => {
    let result = [];
    let n = arr.length;

    if (r === 1) return arr;

    for (let i = 0; i < n; i++) {
      let fixed = arr[i];
      let rest = arr.slice(i + 1);
      let combinations = getCombination(rest, r - 1);
      let attached = combinations.map((comb) => fixed + comb); // 조합을 문자열로
      result.push(...attached);
    }

    // r의 값이 num이랑 같을 때(즉, r-1이 되지 않은 처음)
    // 조합이 완성되기 때문에 그때 candidate 객체에 넣어준다.
    if (r === num) {
      result.forEach((e) => {
        if (e in candidate) {
          candidate[e]++;
        } else {
          candidate[e] = 1;
        }
      });
    }

    return result;
  };

  const answer = course.reduce((answer, num) => {
    // 코스 요리 숫자 이상의 주문만 조합을 구함
    for (let i = 0; i < orders.length; i++) {
      if (orders[i].length >= num) {
        getCombination(orders[i].split("").sort(), num, num);
      }
    }

    // 가장 많이 주문된 메뉴 조합을 탐색한다.
    let mostOrdered = 0;
    let menu = [];
    for (let key in candidate) {
      let value = candidate[key];
      if (value >= 2) {
        // 최소 주문이 2개 이상이어야 함
        if (value > mostOrdered) {
          // 더 큰 주문수를 발견하면
          mostOrdered = value; // 최대값을 변경하고
          menu = [key]; // 메뉴 배열을 초기화 함
        } else if (value === mostOrdered) {
          // 같은 주문수를 발견하면
          menu.push(key); // 메뉴 배열에 추가
        }
      }
    }

    candidate = {}; // num에 따라 확인 해야 하기 때문에 초기화
    return [...answer, ...menu];
  }, []);

  return answer.sort();
}

console.log(
  solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
);
console.log(
  solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
);
console.log(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]));
console.log(solution(["ABXYZ", "ACXYZ", "XWY", "WXA"], [4]));
