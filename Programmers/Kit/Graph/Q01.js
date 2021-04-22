function solution(n, edges) {
  let visited = Array.from({ length: n + 1 }, () => false); // 0~n까지
  let level = new Array(n + 1);
  let queue = [1];
  visited[1] = true;
  level[0] = 0;
  level[1] = 0;

  let lev = 0;
  while (queue.length) {
    const node = queue.shift();
    lev = level[node] + 1;

    for (const e of edges) {
      if (e[0] === node && visited[e[1]] === false) {
        queue.push(e[1]);
        visited[e[1]] = true;
        level[e[1]] = lev;
      } else if (e[1] === node && visited[e[0]] === false) {
        queue.push(e[0]);
        visited[e[0]] = true;
        level[e[0]] = lev;
      }
    }
  }

  return level.filter((l) => l === lev - 1).length;
}
