function solution(people, limit) {
  let answer = 0;

  // 사람들 무게를 정렬
  people.sort((a, b) => a - b);

  let left = 0; // 왼쪽 탐색 변수
  let right = people.length - 1; // 오른쪽 탐색 변수

  // people 순회
  while (left <= right) {
    // 만약 왼쪽 사람과 오른쪽 사람의 무게가 범위 안에 있으면 두 사람을 보트에 태우고 answer ++
    // 그렇지 않을 경우, 오른쪽 사람만 보트에 태우고 answer ++
    if (people[left] + people[right] <= limit) {
      left++;
    }
    right--;
    answer++;
  }

  return answer;
}

console.log(solution([70, 50, 80, 50], 100));
console.log(solution([70, 80, 50], 100));
