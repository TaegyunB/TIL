## DFS(깊이우선탐색)
- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면,
가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
  

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용

### DFS 알고리즘 - 재귀
~~~
DFS_Recursive(G, v)

    visited[v] <- TRUE  // v 방문 설정
    
    FOR each all w in adjacency(G, v)
        IF visited[v] != TRUE
            DFS_Recursive(G, w)
~~~

### DFS 알고리즘 - 반복
~~~
STACK s
visited[]
DFS(v)
    push(s, v)
    WHILE NOT isEmpty(s)
        v <- pop(s)
        IF NOT visited[v]
            visit(v)
            FOR each w in adjacency(v)
                IF NOT visited[w]
                    push(s, w)
~~~

