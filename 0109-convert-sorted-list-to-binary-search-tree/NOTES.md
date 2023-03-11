### 문제정의
- 오름차순으로 정렬된 LinkedList를 입력받아서, BST로 변환하고나서 트리의 RootNode를 반환하라

### 솔루션
- 분할정복(Recursive). 인덱스로 접근가능한 선형리스트로 바꿔서, mid 값을 RootNode로 지정하고, [0:mid]를 LeftChild, [mid+1:]를 RightChild를 재귀적으로 반복하면 해결가능.

### 기록
- LinkedList를 index로 접근가능한 선형리스트로 만들면, 공간복잡도의 손해는 있으나, 시간복잡도의 이득을 볼 수 있다. 이런 문제가 2일 연속 이어지고 있다. 
- len(nums) < 1인 경우는 언제 발생하냐면, len(num) == 2일 떄, RightChild가 None이 발생하는 경우가 존재. 
### 접근과정
- 분할정복이구나. 
- 선형 리스트의 사이즈에서 중간 idx를 root로 잡고, LeftChild, RightChild의 부분문제를 풀면 되겠구나
- LinkedList로만 활용하면, 시간복잡도가 O(N^2)일 것 같은데? 
  - 인덱스화 해서 재귀함수 getAnswer()를 호출하자. 그러면 시간을 많이 아낄 수 있다.  
![image](https://user-images.githubusercontent.com/16419202/224460681-8c56496b-3fe5-483c-9521-2e51bfcef426.png)
![image](https://user-images.githubusercontent.com/16419202/224460685-dbcfe4c7-7662-4e84-a22c-ec725992c7d1.png)
