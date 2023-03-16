### 문제정의
- 임의 트리의 preorder와 inorder의 순서를 리스트로 입력받았을 때, 원본 트리를 만들고, 트리의 root를 반환하라 
### 솔루션
- preorder와 postorder를 통해 root를 찾아내고, 그 root가 존재하는 선형 리스트상의 idx를 inorder에서 찾으면, leftSubtree와 rightSubtree의 개수를 알아낼 수 있다. 이것을 재귀적으로 반복하면, 원본트리를 형성할 수 있다. 
- 실전에서도 솔루션을 내가 글로 정리하는 습관.  
### 기록
- 인덱스가 혼동될 때는 오늘처럼 글로 정리하고, 예시를 들어보자. 
- preorder(맨앞)와 postorder(맨뒤)는 root의 위치가 항상 똑같구나. 
- preorder와 postorder를 통해 root가 뭔지를 알아낼 수 있다면, inorder는 leftTree와 RightTree를 나눠줄 수 있구나.
- 혹시 preorder와 postorder를 알 때, 알아낼 수 있는게 있을까?
- inorder로 left와 right의 개수만 알아내면 되는구나. 그러면 pre와 post에서도 leftTree와 rightTree의 개수는 달라질 수가 없구나.
- Tree는 사이클이 없기 때문에, 부분문제가 반복될리 없고, 분할정복의 응용으로 엄청 많이 활용되겠구나. 
- Graph는 사이클이 있고, 중복적으로 방문을 할 수 있게 되기 때문에 DP랑 함께 응용이 많이 되겠구나.   
### 접근과정
- [비슷한 문제네?](https://github.com/jongwuner/Leetcode/tree/main/0106-construct-binary-tree-from-inorder-and-postorder-traversal)
- preorder는 root가 항상 preorder[0]에 존재하면 똑같구나. 
