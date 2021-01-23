# Hash

## Hashing (해시법)

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

## Hash collision (해시 충돌)

- 키와 해시값의 대응 관계가 꼭 1:1일 필요는 없다.

    키와 해시값은 일반적으로 n:1이다.

- 이런 경우 저장할 버킷이 중복되는 현상이 발생하고, 이를 충돌이라 한다.
- 이렇게 해시법에서 충돌이 발생하는 경우, 2가지 방법으로 대처할 수 있다.
    1. 체인법 : 해시값이 같은 원소를 연결 리스트로 관리한다.
    2. 오픈 주소법 : 빈 버킷을 찾을 때까지 해시를 반복한다.

### Chaining (체인법)

- 해시값이 같은 데이터를 체인 모양의 연결 리스트로 연결하는 방법을 말한다.
- 오픈 해시법(open hashing)이라고도 한다.
- 예를 들어, 69와 17의 해시값은 둘 다 4 이다. (해시 함수가 13으로 나눈 나머지를 구하는 연산일 경우)

    버킷 x[4]에 이 둘을 연결하는 연결 리스트를 저장한다.

- 해시 테이블에서 데이터가 하나도 없는 버킷의 값을 None이라고 한다.

### Open addressing (오픈 주소법)

- 충돌이 발생했을 때 재해시(rehashing)을 수행하여 빈 버킷을 찾는 방법을 말한다.
- 닫힌 해시법(closed hashing)이라고도 한다.
- 빈 버킷이 나올 때까지 재해시를 반복하므로 선형 탐사법(liner probing)이라고도 한다.
- 삭제 후에 삭제 완료 상태를 표시 해야 한다.

    해시값이 같은 데이터를 처리하기 위함이다.

    예를 들어, 해시 함수가 13으로 나눈 나머지를 구하는 연산일 경우 5와 18의 해시값은 5로 같다.

    5를 먼저 x[5] 버킷에 저장하고, 18을 추가하려 할 때 재해시를 거쳐 x[7]에 저장 되었다고 가정 해보자.

    5를 삭제하고 상태 값을 표시하지 않으면, 18을 삭제하려 할 때 x[5]에 가서 삭제를 시도 하고, 값이 없어 삭제 실패를 반환하게 된다.

    따라서 5를 삭제한 후 x[5]의 상태를 '이 버킷의 값은 삭제 되었어'라고 표시를 해줘야 다음 버킷으로 이동해 재해시 한 값과 비교할 수 있다.