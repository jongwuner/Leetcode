![image](https://user-images.githubusercontent.com/16419202/235164476-bb37d3d9-e18d-439b-acb2-806ac6ec7b24.png)


### 문제정의
- 여러 문자열을 List로 입력받은 후, 문자열끼리 유사하면 같은 그룹이 된다. 예를 들면, 직접적으로 문자열이 유사하지 않더라도, A문자열과 B문자열이 유사하고, A문자열과 C문자열이 유사하면, A, B, C는 하나의 그룹 내에 속한다. List 내에 몇개의 그룹이 만들어지는 지 반환하라. 
### 솔루션
- O(N^2\*M). Union-Find (Disjoint-set). 문자열의 개수 N에 대하여, N^2으로 모든 문자열들을 매칭시켜 확인한 후, 서로 유사한지를 확인한다. 이때 서로 유사하면 Merge(Union)을 해서, 최대 몇개의 독립집합이 만들어지는 지를 확인하면 된다. 
### 기록
- Union-Find 오랜만이다.
- 이 문제는 Memoization DFS, BFS로도 풀 수 있다.  
### 접근과정
- 처음에는 문제를 잘못이해했었는데, 같은 그룹에 대해 다시 읽고 알았다.
- ![image](https://user-images.githubusercontent.com/16419202/235164666-a57ab144-ca34-4f94-8e3f-2c767ae4e15e.png)
