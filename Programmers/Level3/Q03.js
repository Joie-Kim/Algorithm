// [2019 카카오 겨울 인턴십] 징검다리 건너기

function solution(stones, k) {
  let left = 1;
  let right = 200000000;

  function checkStone(mid) {
    let seqZero = 0;

    for (let i = 0; i < stones.length; i++) {
      if (stones[i] < mid) {
        seqZero++;
      } else {
        seqZero = 0;
      }

      if (seqZero >= k) {
        return false;
      }
    }

    return true;
  }

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (checkStone(mid)) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left - 1;
}

console.log(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3));
