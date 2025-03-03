# Stack 2
## 계산기 1
## 계산기 2
## 백트래킹
- 백트래킹(Backtracking) 기법은 해를 찾는 도중에 '막히면'(즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법이다.
- 백트래킹 기법은 최적화(optimization) 문제와 결정(decision) 문제를 해결할 수 있다.
- 결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
    - 미로 찾기
    - n-Queen 문제
    - Map coloring
    - 부분 집합의 합(Subset Sum) 등.
- 백트래킹과 깊이우선탐색과의 차이
    - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(<U>Prunning 가지치기</U>)
    - 깊이우선탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단.
    - 깊이 우선탐색을 가하기에는 경우의 수가 너무나 많음. 즉, N! 가지의 경우의 수를 가진 문제에 대해 깊이우선탐색을 가하면 당연히 처리 불가능한 문제
    - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수 시간(Exponetial Time)을 요하므로 처리 불가능
- 백트래킹 기법
    - 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
    - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드를 유망하지 않않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
    - **가지치기(pruning)**: 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.
- 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행된다.
    1. 상태 공간 트리의 깊이 우선 검색을 실시한다.
    2. 각 노드가 유망한지를 점검한다.
    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속한다.
- 미로 찾기
![alt](/stack_2_ref/stack_2_1.png)
```python
# 출발점이 2, 도착점이 3인 미로의 백트래킹 적용 예시
## SWEA 11620.
def find_start(matrix, N):          # 출발지점 탐색
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                return i, j

T = int(input())

dr = [0, 0, 1, -1]                  # 2차원 배열 4방향(델타) 탐색색
dc = [1, -1, 0, 0]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    stack = list()
    visited = [[0] * N for _ in range(N)]           # 방문 기록 2차원 배열로 작성성

    sr, sc = find_start(matrix, N)
    visited[sr][sc] = 1                             # 출발 지점 방문 표시
    stack = [(sr, sc)]                              # 출발 지점 push
    tf = 0

    while stack:
        r, c = stack.pop()                          # pop을 통해 위치치 재할당
        if matrix[r][c] == 3:                       # 도착점 도달시 탈출
            tf = 1
            break

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] in (0, 3) and not visited[nr][nc]:    # 이동한 경로를 기록
                    stack.append((nr, nc))
                    visited[nr][nc] = 1
```
## 부분집합
- 어떤 집합의 공집합과 자기자신을 포함한 모든 부분집합을 **powerset**이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 <U>부분집합의 개수는 2^n</U>>개 이다.
- 백트래킹 기법으로 powerset을 만들어 보자.
    - 앞에서 설명한 일반적인 백트래킹 접근 방법을 이용한다.
    - n개의 원소가 들어있는 집합의 2^n개의 부분집합을 만들 때는, true 또는 false값을 가지는 항목들로 구성된 n개의 배열을 만드는 방법을 이용.
    - 여기서 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값이다.
- 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합을 생성하는 방법
```python
set_elements = ['A', 'B', 'C', 'D']     # 원소가 겹치지 않는 집합
bit = [0, 0, 0, 0]
for i in range(2):                      # 0번째 원소
    bit[0] = i
    for j in range(2):                  # 1번째 원소
        bit[1] = j
        for k in range(2):              # 2번째 원소
            bit[2] = k
            for l in range(2):          # 3번째 원소
                bit[3] = l
                subset = [set_elements[m] for m in range(4) if bit[m]]
                print(subset)           # 생성된 부분집합 출력
```
- powerset을 구하는 백트래킹 알고리즘
```python
def backtrack(a, k, n):     # 주어진 배열 a, 결정할 원소 k, 원소의 개수 n
    c = [0] * MAXCANDIDATES

    if K ==n:
        process_solution(a, k)      # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n ,c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)
    
def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end = " ")
    print()

MAXCANDIDATES = 2
NMAX = 4
a = [0] * [1, 2, 3, 4]
backtrack(a, 0, 3)
```
## 순열
- 단순하게 순열을 생성하는 방법
    - (예) 집합 {1, 2, 3}에서 모든 순열을 생성하는 함수
        - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop을 이용해 아래와 같이 구현할 수 있다.
        ```python
        for i1 in range(1, 4):
            for i2 in range(1, 4):
                if i2 != i1 :
                    for i3 in range(1, 4):
                        if i3 != i1 and i3 != i2:
                            print(i1, i2, i3)
        ```
- 백트래킹을 이용하여 {1 ,2 ,3, ..., NMAX}에 대한 순열 구하기
- (생략)

## 가지치기
![alt](/stack_2_ref/stack_2_2.png)
![alt](/stack_2_ref/stack_2_3.png)
![alt](/stack_2_ref/stack_2_4.png)
![alt](/stack_2_ref/stack_2_5.png)
```python
# 순열을 이용한 배열의 최소합 알고리즘 풀이 예시
## SWEA 11611.
def permu_sum_min(i, N, s):         # 배열의 행 i, 행렬의 크기 N, 순열의 합을 계산하기 위한 지역변수 s
    global min_sum
 
    if i == N:              # i가 마지막 행(N)을 탐색하면 min_sum 값 결정
        if min_sum > s:
            min_sum = s
    elif min_sum < s:       # s가 min_sum 보다 커지면 가지치기 후 종료
        return
    else:                   # 재귀 호출
        for j in range(i, N):   # 재귀 구조를 통해 i열부터 선택함
            p[i], p[j] = p[j], p[i]     # j열의 수를 선택하여, i열에서 추출하기 위한 자리 교환 (세로열 중복 해소)
            permu_sum_min(i + 1, N, s + matrix[i][p[i]])    # i열에서 추출한 값을 순열의 합으로 전달, i + 1행에서 재귀호출 반복
            p[i], p[j] = p[j], p[i]     # 자리 교환을 위해 원형 회복
    pass
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    p = list(range(N))      # 행렬의 인덱스로 동작
    min_sum = float('inf')
    permu_sum_min(0, N, 0)  # 재귀함수 호출
 
    print(f'#{tc}', end=" ")
    print(min_sum)
```