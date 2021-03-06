# Tree

## 관련 용어
트리는 노드(node)와 가지(edge)로 구성되고, 각 노드는 가지를 통해 다른 노드와 연결됨<br>
- 루트(root) : 트리의 가장 위쪽에 있는 노드, 루트는 트리 하나에 1개만 존재
- 리프(leaf) : 가장 아래쪽에 있는 노드, 단말 노드(terminal node) 또는 외부 노드(external node)라고도 함
> 물리적으로 가장 밑에 위치한다는 의미가 아닌 가지가 더 이상 뻗어나갈 수 없는 마지막에 노드가 있음을 뜻함
- 비단말 노드(non-terminal node) : 리프를 제외한 노드(루트 포함), 내부 노드(internal node)라고도 함
- 자식(child) : 어떤 노드와 가지가 연결되었을 때 아래쪽 노드를 칭하며, 노드는 자식을 몇 개라도 가질 수 있음
- 부모(parent) : 어떤 노드와 가지가 연결되었을 때 가장 위쪽에 있는 노드를 칭하며, 노드의 부모는 하나뿐임
- 형제(sibling) : 부모가 같은 노드
- 조상(ancestor) : 어떤 노드에서 위쪽으로 가지를 따라가면 만나는 모든 노드
- 자손(descendant) : 어떤 노드에서 아래쪽으로 가지를 따라가면 만나는 모든 노드
- 레벨(level) : 루트에서 얼마나 멀리 떨어져 있는지를 나타내는 것
> 가장 위쪽에 있는 루트의 레벨은 0이며, 가지가 하나씩 아래로 뻗어 내려갈 때마다 레벨이 1씩 증가
- 차수(degree) : 각 노드가 갖는 자식의 수
> 모든 노드의 차수가 n 이하인 트리를 n진 트리라고 함
> 만약 모든 노드의 자식이 2개 이하면 이진 트리임
- 높이(height) : 루트에서 가장 멀리 있는 리프까지의 거리, 곧 리프 레벨의 최댓값을 뜻함
- 서브트리(subtree) : 어떤 노드를 루트로 하고, 그 자손으로 구성된 트리
- 빈 트리(None tree) : 노드와 가지가 전혀 없는 트리, 널 트리(null tree)라고도 함

<br>

## 순서 트리와 무순서 트리
트리는 형제 노드의 순서 관계가 있는지에 따라 두 종류로 분류됨<br>
형제 노드의 순서 관계가 있으면 `순서 트리(ordered tree)`라 하고, 구별하지 않으면 `무순서 트리(unordered tree)`라고 함

<br>

## 순서 트리의 검색
순서 트리의 노드를 스캔하는 방법은 크게 두 가지가 있음<br>
(아래 설명은 이진 트리를 기준으로 함)
### 너비 우선 검색
너비 우선 검색(breadth-first search)은 폭 우선 검색, 가로 검색, 수평 검색이라고도 함<br>
낮은 레벨부터 왼쪽에서 오른쪽으로 검색하고, 한 레벨에서 검색을 마친다면 다음 레벨로 내려가는 방법
### 깊이 우선 검색
깊이 우선 검색(depth-first search)은 세로 검색, 수직 검색이라고도 함<br>
리프에 도달할 때까지 아래쪽으로 내려가면서 검색하는 것을 우선으로 하는 방법<br>
리프에 도달해서 더 이상 검색할 곳이 없으면 일단 부모 노드로 돌아가고 그 뒤 다시 자식 노드로 내려감<br>
두 자식 가운데 하나 또는 둘 다 없으면 노드(부모 노드)를 지나가는 횟수가 줄어들겠지만, 각 노드를 최대 3번 지나게 됨<br>
이떄 세 종류의 스캔 방법으로 구분됨
> 1. 전위 순회 : 가장 처음에 부모 방문
> 2. 중위 순회 : 왼쪽 자식에서 오른쪽 자식으로 갈 때 부모 방문
> 3. 후위 순회 : 왼쪽 자식과 오른쪽 자식을 방문하고 나서 부모 방문
#### 전위 순회
전위 순회(preorder)는 다음과 같은 순서로 스캔함<br>
`노드 방문 → 왼쪽 자식 → 오른쪽 자식`
#### 중위 순회
중위 순회(inorder)는 다음과 같은 순서로 스캔함<br>
`왼쪽 자식 → 노드 방문 → 오른쪽 자식`
#### 후위 순회
후외 순회(postorder)는 다음과 같은 순서로 스캔함<br>
`왼쪽 자식 → 오른쪽 자식 → 노드 방문`

<br>

## 이진 트리
노드가 왼쪽 자식(left child)과 오른쪽 자식(right child)만 갖는 트리를 이진 트리(binary tree)라고 하며, 이때 두 자식 가운데 하나 또는 둘 다 존재하지 않는 노드가 있어도 상관 없음<br>
이진 트리의 특징은 왼쪽 자식과 오른쪽 자식을 구분한다는 것!<br>
또 왼쪽 자식을 루트로 하는 서브트리를 왼쪽 서브트리(left subtree)라 하고, 오른쪽 자식을 루트로 하는 서브트리를 오른쪽 서브트리(right subtree)라고 함

### 완전 이진 트리
루트부터 아래쪽 레벨로 노드가 가득 차 있고, 같은 레벨 안에서 왼쪽부터 오른쪽으로 노드가 채워져 있는 이진 트리를 완전 이진 트리(complete binary tree)라고 함<br>
노드를 채우는 방법은 다음과 같음
> - 마지막 레벨을 제외하고 모든 레벨에 노드가 가득 차 있음
> - 마지막 레벨에 한해서 왼쪽부터 오른쪽으로 노드를 채우되 반드시 끝까지 채우지 않아도 됨

높이가 k인 완전 이진 트리가 가질 수 있는 노드의 수는 최대 `2^(k+1) - 1`이므로, n개의 노드를 저장할 수 있는 완전 이진 트리의 높이는 `log n`

<br>

## 이진 검색 트리
이진 검색 트리(binary search tree)는 모든 노드가 다음 조건을 만족해야 함
> - 왼쪽 서브트리 노드의 키값은 자신의 노드 키값보다 작아야 함
> - 오른쪽 서브트리 노드의 키값은 자신의 노드 키값보다 커야 함

따라서 키값이 같은 노드는 복수로 존재하지 않음 (힙 정렬때 했었음)<br>

이진 검색 트리는 다음과 같은 특징이 있어서 알고리즘에서 폭 넓게 사용되고 있음
> - 구조가 단순함
> - 중위 순회의 깊이 우선 검색을 통하여 노드값을 오름차순으로 얻을 수 있음
> - 이진 검색과 비슷한 방식으로 아주 빠르게 검색할 수 있음
> - 노드를 삽입하기 쉬움

### 균형 검색 트리
이진 검색 트리는 키의 오름차순으로 노드가 삽입되면 트리의 높이가 깊어진다는 단점이 있음<br>
예를 들어, 1, 2, 3, 4, 5 순으로 노드를 삽입하면 직선 모양의 트리가 됨 (실제로 선형 리스트처럼 되어 아주 빠른 검색을 수행할 수 없게 됨)<br>
이와 같은 높이를 O(log n)으로 제한하여 고안된 검색 트리를 `균형 검색 트리(self-balancing search tree)`라고 함<br>

이진의 균형 검색 트리로는 다음과 같은 종류가 있음
> - AVL 트리 (AVL tree)
> - 레드-블랙 트리 (red-black tree)

이진이 아닌 균형 검색 트리로는 다음과 같은 종류가 있음
> - B 트리 (B tree)
> - 2-3 트리 (2-3 tree)