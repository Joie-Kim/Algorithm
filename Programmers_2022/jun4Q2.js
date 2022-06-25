// link: https://programmers.co.kr/learn/courses/30/lessons/42888

// function solution(record) {
//   const records = record.map((v) => v.split(' '));
//   let recordMap = new Map();
//   let answer = [];

//   for (const list of records) {
//     if (list[0] === 'Enter' || list[0] === 'Change') recordMap.set(list[1], list[2]);
//   }

//   for (const list of records) {
//     let string = '';
//     const nickname = recordMap.get(list[1]);

//     if (list[0] === 'Enter') string = nickname + '님이 들어왔습니다.';
//     else if (list[0] === 'Leave') string = nickname + '님이 나갔습니다.';

//     if (string.length) answer.push(string);
//   }

//   return answer;
// }

function solution(record) {
  let userInfo = new Map();
  let actions = [];
  const actionStringMap = {
    Enter: '님이 들어왔습니다.',
    Leave: '님이 나갔습니다.',
  };

  record.forEach((value) => {
    const [action, id, nick] = value.split(' ');

    if (action !== 'Change') {
      actions.push([id, action]);
    }

    if (nick) {
      userInfo.set(id, nick);
    }
  });

  return actions.map((value) => `${userInfo.get(value[0])}${actionStringMap[value[1]]}`);
}

console.log(
  solution(['Enter uid1234 Muzi', 'Enter uid4567 Prodo', 'Leave uid1234', 'Enter uid1234 Prodo', 'Change uid4567 Ryan'])
);
