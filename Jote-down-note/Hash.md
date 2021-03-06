# Hash

해시 테이블로 구현된 파이썬의 자료형은? 👉 딕셔너리

## Hashing (해시법)

> Hashing은 정보를 가능한 빠르게 저장하고 검색하기 위해 사용하는 중요한 기법 중 하나다. 최적의 검색이 필요한 분야에 사용되며, 심볼 테이블 등의 자료구조를 구현하기에도 적합하다.<br>이외에도 해시 함수는 체크섬(Checksum), 손실 압축, 무작위화 함수(Randomization function), 암호 등과도 관련이 깊으며 때로는 서로 혼용되기도 한다. 어느 정도 개념이 겹치긴 하지만, 서로 용도와 요구사항이 다른 만큼 각각 다르게 설계되고 최적화 된다.

- 해시법은 데이터를 저장할 위치 = 인덱스를 간단한 연산으로 구하는 것을 말한다.
- 원소의 검색뿐 아니라 추가나 삭제도 효율적으로 수행할 수 있다.
- 배열의 원소의 값을 키(key)라고 한다.

  ex) 18

- 키에 어떠한 연산을 해 만들어진 값을 해시값(hash value)라고 한다.

  ex) 키를 13으로 나눈 값 : 5

- 이렇게 키를 해시값으로 변환하는 과정을 해시 함수(hash function)라고 한다.

  일반적으로 해시 함수는 나머지를 구하는 연산 또는 그 연산을 응용할 때 주로 사용한다.

  ex) 키를 13으로 나누는 연산

- 해시값을 인덱스로 하여, 원소를 새로 저장한 배열을 해시 테이블(hash table)이라 한다.

  ex) 인덱스 5에 원소 18이 있는 배열

- 해시 테이블에서 만들어진 원소를 버킷(bucket)이라고 한다.

  ex) 버킷 x[5] = 18

### 성능 좋은 해시 함수의 특징

- 해시 함수 값 충돌의 최소화
- 쉽고 빠른 연산
- 해시 테이블 전체에 해시 값이 균일하게 분포
- 사용할 키의 모든 정보를 이용하여 해싱
- 해시 테이블 사용 효율이 높을 것

### Load factor (로드 팩터)

- 해시 테이블에 저장된 데이터 개수 n을 버킷의 개수 k로 나눈 것이다.

  `load factor = n / k`

- 로드 팩터 비율에 따라서 해시 함수를 재작성해야 될지 또는 해시 테이블의 크기를 조정 해야 할지를 결정한다.
- 또한, 해시 함수가 키들을 잘 분산해 주는지를 말하는 효율성 측정에도 사용된다.

<br>

## Hash collision (해시 충돌)

> 생각보다 충돌은 쉽게 발생한다. 흔한 에로 생일 문제(Birthday problem)를 들 수 있다.<br>생일의 가짓수는 365개(윤년 제외)이므로, 여러 사람이 모였을 때 생일이 같은 2명이 존재할 확률을 얼핏 생각해보면 비둘기집 원리(Pigeonhole principle)에 따라 366명 이상이 모여야 일어나는 일 같다. 하지만 실제로는 23명만 모여도 50%를 넘고, 57명이 모이면 그때부터는 99%를 넘어선다.

- 키와 해시값의 대응 관계가 꼭 1:1일 필요는 없다.

  키와 해시값은 일반적으로 n:1이다.

- 이런 경우 저장할 버킷이 중복되는 현상이 발생하고, 이를 충돌이라 한다.
- 이렇게 해시법에서 충돌이 발생하는 경우, 2가지 방법으로 대처할 수 있다.
  1. 체인법 : 해시값이 같은 원소를 연결 리스트로 관리한다.
  2. 오픈 주소법 : 빈 버킷을 찾을 때까지 해시를 반복한다.

### Chaining (체인법)

> 개별 체이닝(Seperate chaining)<br>: 해시 테이블의 기본 방식이기도 한 개별 체이닝은 충돌 발생 시 연결 리스트로 연결한다.

> 기본적인 자료구조와 임의로 정한 간단한 알고리즘만 있으면 되므로, 인기가 높다.

> 잘 구현한 경우 대부분의 탐색은 `O(1)`이지만 최악의 경우(즉, 모든 해시 충돌이 발생했다고 가정할 경우)에는 `O(n)`이 된다.

- 해시값이 같은 데이터를 체인 모양의 연결 리스트로 연결하는 방법을 말한다.
- 오픈 해시법(open hashing)이라고도 한다.
- 예를 들어, 69와 17의 해시값은 둘 다 4 이다. (해시 함수가 13으로 나눈 나머지를 구하는 연산일 경우)

  버킷 x[4]에 이 둘을 연결하는 연결 리스트를 저장한다.

- 해시 테이블에서 데이터가 하나도 없는 버킷의 값을 None이라고 한다.

### Open addressing (오픈 주소법)

> 무한정 저장할 수 있는 체인법과 달리, 전체 슬롯의 개수 이상은 저장할 수 없다. 충돌이 일어나면 테이블 공간 내에서 탐사(Probing)를 통해 빈 공간을 찾아 해결하며, 이 때문에 체인법과 달리 모든 원소가 반드시 자신의 해시값과 일치하는 주소에 저장된다는 보장은 없다.

- 충돌이 발생했을 때 재해시(rehashing)을 수행하여 빈 버킷을 찾는 방법을 말한다.
- 닫힌 해시법(closed hashing)이라고도 한다.
- 빈 버킷이 나올 때까지 재해시를 반복하므로 선형 탐사법(liner probing)이라고도 한다.
- 삭제 후에 삭제 완료 상태를 표시 해야 한다.

  해시값이 같은 데이터를 처리하기 위함이다.

  예를 들어, 해시 함수가 13으로 나눈 나머지를 구하는 연산일 경우 5와 18의 해시값은 5로 같다.

  5를 먼저 x[5] 버킷에 저장하고, 18을 추가하려 할 때 재해시를 거쳐 x[7]에 저장 되었다고 가정 해보자.

  5를 삭제하고 상태 값을 표시하지 않으면, 18을 삭제하려 할 때 x[5]에 가서 삭제를 시도 하고, 값이 없어 삭제 실패를 반환하게 된다.

  따라서 5를 삭제한 후 x[5]의 상태를 '이 버킷의 값은 삭제 되었어'라고 표시를 해줘야 다음 버킷으로 이동해 재해시 한 값과 비교할 수 있다.

- 선형 탐사법의 한 가지 문제점은 해시 테이블에 저장되는 데이터들이 고르게 분포되지 않고 뭉치는 경향이 있다는 점이다.

  해시 테이블 여기저기에 연속된 데이터 그룹이 생기는 현상을 클러스터팅(Clustering)이라 하는데, 클러스터들이 점점 커지게 되면 인근 클러스터들과 서로 합쳐지는 일이 발생한다.

  그렇게 되면 해시 테이블의 특정 위치에는 데이터가 몰리게 되고, 다른 위치에는 상대적으로 데이터가 거의 없는 상태가 될 수 있다. 이러한 클러스터링 현상은 탐사 시간을 오래 걸리게 하며, 전체적으로 해싱 효율을 떨어뜨리는 원인이 된다.

- 버킷 사이즈보다 큰 경우에는 삽입할 수 없다.

  따라서 일정 이상 채워지면, 즉 기준이 되는 로드 팩터 비율을 넘어서게 되면, 그로스 팩터(Growth factor)의 비율에 따라 더 큰 크기의 또 다른 버킷을 생성한 후 여기에 새롭게 복사하는 리해싱(Rehashing) 작업이 일어난다.

  이는 동적 배열에서 공간이 가득 찰 경우, 더블링으로 새롭게 복사해서 옮기는 과정과 유사하다.

> 파이썬의 해시 테이블은 충돌 시, 오픈 주소법 방식을 사용한다.
