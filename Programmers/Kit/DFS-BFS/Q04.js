function solution(tickets) {
  let answers = [];

  const dfs = (airport, leftTickets, path) => {
    // 경로에 현재 방문한 공항을 추가
    const newPath = [...path, airport];

    // 남은 티켓이 없을 경우
    if (leftTickets.length === 0) {
      // 경로를 answers 배열에 추가
      answers.push(newPath);
    } else {
      // 남은 티켓이 있을 경우, 티켓을 순회하며 탐색
      leftTickets.map((ticket, index) => {
        // 현재 방문한 공항이 출발지인 티켓을 찾아서
        if (ticket[0] === airport) {
          let newTickets = [...leftTickets];
          // 그 티켓을 사용하고
          const [[from, to]] = newTickets.splice(index, 1);
          // 재귀 탐색
          dfs(to, newTickets, newPath);
        }
      });
    }
  };

  dfs("ICN", tickets, []);

  return answers.sort()[0];
}

console.log(
  solution([
    ["ICN", "JFK"],
    ["HND", "IAD"],
    ["JFK", "HND"],
  ])
);
console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
