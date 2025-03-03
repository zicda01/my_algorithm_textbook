# Stack 1
## 스택
- 스택의 특성
    - 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
    - 스택에 저장된 자료는 선형 구조를 갖는다.
    - 선형구조: 자료 간의 관계가 1대1의 관계를 갖는다.
    - 비선형 구조: 자료 간의 관계가 1대N의 관계를 갖는다.
    - 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
    - 마지막에 삽입한 자료를 가장 먼저 꺼낸다.
    - **후입선출(LIFO, Last-In-First-Out)**
    - 예를 들어 스택에 1, 2, 3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉 3, 2, 1 순으로 꺼낼 수 있다.

- 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산
    - 자료구조: 자료를 선형으로 저장할 저장소
        - 배열을 사용할 수 있다.
        - 저장소 자체를 스택이라 부르기도 한다.
        - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.
    - 연산
        - 삽입: 저장소에 자료를 저장한다. 보통 push라고 부른다.
        - 저장소에서 자료를 꺼낸다., 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.
        - 스택이 공백인지 아닌지를 확인하는 연산. isEmpty
        - 스택의 top에 있는 item(원소)을 반환하는 연산. peek
    - 스택의 삽입/삭제 과정
    ![Alt text](/stack_1_ref/stack_1_1.png)
    - 스택의 push 알고리즘
        - append 메소드를 통해 리스트의 마지막에 데이터를 삽입
        ```python
        def push(item) :
            s.append(item)
        ```

        ```python
        def push(itme, size):
            global top
            top += 1
            if top == size:
                print('overflow!')
            else:
                stack[top] = item
        
        size = 10
        stack = [0] * size
        top = -1

        push(10, size)
        top += 1
        stack[top] = 20
        ```

    - 스택의 pop 알고리즘
    ```python
    def pop():
        if len(s) == 0:
            # underflow
            return
        else:
            return s.pop()
    ```
    ```python
    def pop():
        global top
        if top == -1:
            print('underflow')
            return 0
        else:
            top -= 1
            return stack[top + 1]
    
    print(pop())

    if top > -1:
        top -= 1
        print(stack[top+1])
    ```
## 스택의 응용1: 괄호 검사
![Alt text](/stack_1_ref/stack_1_2.png)
![Alt text](/stack_1_ref/stack_1_3.png)
- 괄호를 조사하는 알고리즘 개요
    - 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입하고, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지를 검사한다.
    - 이 때, 스택이 비어 있으면 조건1 또는 조건2에 위배되고 괄호의 짝이 맞지 않으면 조건3에 위배된다.
    - 마지막 괄호까지를 조사한 후에도 스택ㅇ네 괄호가 남아 있으면 조건 1에 위배된다.

## 스택의 응용2: Function Call
- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리
    - 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택을 이용하여 수행순서 관리
    - 함수 호출이 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 스택 프레임(stack frame)에 저장하여 시스템 스택에 삽입
    - 함수의 실행이 끝나면 시스템 스택의 top(스택 프레임)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
    - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 된다.

- 함수 호출과 복귀에 따른 전체 프로그램의 수행 순서
![Alt text](/stack_1_ref/stack_1_4.png)
![Alt text](/stack_1_ref/stack_1_5.png)

## 재귀호출
- 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조
- 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 크기를 줄이고 간단하게 작성
    - 재귀 호출의 예: facorial
        ![Alt text](/stack_1_ref/stack_1_6.png)
- 피보나치 수열
    ![Alt text](/stack_1_ref/stack_1_7.png)
    ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n - 1) + fibo(n - 2)
    ```

### 재귀 호출 연습
- 모든 배열 원소에 접근하기
```python
def f(i, N):
    if i == N:
        return
    else:
        print(arr[i])
        f(i + 1, N)
```
- 배열에 v가 있으면 1, 없으면 0을 리턴
```python
def f(i, N, v): # 찾는 값 v
    if i == N :
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i + 1, N)
```
## Memoization
- 앞의 예에서 피보나치 수를 구하는 함수를 재귀함수로 구현한 알고리즘은 **엄청난 중복 호출이 존재한다**는 문제점을 가지고 있다.
![Alt text](/stack_1_ref/stack_1_8.png)
- **메모이제이션(memoization)**은 컴퓨터 프로그램을 실행할 때 이전에 계산한 갑ㄷㅅ을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.
- 'memoization'은 글자 그대로 해석하면 '메모리에 넣기(to put in memory)' 라는 의미이며, 기억되어야 할 것이라는 뜻의 라틴어 'memorandum'에서 파생되었다.
- 앞의 예에서 피보나치 수를 구하는 알고리즘에서 fibo(n)의 값을 계산하자마자 저장하면(memoize), 실행시간을 O(n)으로 줄일 수 있다.
- Memoization 방법을 적용한 알고리즘은 다음과 같다.
```python
# memo를 위한 배열을 할당하하고, 모두 0으로 초기화 한다.
# memo[0]을 0으로 memo[1]는 1로 초기화 한다.
def fibo1(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n - 1) + fibo1(f - 2)
    return memo[n]

memo = [0] * (n + 1)
memo[0] = 0
memo[1] = 1
```

## DP
- 동적 계획(Dynamic Programming) 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.
- 동적 계획 알고리즘은 먼저 입력 크기가 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.
- 피보나치의 수 DP 적용
    - 피보나치 수는 부분 문제의 답으로부터 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다.
    1. 문제를 부분 문제로 분할한다.
    ![alt](/stack_1_ref/stack_1_9.png)
    2. 부분 문제로 나누는 일을 끝냈으면 가장 작은 부분 문제부터 해를 구한다.
    3. 그 결과는 테이블에 저장하고, 테이브렝 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구한다.
    ![alt](/stack_1_ref/stack_1_10.png)
    - 피보나치 수 DP 적용 알고리즘
    ```python
    def fibo2(n):
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
    ```
## DFS(깊이 우선 탐색)
- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함
- 두 가지 방법
    - 깊이 우선 탐색(Depth First Search, DFS)
    - 너비 우선 탐색(Breadth First Search, BFS)
- 깊이 우선 탐색
    - 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 골이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
    - 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 **후입선출 구조의 스택 사용**
- 로봇이 선을 따라 모든 칸을 탐색하는 방법
![alt](/stack_1_ref/stack_1_11.png)
1) 시작 정점 v를 결정하여 방문한다.
2) 정점 v에 인접한 정점 중에서
    - 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 (2)를 반복한다.
    - 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 (2)를 반복한다.
3) 스택이 공백이 될 때까지 (2)를 반복한다.
```python
def dfs(v, N):                          # 출발점 v, 마지막 정점 N
    visited = [0] * (N + 1)             # 방문 표시 기록용
    stack = []                          # 스택

    while True:
        if visited[v] == 0:             # 첫 방문이면
            visited[v] = 1              # 방문 표시
        
        for w in adj_list[v]:           
            if visited[w] == 0:         # 인접하고 방문 안 한 w가 있으면,
                stack.append(v)         # 현재 정점 push
                v = w                   # w로 이동
                break               
        else:                           
            if stack:                   # 더 이상 갈 곳이 없다면,
                v = stack.pop()         # top 스택 제거
            else:                       # 스택이 비어있다면,
                break                   # 반복문 탈출출
V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]   # 이하 인접리스트 입력 받기
for i in range(E):
    v, w = graph[i*2], graph[i*2 + 1]

    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(1, V)
```
