// 멀쩡한 정사각형

// 공식을 이용한 풀이
// 지워지는 사각형의 수 = w + h - GCD(w, h)
function solution(w, h) {
  function GCD(a, b) {
    if (a % b === 0) {
      return b;
    } else {
      return GCD(b, a % b);
    }
  }

  let delRec = 0;

  if (w >= h) {
    delRec = w + h - GCD(w, h);
  } else {
    delRec = w + h - GCD(h, w);
  }

  return w * h - delRec;
}

// 기울기를 이용한 풀이
/*
function solution(w,h){
    const slope = h / w;
    let result = 0;

    for(let i = 1; i <= w; i++){
        result += Math.ceil(slope * i);
    }

    return ((h * w) - result) * 2;
}
*/
