### 문제정의
- 이진트리의 root를 입력받고, 완전 이진 트리인지를 반환하라 
### 솔루션
- 트리 그래프를 BFS탐색으로 List 형태로 변환한 후, 그 List를 통해 완전 이진 트리인지 확인한다.  
### 기록
- 완전 이진 트리는 List 상에서 element가 존재하는 경우, 사이사이 값에 None 값이 없다.
- queue 사용하기 가장 쉬운 라이브러리
```python
from collections import deque

que = deque()
que.append()  # back 삽입
que.popleft() # front 삭제
que.appendleft() # front 삽입
que.pop() # back 삭제
```
### 접근과정
- preOrder 방식으로 접근할 수 있을거라 생각했는데, 탐색 순서가 DFS로 되어서, 너비 우선 탐색으로 하는 게 유일하다고 생각했다. 
