# 최대공약수, 최소공배수 구하기

## 최대공약수(Greatest Common Divisor, GCD)

최대공약수는 `유클리드 호제법(Euclidean Algorithm)`으로 구할 수 있으며, 원리는 다음과 같다.

- 임의의 두 자연수 a, b가 주어졌을 때, 둘 중 큰 값이 a라 하자.
- a를 b로 나눈 나머지를 n이라 하면 n이 0일 때, b가 최대 공약수이다.
- 만약 n이 0이 아니라면, a에 b를 b에 n을 대입해 다시 반복한다.

이는 반복문 또는 재귀를 이용해 구현할 수 있다.

### 반복문을 이용한 방법

```jsx
function gcd(a, b) {
  let n = 0;
  while (b !== 0) {
    n = a % b;
    a = b;
    b = n;
  }
  return a;
}
```

### 재귀를 이용한 방법

```jsx
function gcd(a, b) {
  if (b === 0) {
    return a;
  } else {
    return gcd(b, a % b);
  }
}
```

## 최소공배수(Least Common Multiple)

최대공약수를 구했다면 최소공배수는 쉽게 구할 수 있다.

`최소공배수 = 두 자연수의 곱 / 최대공약수`
