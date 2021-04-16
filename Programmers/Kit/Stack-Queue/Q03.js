function solution(bridge_length, weight, truck_weights) {
  let time = 0; // 걸린 시간
  let onBridge = []; // 다리 위에 있는 트럭 리스트
  let totalWeight = 0; // 다리 위에 있는 트럭의 총 무게
  let arrivedNum = 0; // 다리를 건넌 트럭 개수

  while (truck_weights.length != 0) {
    time += 1; // 시간 지남

    // 다리에 올라갈 수 있는 트럭수 체크
    // 만약 가득 차있으면
    if (onBridge.length === bridge_length) {
      totalWeight -= onBridge.shift(); // 맨앞 트럭을 다리에서 내보내고
    }

    // 다리에 있는 트럭 무게 체크
    // 견딜 수 있으면
    if (totalWeight + truck_weights[0] <= weight) {
      let thisTruck = truck_weights.shift();
      onBridge.push(thisTruck);
      totalWeight += thisTruck;
    } else {
      onBridge.push(0);
    }
  }

  time += bridge_length; // 마지막 트럭이 다리를 건너는 시간 추가

  return time;
}

console.log(solution(2, 10, [7, 4, 5, 6]));
console.log(solution(100, 100, [10]));
console.log(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));
