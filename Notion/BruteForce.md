# Brute force

## 문자열 검색
문자열 검색(string searching)은 어떤 문자열 안에 다른 문자열이 포함되어 있는지 검사하고, 만약 포함되어 있다면 어디에 위치하는지 찾아내는 것을 말함<br>
만약 문자열 'STRING'에서 'IN'을 검색한다면, 검색되는 문자열인 'STRING'을 `텍스트(text)`, 찾아내는 문자열인 'IN'을 `패턴(pattern)`이라고 함

## 브루트 포스법
브루트 포스법(brute force method)은 문자열 검색 알고리즘 중에서 가장 기초적이고 단순한 방법으로 선형 검색을 단순하게 확장한 알고리즘이라 `단순법`이라고도 함<br>
만약 문자열 'ABABCDEFGHA'에서 'ABC'를 찾으려 한다면, 하나씩 모두 비교함
> 1. 'ABA' → 세 번째 글자가 같지 않음
> 2. 인덱스 한 칸 이동
> 3. 'BAB' → 첫 번째 글자가 같지 않음
> 4. 인덱스 한 칸 이동
> 5. 'ABC' → 모두 같음. 검색 성공!

## 멤버십 연산자와 표준 라이브러리를 사용한 문자열 검색
파이썬에서 문자열을 검색할 때, 멤버십 연산자나 표준 라이브러리를 사용하여 구현할 수 있음<br>

### 멤버십 연산자로 구현하기
멤버십 연산자(membership operator)인 `in`과 `not in`을 사용하면 어떤 문자열이 다른 문자열 안에 포함되어 있는지 검색할 수 있음<br>
예를 들어 txt 안에 ptn이 포함되어 있는지 판단할 때 다음과 같이 하면 됨
```python
ptn in txt      # ptn이 txt 안에 포함되어 있는지 확인
ptn not in txt      # ptn이 txt 안에 포함되어 있지 않은지 확인
```
이 방법은 어떤 문자열이 다른 문자열 안에 포함되어 있는지 판단할 수 있지만 그 위치를 알 수 없음

### find, index 계열 함수로 구현하기
str 클래스형에 소속된 `find()`, `rfind()`, `index()`, `rindex()` 함수는 문자열을 검색하여 검색한 문자열의 위치를 반환함

문자열 str의 [start: end]에 sub가 포함되면 그 가운데 가장 작은 인덱스를 반환하고, 그렇지 않으면 -1을 반환함
```python
str.find(sub[, start[, end]])
```

문자열 strdml [start:end]에 sub가 포함되면 그 가운데 가장 큰 인덱스를 반환하고, 그렇지 않으면 -1을 반환
```python
str.rfind(sub[, start[, end]])
```

find() 함수와 같은 기능을 수행하지만, sub가 발견되지 않으면 예외 처리로 ValueError를 내보낸다는 차이가 있음
```python
str.index(sub[, start[, end]])
str.rindex(sub[, start[, end]])
```

### with 계열 함수로 구현하기
with 계열 함수는 어떤 문자열이 다른 문자열의 시작이나 끝에 포함되어 있는지를 판단함

`startwith()`: 문자열이 prefix로 시작하면 True를, 그렇지 않으면 False를 반환함<br>
`endwith()`: 문자열이 suffix 끝나면 True를, 그렇지 않으면 False를 반환함<br>
start가 지정되어 있으면 그 위치에서 판단을 시작하고, end가 지정되어 있으면 그 위치에서 비교를 중지함
```python
str.startwith(prefix[, start [, end]])
str.endwith(suffix[, start [, end]])
```

<br>

**위 모든 함수의 `start`와 `end`는 생략 가능! 기본 값은 `0`**