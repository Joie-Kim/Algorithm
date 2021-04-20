# Lower Bound, Upper Bound

이분 탐색에서 파생된 방법이다.

이분 탐색이 `원하는 k 값을 찾는 과정`이라면,

- Lower Bound : 원하는 `k 값 이상`의 값이 처음 나오는 위치를 찾는 과정
- Upper Bound : 원하는 `k 값 초과`의 값이 처음 나오는 위치를 찾는 과정

## Lower Bound

정렬된 데이터 `arr = [1, 3, 5, 7, 9, 11]`에서 `k = 8` 이상인 값이 처음 나오는 위치를 구해보자.

1. 시작 위치=0, 끝 위치=5으로 설정한다.
2. 시작 위치과 끝 위치 5의 중간 위치인 2((0+5) / 2)번째 값을 8과 비교한다.
   `* 나누기 할 때, 소수점 나오면 버리기`
3. 5는 8보다 작으므로 시작 위치를 2 다음인 3으로 설정한다.
4. 시작 위치 3과 끝 위치 5의 중간 위치인 4번째 값을 8과 비교한다.
5. 9는 8보다 크다. <u>이때에는 이분 탐색과 달리, 끝 위치를 중간 위치인 4로 설정한다.</u>
   `* 8 이상인 값이 처음 나오는 위치를 구하는 것이므로, 이전 값 중에 조건을 만족하는 게 있는지 확인 해야 함`
6. 시작 위치=3, 끝 위치=4이므로 중간 위치인 3번째 값을 8과 비교한다.
7. 7은 8보다 작다. 따라서 시작 위치를 중간 위치+1 = 4로 설정한다.
8. 시작 위치 = 끝 위치 = 4이므로 4번째 값인 9가 Lower Bound가 된다.

```jsx
// 원하는 값(k) 이상의 값이 처음 나오는 위치 반환
const getLowerBound = (arr, k) => {
  let start = 0;
  let end = arr.length - 1;
  let Mid;

  while (start < end) {
    Mid = Math.floor((start + end) / 2);

    if (arr[Mid] >= k) {
      end = Mid;
    } else {
      start = Mid + 1;
    }
  }

  return end;
};
```

## Upper Bound

Lower Bound와 동일하고, 조건만 수정했다. (이상 X, 초과 O)

```jsx
// 원하는 값(k) 초과의 값이 처음 나오는 위치 반환
const getUpperBound = (arr, k) => {
  let start = 0;
  let end = arr.length - 1;
  let Mid;

  while (start < end) {
    Mid = Math.floor((start + end) / 2);

    if (arr[Mid] > k) {
      end = Mid;
    } else {
      start = Mid + 1;
    }
  }

  return end;
};
```
