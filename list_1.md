# LIST_1
- 과정 소개
- 알고리즘
- 배열
- 연습문제
- 버블 정렬 (Bubble Sort)
- 카운팅 정렬 (Counting Sort)
- 완전검색
- 그리디 (Greedy Algorithm)

---
## 알고리즘
```
유한한 단계를 통해 문제를 해결하기 위한 절차나 방법이다. 주로 컴퓨터 용어로 쓰이며, 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법을 말한다.
```
- 의사코드(pseudocode)와 순서도로 표현
- 무엇이 좋은 알고리즘인가?
    1. 정확성 : 얼마나 정확하게 동작하는가
    2. 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
    3. 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
    4. 단순성 : 얼마나 단순한가
    5. 최적성 : 더 이상 개선할 여지 없이 최적화되었는가

- 주어진 문제를 해결하기 위해 어떤 알고리즘을 사용해야 하는가?

- 시간 복잡도(Time Complexity)
    - 실제 걸리는 시간을 측정
    - 실행되는 명령문의 개수를 계산
- 빅-오(O) 표기법
    - n에 대한 항만을 표시
    - 계수(Coefficiont)는 생략

## 배열
```
일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
```
- 배열의 필요성
    - 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 비효율적
    - 다수의 변수로 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.
    - 배열 원소의 합 s 계산하기
    ```python
    s = 0
    for i in range(N):
        s += arr(i)
    ```
    - 배열 원소 중 최댓값 max_v 찾기
    ```python
    max_v = arr[0]
    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
    ```
    - 배열 원소 중 최댓값의 인덱스 max_idx 찾기
    ```python
    max_idx = 0
    for i in ragne(1, N):
        if arr[max_idx] < arr[i]
            max_idx = i
    ```
    - 최댓값이 여러 개인 경우 마지막 인덱스 max_idx 찾기
    ```python
    amx_idx = 0
    for i in range(i, N):
        if arr[max_idx] <= arr[i]:      # 더 큰 값 또는 같은 값이라면
            max_idx = i                 # max_idx 갱신
    ```
    - 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기
    ```python
    idx = -1
    for i in range(N):
        if arr[i] == V:
            idx = i
            break                       # 찾았다면 반복 종료
    ```
---
- 연습문제 1
- 연습문제 2
---
## 버블 정렬
- 정렬 : 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순 : ascending), 혹은 그 반대의 순서대로(내림차순 : descending) 재배열하는 것
- 키 : 자료를 정렬하는 기준이 되는 특정 값
- 대표적인 정렬 방식의 종류
    - 버블 정렬(Bubble Sort)            *# 250217 과목 평가 대상*
    - 카운팅 정렬 (Counting Sort)       *# 250217 과목 평가 대상*
    - 선택 정렬 (Selection Sort)        *# 250217 과목 평가 대상*
    - 퀵 정렬 (Quick Sort)
    - 삽입 정렬 (Insertion Sort)
    - 병합 정렬 (Merge Sort)
- 버블 정렬
```
인접한 두 개의 원소를 비교하며 자리를 계쏙 교환하는 방식
```
- 정렬 과정
    1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.
    2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.
    3. 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블 정렬이라고 한다.

- 시간 복잡도 : O(n^2)
- 버블 정렬의 구현(오름차순)
```python
def BubbleSort(a, N):                               # 정렬할 List, N 원소 수
    for i in range(N - 1, 0, - 1):                  # 인덱스 범위의 끝부터 역순으로 순회
        for j in range(i):                          # 비교할 왼쪽 원소의 인덱스 j
            if a[j] > a[j + 1] :
                a[j], a[j + 1] = a[j + 1], a[j]
```
- exercise
```python
# Bubble_Sort:

list_a = [5 ,2, 9, 1, 5, 6]

for j in range(len(list_a) - 1):
    for i in range(1, len(list_a) - j):
        if list_a[i - 1] > list_a[i]:
            list_a[i - 1], list_a[i] = list_a[i], list_a[i -1]

print(list_a)               # [1, 2, 5, 5, 6, 9]
```
# 카운팅 정렬
```
항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘
```
- 제한 사항
    - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
        - 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
    - 카운트들을 위한 충분한 공간을 할다앟려면 집합 내의 가장 큰 정수를 알아야한다.
- 시간 복잡도 : O(n + k) 
    - n은 리스트의 길이, k는 정수의 최댓값
- 카운팅 정렬의 구현
```python
def Counting_Sort(DATA, TEMP, k):
    # DATA [] -- 입력 배열 (원소는 0 이상 k이하의 정수)
    # TEMP [] -- 정렬된 배열(result)
    # COUNTS [] -- 카운트 배열

    COUNTS = [0] * (k + 1)

    for i in range (len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k + 1):
        COUNTS[i] += COUNTS[i - 1]          # 배열의 실질적인 크기 정보를 입력하는 작업
    
    TEMP = [0] * len(DATA)
    for i in range(len(DATA) - 1, -1, -1):
        COUNTS[DATA[i]] -= 1                # COUNTS 개수를 1씩 감소하며,
        TEMP[COUNTS[DATA[i]]] = DATA[i]     # TEMP에 DATA를 삽입
```

- exercise
    ```python
    list_a = [0, 4, 1, 3, 1, 2, 4, 1]

    A = max(list_a)

    counts = [0] * (A + 1)
    for i in list_a:
        counts[i] += 1

    for i in range(1, A + 1):
        counts[i] = counts[i] + counts[i - 1]

    temp = [0] * len(list_a)
    for i in range(7, -1, -1):
        counts[list_a[i]] -= 1
        temp[counts[list_a[i]]] = list_a[i]
    print(temp)         # [0, 1, 1, 1, 2, 3, 4, 4]
    ```
---
# 완전검색
```
완전 검색 방법은 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
```
- Brute-force 혹은 generate-and-test 기법
- 경우의 수가 상대적으로 작을 때 유용
- 알고리즘 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출하고, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것(*최적화*)이 바람직하다
- 순열(Permutation)
    - 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것
    - 서로 다른 n개 중 r개를 택하는 순열은 다음과 같이 표현한다
    ```
    nPr

    nPr = n * (n-1) * (n-2) * ... * (n-r+1)

    nPn = n! = n * (n-1) * (n-2) * ... * 2 * 1
    ```
    - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop를 이용해 아래와 같이 구현할 수 있다.
    ``` python
    # example = {1, 2, 3}

    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2 , i3)
    ```
---
# 탐욕 알고리즘
```
탐욕 알고리즘은 최적해를 구하는 데 사용되는 근시안적인 방법

여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
```
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없다.
- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.
- 탐욕 알고리즘의 동작 과정
    1. 해 선택: 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해집합(Solution Set)에 추가한다.
    2. 실행 가능성 검사: 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는지를 검사한다.
    3. 해 검사: 새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체 문제의 해가 완성되지 않았다면 1의 해 선택부터 다시 시작한다.

- 탐욕 알고리즘의 예
    - 거스름돈 줄이기

- 카운팅을 통한 Baby-Gin 풀이 알고리즘 구현(Greedy)
```python
num = 456789
c = [0] * 12

while num > 0:
    c[num % 10] += 1
    num = num // 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("baby gin")
else:
    print("lose")

    # 그러나 그리디 알고리즘을 통한 풀이이므로 예외가 존재한다.
```