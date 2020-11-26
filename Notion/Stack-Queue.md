# Stack

<p>
스택(stack)은 데이터를 임시 저장할 때 사용하는 자료구조

데이터의 입력과 출력 순서는 후입선출(LIFO) 방식

> LIFO (Last in first out)
: 가장 나중에 넣은 데이터를 가장 먼저 꺼냄

> 예를 들어 접시를 쌓아두고 맨 윗 접시를 꺼내는 상황을 생각하면 됨

스택에 데이터를 넣는 작업을 푸시(push)라 하고, 스택에서 데이터를 꺼내는 작업을 팝(pop)이라 함

윗 부분을 꼭대기(top)라 하고, 아랫 부분을 바닥(bottom)이라고 함

푸시한 데이터는 스택 꼭대기에 쌓임

팝을 할 때는 꼭대기에 있는 데이터가 꺼내지므로 팝을 하면 방금 푸시한(가장 최근에 푸시 한) 데이터를 꺼낼 수 있음
</p>

<br>

# Queue

<p>
큐(queue)는 스택과 같이 데이터를 임시 저장하는 자료구조

데이터의 입력과 출력 순서는 후입선출(FIFO) 방식

> FIFO (First in first out)
: 가장 먼저 넣은 데이터를 가장 먼저 꺼냄

> 예를 들어 은행 창구에서 차례를 기다리거나 마트에서 계산을 기다리는 줄을 생각하면 됨

큐에 데이터를 추가하는 작업을 인큐(enqueue), 데이터를 꺼내는 작업을 디큐(dequeue)라고 함

데이터를 꺼내는 쪽(맨 앞의 원소)을 프런트(front), 데이터를 넣는 쪽(맨 끝의 원소)을 리어(rear)라고 함
</p>