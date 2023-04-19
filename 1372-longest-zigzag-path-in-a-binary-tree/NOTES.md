
![image](https://user-images.githubusercontent.com/16419202/233144684-4a59c442-1214-4c44-aa9c-c6b8f3ea388c.png)


### 문제정의
- 이진트리에서 최대 지그재그(좌-서브트리 노드에서 우-서브트리 노드 or 우-서브트리 노드에서 좌-서브트리) 구간의 길이(2개 노드를 잇는 간선 1개의 개수)를 반환하시오
### 솔루션
- O(N). 이진트리를 방문할 때마다, 해당 노드에서 부모로부터 좌우 어디쪽 노드였는지, 그리고 자식노드 좌우 어느쪽 노드였는지를 확인하고 max값을 갱신해서 반환하면 된다. 
### 기록
- ★ 반드시 다시 풀어볼 것. 리트코드 연결리스트 톤앤매너 적응 못한 문제 
### 접근과정
- 첫 접근방식으로 제대로는 풀다 말았는데, 왜 Leetcode 통과가 안됐는지는 확인해볼 필요가 있음.
  - 문제 첫번쨰 TC 통과안된 이유.
  - ```python
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def __init__(self):
            self.ans = 0
        def treeOrder(self, nowNode, record, opt):
            if nowNode is None:
                return

            self.ans = max(self.ans, record)

            if nowNode.left:
                if opt == 0: # 현재 노드는 부모의 왼쪽 자식이다.
                    self.treeOrder(nowNode.left, 1, 0)
                elif opt == 1: #부모의 오른쪽 자식
                    self.treeOrder(nowNode.left, record + 1, 0)
                else:
                    self.treeOrder(nowNode.left, record + 1, 0)

            if nowNode.right:
                if opt == 0: # 현재 노드는 부모의 왼쪽 자식
                    self.treeOrder(nowNode.right, record + 1, 1)
                elif opt == 1: #부모의 오른쪽 자식
                    self.treeOrder(nowNode.right, 1, 1)
                else:
                    self.treeOrder(nowNode.left, record + 1, 1)


        def longestZigZag(self, root: Optional[TreeNode]) -> int:
            self.treeOrder(root, 0, -1)
            return self.ans
    ```
