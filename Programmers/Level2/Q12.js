// Q12. JadenCase 문자열 만들기

function solution(s) {
  var answer = "";
  const arr = s.split(" ");

  for (let i = 0; i < arr.length; i++) {
    let str = arr[i].toLowerCase();

    // 정규식으로 앞이 문자인지 숫자인지 확인
    // 굳이 없어도 됨. 그냥 무조건 첫 문자를 대문자로 변경해도 됨
    if (/^\D/g.test(str) === true) {
      str = str[0].toUpperCase() + str.slice(1);
    }

    answer += i === arr.length - 1 ? str : str + " ";
  }

  return answer;
}

// 이렇게 해도 됨..!
// 근데 이게 한 줄 말고 나눠서 표현은 안 됨.. 왜 그럴까?
//return s.split(" ").map(v => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase()).join(" ");
