# 소수 구하기

## Basic
```python
def is_prime(x):
    for i in range(2, x+1):
        if x % i == 0: return False
    return True
```

## 제곰근까지 비교하기 (1) - math.sqrt() 사용
```python
import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True
```

## 제곱근까지 비교하기 (2) - math 라이브러리 사용 x
```python
def is_prime(x):
    for i in range(2, (x ** 0.5)+1):
        if x % i == 0: return False
    return True
```

## 제곱근까지 비교하기 (3) - math 라이브러리 사용 x
```python
def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0: return False
        i += 1
    return True
```

## 에라토스테네스의 체 - x 이하인 수 중 소수 구하기
```python
def is_prime(x):
    a = [False, False] + [True] * (x-2)
    primes = []

    for i in range(2, x+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    
    return primes