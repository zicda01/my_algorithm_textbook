# Queue
- 큐(Queue)의 특성
    - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
        - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조

    - **선입선출구조(FIFO: First In First Out)**
        - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)된다.
- 큐의 구조 및 기본연산
![alt](/queue_1_ref/queue_1_1.png)
- 큐의 사용을 위해 필요한 주요 연산은 다음과 같음
![alt](/queue_1_ref/queue_1_2.png)
![alt](/queue_1_ref/queue_1_3.png)
![alt](/queue_1_ref/queue_1_4.png)
## 선형큐
- 1차원 배열을 이용한 큐
    - 큐의 크기 = 배열의 크기
    - front: 저장된 첫번째 원소의 인덱스
    - rear: 저장된 마지막 원소의 인덱스
- 상태 표현
    - 초기 상태: front = rear = -1
    - 공백 상태: front == rear
    - 포화 상태: rear == n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)
- 초기 공백 큐 생성
    - 크기 n인 1차원 배열 생성
    - front와 rear를 -1로 초기화
- 삽입: enQueue(item)
    - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
        1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
        2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
    ```python
    def enQueue(itme):
        global rear
        if isFull():
            print("Queue_Full")
        else:
            rear += 1
            Q[rear] = item
    ```
- 삭제: deQueue()
    - 가장 앞에 있는 원소를 삭제하기 위해
        1) front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소 이동
        2) 새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능함
    ```python
    def deQueue()
        global front
        if isEmpty():
            print("Queue_Empty")
        else:
            front += 1
            return Q[front]
## 원형큐
- 선형 큐 이용시의 문제점
    - 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n - 1인 상태 즉, 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
- 해결방법 1
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
- 해결방법 2
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
    - 원형 큐의 논리적 구조
- 초기 공백 상태
    - front = rear = 0
- Index의 순환
    - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
    - 이를 위해 나머지 연산자 mod를 사용함
- front 변수
    - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위치 및 삭제 위치
![alt](/queue_1_ref/queue_1_5.png)
- 원형 큐의 연산 과정
![alt](/queue_1_ref/queue_1_6.png)
![alt](/queue_1_ref/queue_1_7.png)
![alt](/queue_1_ref/queue_1_8.png)
- 원형 큐의 구형
    - 초기 공백 큐 생성
        - 크기 n인 1차원 배열 생성
        - front와 rear를 0으로 초기화
    - 이하 생략
## 연결큐
- [참고] **deque(덱)**
    - 컨테이너 자료형 중 하나
    - deque 개체
        - 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
    - 연산
        - append(x): 오른쪽에 x 추가
        - popleft(): 왼쪽에서 요소를 제거하고 반환. 요소가 없으면 IndexError
    ```python
    from collections import deque

    q = deque()
    q.append(1)     # enqueue()
    t = q.popleft() # dequeue()
    ```
## 우선순위 큐

## 버퍼

## BFS (Breadth First Search)
- 그래프를 탐색하는 방법에는 크게 두 가지가 있음
    - 깊이 우선 탐색(DFS)
    - 너비 우선 탐색(BFS)

- **너비우선탐색**은 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
- 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, <U>선입선출 형태의 자료구조인 큐를 활용함</U>
![alt](/queue_1_ref/queue_1_9.png)
- BFS 알고리즘 구현
```python
def BFS(G, v):                              # 그래프 G, 탐색 시작점 v
    visited = [0]*(n + 1)                   # 정점의 개수 n
    queue = []                      
    queue.append(v)                         # 시작점 v를 큐에 삽입
    visited[v] = 1
    while queue:                            # 큐가 비어있지 않다면,
        t = queue.pop(0)                    # 큐의 첫번째 원소 반환
        visit(t)                    
        for i in G[t]:                      # t와 연결된 모든 정점에 대해
            if not visited[i]:              # 방문되지 않은 곳이라면
                queue.append(i)             # 큐에 삽입
                visited[i] = visited[t] + 1 # n으로 부터 1만큼 이동동
```