## 검색
- 데이터 구조 안에서 특정한 값을 빠르고 효율적으로 찾기 위해 사용되는 알고리즘
- 데이터 베이스에서 원하는 정보를 찾을 때
- 특정한 값(아이템)이 배열 또는 리스트에 존재하는지를 확인할 때
- 그래프에서 특정 노드에 도달 가능한지를 탐색할 때

### 검색의 종류
- 선형 검색(Linear Search) / 순차 검색(Sequential Search)
- 이진 검색(Binary Search)
- 인덱싱(Indexing)
- 탐색(DFS, BFS)
- ...

### 순차 검색(Sequential Search)
- 앞에서부터 자료를 순서대로 검색하는 방법
- 가장 간단하고 직관적인 검색 방법
- 배열이나 연결 리스트 등 순차 구조로 구현된 자료구조에서 원하는 값을 찾을 때 유용함
- 구현은 간단하지만 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적임
- 정렬 여부와 관계없이 적용가능 함

### 순차 검색(Sequential Search): 정렬 X
- 첫 번째 원소부터 순서대로 검색
- 해당 원소와 키 값이 일치하는지 비교하여 일치하면 해당 위치 반환
- 자료구조의 마지막에 도달할 때 까지 키 값을 찾지 못하면 검색 실패
- 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정됨
- 첫 번째 위치에서 원소를 찾으면 1번 비교, 두 번째 위치에서 원소를 찾으면 2번 비교, ...
- 정렬되지 않은 자료구조에서 순차 검색의 평균 비교 횟수
    -> 1/n * (1 + 2 + 3 + ... + n) = (n+1) / 2
- 시간 복잡도: O(n)

#### 의사 코드 예시
~~~Java
// a: 1차원 배열, n: 배열의 크기, key: 찾고 싶은 값
sequentialSearch(int[] a, int n, int key)
    i <- 0
    while (i < n and a[i] != key)
        i <- i + 1;
    if (i < n) return i;
    else return -1;
~~~

### 순차 검색(Sequential Search): 정렬 O
- 자료가 오름차순으로 정렬된 상태라고 가정
- 첫 번째 원소부터 순서대로 검색
- 해당 원소와 키 값이 일치하는지 비교하여 일치하면 해당 위치 반환
- 해당 원소의 값이 키 값보다 크다면 찾는 원소가 없다는 것이므로 검색 종료
- 찾고자 하는 원소의 순서에 따라 비교 횟수가 결정됨
- 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듬
- 시간 복잡도: O(n)

#### 의사 코드 예시
~~~Java
//a: 1차원 배열, n: 배열의 크기, key: 찾고 싶은 값
sequentialSearch2(int[] a, int n, int key)
    for i in range from 0 to n-1:
        if a[i] == key: return i;
        else if a[i] > key: break;
    return -1
~~~

### 이진 검색(Binary Search)
- 키 값을 찾을 때까지 데이터의 범위를 절반씩 줄이면서 검색하는 방식
- 자료가 정렬된(오름차순, 내림차순) 상태여야 함
- 시간 복잡도: O(log n)

### 구현 방법
1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료 구간의 범위를 왼쪽으로 축소
   목표 값이 중앙 원소의 값보다 크다면 자료 구간의 범위를 오른쪽으로 축소
4. 찾고자 하는 값을 찾을 때까지 1~3의 과정을 반복한다.

### 반복문을 이용한 구현
- 검색 범위의 시작점과 종료점을 이용하여 검색을 반복 수행
- 자료의 삽입이나 삭제가 발생했을 때 배열의 상태를 항상 정렬된 상태로 유지해야 함
~~~Java
binarySearch(int[] a, int key)
    left <- 0;
    right <- length(a)-1;
    while (left <= right) {
        mid = (left + right) / 2;
        if (a[mid] == key) return true;  // 검색 성공
        else if (a[mid] > key) right = mid - 1;  // 왼쪽
        else left = mid + 1;  // 오른쪽
    }
    return false;  // 검색 실패
~~~

### 재귀함수를 이용한 구현
~~~Java
binarySearch2(int[] a, int left, int right, int key) :
    if (left > right) return false;  // 검색 실패

    mid = (left + right) / 2;
    if (key == a[mid]) return true  // 검색 성공
    else if (key < a[mid])  // 왼쪽
        return binarySearch2(a, left, mid-1, key)
    else if (key > a[mid])  // 오른쪽
        return binarySearch2(a, mid+1, right, key)
~~~