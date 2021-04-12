function solution(begin, target, words) {
  if (!words.includes(target)) return 0;
  let answers = [];

  // 한 글자 빼고 같은지 확인하는 함수
  const checkWord = (word1, word2) => {
    let check = 0;
    for (let i = 0; i < word1.length; i++) {
      if (word1[i] === word2[i]) {
        check += 1;
      }
    }

    return check === word1.length - 1 ? true : false;
  };

  const dfs = (thisWord, level, visit) => {
    // 현재 단어와 한 글자만 다른 단어들을 임시 배열에 넣음
    const tmp = words.filter(
      (word) => !visit.has(word) && checkWord(thisWord, word)
    );

    // 만약 다음 레벨에 target이 있다면
    if (tmp.includes(target)) {
      answers.push(level + 1);
      return;
    }

    // 임시 배열을 순회하면서 다음 레벨의 단어를 탐색하는 함수를 재귀적으로 수행
    tmp.forEach((node) => {
      const visited = new Set([...visit]);
      visited.add(node);
      dfs(node, level + 1, visited);
    });
  };

  dfs(begin, 0, new Set());

  return answers.length < 1 ? 0 : Math.min(...answers);
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
//console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));
