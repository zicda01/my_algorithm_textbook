# LIST_2
- 2차원 배열
- 델타
- 부분집합
- 검색
- 이진 검색(Binary Search)
- 선택 정렬(Selection Sort)
- 셀렉션 알고리즘(Selection Algorithm)
## 2차원 배열
- 2차원 배열의 선언
    - 1차원 list를 묶어놓은 list
    - 2차원 이상의 다차원 list는 차원에 따라 index를 선언
    - 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
    - Python 에서는 데이터 초기화를 통해 변수선언과 초기화가 가능함
    ```python
    arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
    ```
    - 배열 순회
        - 행 우선 순회
        ```python
        for i in range(n):
            for j in range(m):
                f(array[i][j])          # 필요한 연산 수행
        ```
        - N * M 배열의 합을 구하는 방법
        ```python
        s = 0
        for i in range(N):
            for j in range(M):
                s += arr[i][j]
        ```
        - 열 우선 순회
        ```python
        for j in range(m):
            for i in range(n):
                f(array[i][j])          # 필요한 연산 수행
        ```
        - 지그재그 순회
        ```python
        for i in range(n):
            for j in range(m):
                f(array[i][j + (m - 1 - 2 * j) * (i % 2)])
        ```
## 델타
- 델타를 이용한 2차원 배열 탐색
    - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
    - 인덱스 (i, j)인 칸의 상하좌우 칸(ni, nj)
        - di[] <-- [0, 1, 0, -1]
        - dj[] <-- [1, 0, -1, 0]
        - for k : 0 -> 3
            - ni <-- i + di[k]
            - ni <-- i + dj[k]
    ```python
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj
                # 언패킹을 이용해 위와 같이 작성할 수도 있다.
    ```
- 델타 응용
    - ex. N * N 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최대값(k=2)
    ```python
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for di, dj in [[0, 1], [1,0], [0, -1], [-1, 0]]:
                for c in range(1, k + 1):
                    ni, nj = i + di*c, j + dj*c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    ```
- 전치 행렬
```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]         # 서로 바꾸는 것이므로 i<j 인 조건에서 한번만 반복을 수행하면 된다.
```
- 연습문제 1
- 연습문제 2
---
## 부분집합
- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 던한 값이 0이 되는 경우가 있는지를 알아내는 문제
- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.
- 부분집합의 수
    - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개이다.
    - example. {1, 2, 3, 4}
        - 부분집합의 수 2^4 = 16
- 비트 연산자
    - & 비트 단위로 AND 연산을 한다
    - | 비트 단위로 OR 연산을 한다
    - << 피연산자의 비트 열을 왼쪽으로 이동시킨다
    - >> 피연산자의 비트 열을 오른쪽으로 이동시킨다
- << 연산자
    - 1 << n : 2^n 즉, 원소가 n개일 경우의 모든 부분집합의 수
- & 연산자
    - i & (1<<j) : i의 j번째 비트가 1인지 아닌지를 검사한다.
- 비트 연산자를 이용하여 보다 간결하게 부분집합을 생성하는 방법
    ```python
    arr = [3, 6, 7, 1, 5, 4]

    n = len(arr)

    for i in range(1<<n):                   # 부분집합의 개수
        for j in range(n):                  # 원소의 수
            if i & (1<<j):                  # i의 j번 비트가 1인 경우
                print(arr[j], end=", ")     # j번 원소 출력
        print()
    print()
    ```
- 연습문제 3
```python
arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9]

n = len(arr)

cnt = 0
for i in range(1<<n):
    sub_set = list()
    sub_sum = 0
    for j in range(n):
        if i & (1<<j):
            sub_sum += arr[j]
            sub_set.append(arr[j])
        
    if sub_sum == 0:
        cnt += 1
        print(sub_sum, sub_set, cnt)
```
---
## 검색
- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색 키(search key): 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
    - 순차 검색(sequential search)
    - 이진 검색(binary search)
    - 해쉬(hash)
### 순차 검색
- 일렬로 되어 있는 자료를 순서대로 검색하는 방법
    - 가장 간단하고 직관적
    - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용함
    - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적
    - 정렬되어 있는 경우 / 정렬되어 있지 않은 경우
- 정렬되어 있지 않은 경우
    - 검색 과정
        1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하며 찾는다
        2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다
        3. 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패
        ```python
        def sequential_search(a, n, key):
            i = 0
            while i < n and a[i]! = key:
                i += 1
            if i < n:
                return i
            else:
                return -1
        ```
- 정렬되어 있는 경우
    - 오름차순이라고 가정한다면, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 검색 종료
    ```python
    def sequentialSearch2(a, n, key):
        i = 0
        while i < n and a[i] < key:
            i += 1
        if i < n and a[i] == key:
            return i
        else:
            return -1
    ```
- 시간 복잡도
    - O(n)
---
### 이진 검색
```
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
```
- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행함
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다
- 검색과정
    1. 자료의 중앙에 있는 원소를 고른다.
    2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
    3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
    4. 찾고자 하는 값을 찾을 때까지 1~3 과정을 반복한다.
- 이진검색의 구현
    ```python
    def binarySearch(a, N, key):
        start = 0
        end = N - 1
        while start <= end:
            middle = (start + end) // 2
            if a[middle] == key:            # 검색 성공
                return middle
            elif a[middle] > key:           # 찾는 값보다 크면
                end = middle - 1            # 왼쪽 구간 선택
            else:                           # 찾는 값보다 작으면
                start = middle + 1          # 오른쪽 구간 선택
        return -1                           # 검색 실패
    ```
#### 인덱스
- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다
- Database 분야가 아닌 곳에서는 Look up table 등의 용어를 사용하기도 한다
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.
- 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.
- 데이터베이스 인덱스는 **이진 탐색 트리** 구조로 되어있다.
---
## 선택 정렬
```
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식(오름차순의 경우)
```
- 정렬 과정
    1. 주어진 리스트 중에서 최소값을 찾는다.
    2. 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
    3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.
- 시간 복잡도
    - O(n^2)
- 선택 정렬의 구현
    ```python
    def selectionSort(a, N):
        for i in range(N - 1):                      # 정렬 구간의 시작 인덱스
            min_idx = i                             # 첫 원소를 최소로 가정
            for j in range(i + 1, N):
                if a[min_idx] > a[j]:               # 최소 원소 위치 갱신
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]     # 구간 최솟값을 구간 맨 앞으로
    ```
    ```python
    # selection_sort
    a = [5, 3, 8, 1, 2]

    n = len(a)

    for i in range(n - 1):
        idx = i
        for j in range(i + 1, n):
            if a[idx] > a[j]:
                idx = j
        a[idx], a[i] = a[i], a[idx]
    print(a)            # [1, 2, 3, 5, 8]
    ```
### 셀렉션 알고리즘
```
저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법

최소값, 최대값, 중간값을 찾는 알고리즘
```
- 선택과정
    1. 정렬 알고리즘을 이용하여 자료 정렬
    2. 원하는 순서에 있는 원소 가져오기
- k번째로 작은 원소를 찾는 알고리즘
    - 1번부터 k번째까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다.
    - k가 비교적 작을 때 유용하면 O(kn)의 수행시간을 필요로 한다.
    ```python
    def select(arr, k):
        for i in range(0, k):               # k = 1 이라면, 최솟값을 찾는 알고리즘이 됨!
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_idex] = arr[min_index], arr[i]
        return arr[k - 1]
- 연습문제 4