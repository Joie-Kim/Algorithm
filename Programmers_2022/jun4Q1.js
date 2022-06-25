// link: https://programmers.co.kr/learn/courses/30/lessons/92334

function solution(id_list, report, k) {
  const reportSet = new Set([...report]);
  let numOfReportMap = new Map();
  let reportMap = new Map();
  let blockList = [];
  let numOfEmailMap = new Map();

  for (let id of id_list) {
    numOfReportMap.set(id, 0);
    reportMap.set(id, []);
    numOfEmailMap.set(id, 0);
  }

  for (let value of reportSet) {
    const people = value.split(' ');

    const numOfReport = numOfReportMap.get(people[1]);
    numOfReportMap.set(people[1], numOfReport + 1);

    const reportList = reportMap.get(people[0]);
    reportMap.set(people[0], [...reportList, people[1]]);
  }

  numOfReportMap.forEach((value, key) => {
    if (value >= k) blockList.push(key);
  });

  reportMap.forEach((value, key) => {
    value.forEach((v) => {
      if (blockList.includes(v)) {
        const numOfEmail = numOfEmailMap.get(key);
        numOfEmailMap.set(key, numOfEmail + 1);
      }
    });
  });

  return [...numOfEmailMap.values()];
}

console.log(
  solution(
    ['muzi', 'frodo', 'apeach', 'neo'],
    ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi'],
    2
  )
);
