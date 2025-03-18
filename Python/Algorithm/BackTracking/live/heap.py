import heapq

arr = [20, 15, 19, 4, 13, 11]

# 1. 기본 리스트를 heap 으로 만들기
# heapq.heapify(arr)  # 최소힙으로 바뀐다.
# 디버깅 시에 이진 트리로 그림을 그려야 한다!
# -> 딱 봤을때는 정렬이 안된 것 처럼 보인다.
# print(arr)

# 2. 하나 씩 데이터를 추가
min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

# 최대힙?
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end=' ')

# ------------------ 전자사전 예제
# 1. 길이 순서로 먼저 출력
# 2. 길이가 같다면, 사전 순으로 출력

arr = ['apple', 'banana', 'kiwi', 'abcd', 'abca', 'lemon', 'peach', 'grape', 'pear']
# sort 를 쓰면 아래와 같다.
# 즉, 우선순위가 2가지
# arr.sort(key=lambda x: (len(x), x))
dictionary = []

# 단어를 삽입 (길이, 단어) 형태로 삽입
for word in arr:
    heapq.heappush(dictionary, (len(word), word))

# 전자사전에서 단어를 하나씩 꺼내기
print("전자사전 순서:")
while dictionary:
    length, word = heapq.heappop(dictionary)
    print(f"{word} (길이: {length})")
