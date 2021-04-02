function solution(begin, target, words) {
  if (!words.includes(target)) return 0;
  let answer = 0;
  let queue = [];
  let tmp = [];
  let visited = new Set();

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

  // 1. 루트 노드 선언
  queue.push(begin);

  while (queue.length) {
    // 현재 단어 꺼내기
    const thisWord = queue.shift();
    // 방문한 단어로 추가
    visited.add(thisWord);

    // 만약 현재 단어와 target이 같다면 현재 레벨을 반환
    if (thisWord === target) {
      return answer;
    }

    // 현재 단어와 한 글자만 다른 단어들을 임시 배열에 넣음
    words.forEach((word) => {
      if (!visited.has(word) && checkWord(word, thisWord)) {
        tmp.push(word);
      }
    });

    // queue가 비었다는 건 현재 레벨에서 확인할 게 끝났다는 뜻
    // 임시 배열에 있는 다음 레벨에 비교할 단어들을 넣어줌
    if (queue.length < 1) {
      answer += 1;
      queue.push(...tmp);
      tmp = [];
    }
  }

  return answer;
}

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));
