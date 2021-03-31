function solution(clothes) {
  let answer = 1;
  let clothesObj = {};

  clothes.map((item) => {
    clothesObj[item[1]] = (clothesObj[item[1]] || 1) + 1;
  });

  for (let key in clothesObj) {
    answer *= clothesObj[key];
  }

  return answer - 1;
}
