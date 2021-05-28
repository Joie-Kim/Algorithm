// Q43. 로또의 최고 순위와 최저 순위

// 투포인터 이용하기
/*
function solution(lottos, win_nums) {
    const rank = [6, 6, 5, 4, 3, 2, 1];
    var answer = [];

    lottos.sort((a, b) => a - b);
    win_nums.sort((a, b) => a - b);
    
    let lPtr = 0;
    let wPtr = 0;
    let minCnt = 0;
    while (lPtr < 6 && wPtr < 6) {
        if (lottos[lPtr] < win_nums[wPtr]) {
            lPtr++;
        } else if (lottos[lPtr] > win_nums[wPtr]) {
            wPtr++;
        } else {
            minCnt++;
            lPtr++;
            wPtr++;
        }
    }
    
    let zero = lottos.reduce((acc, cur) => cur === 0 ? acc + 1 : acc, 0);
    let maxCnt = minCnt + zero;
    
    return [rank[maxCnt], rank[minCnt]];
}
*/

// filter 이용하기
function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];
  var answer = [];

  const minCnt = lottos.filter((v) => win_nums.includes(v)).length;
  const zeroCnt = lottos.filter((v) => !v).length;
  const maxCnt = minCnt + zeroCnt;

  return [rank[maxCnt], rank[minCnt]];
}
