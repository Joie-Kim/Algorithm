// [2019 카카오 겨울 인턴십] 불량 사용자

function solution(user_id, banned_id) {
  let answers = new Set();
  const bannedSize = banned_id.length;

  function dfs(index, users, selected) {
    if (index === bannedSize) {
      selected.sort();
      let result = "";
      result = selected.reduce((acc, cur) => acc + cur);
      answers.add(result);
      return;
    }

    const str = banned_id[index].replace(/[*]/g, ".");

    users.forEach((user, i) => {
      const arr = RegExp(str, "g").exec(user);
      if (arr !== null && arr[0].length === user.length) {
        let restUser = [...users];
        restUser.splice(i, 1);
        let newSelected = [...selected, user];
        dfs(index + 1, restUser, newSelected);
      }
    });
  }

  dfs(0, user_id, []);

  return answers.size;
}

console.log(
  solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
);
console.log(
  solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["*rodo", "*rodo", "******"]
  )
);
console.log(
  solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
  )
);
