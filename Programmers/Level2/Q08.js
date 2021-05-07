// [2019 카카오 겨울 인턴십] 튜플

function solution(s) {
  let answer = new Set();

  const sArray = s.replace(/^[{]|[}]$/g, "").split(/[,](?=[{])/g);

  sArray.sort((a, b) => a.length - b.length);

  for (let i = 0; i < sArray.length; i++) {
    sArray[i] = sArray[i].replace(/^[{]|[}]$/g, "").split(/[,]/g);
  }

  for (const a of sArray) {
    for (let i = 0; i < a.length; i++) {
      answer.add(parseInt(a[i]));
    }
  }

  return [...answer];
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"));
console.log(solution("{{20,111},{111}}"));
console.log(solution("{{123}}"));
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
