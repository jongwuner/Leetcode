### 문제정의
### 솔루션
- 분할정복. postorder List를 통해, root를 찾고, 그 root를 inorder List에서 idx를 찾을 수 있다. inorder List 좌 우의 subList가 결국 트리 상에서의 Subtree가 된다. subtree들의 개수를 알면, postorder에서의 subtree 순서와 동일하다. leftsubtree와 rightsubtree를 분할정복하면 된다. 
### 기록
### 접근과정
- index가 헷갈릴 것 같아서, 글로 알고리즘을 정리하였음. 
  - def divideLR(inorder, postorder):
    ## postorder의 마지막 값이 항상 루트다. answer에 삽입하고,
    ## inorder에서 인덱스를 찾고, Lsubtree(5), Rsubtree(4) 개수를 파악해서, 
    ## inorder에서는 [0:rootIdx], [rootIdx+1:]
    ## postorder에서 [0:Lsubtree개수]를 postorder [5:-1]를 postorder. 항상 2개씩
    ## 그 후, 재귀탐색한다.
![image](https://user-images.githubusercontent.com/16419202/225495347-836a57b3-9570-4167-bafe-810566be178e.png)
![image](https://user-images.githubusercontent.com/16419202/225495361-41a8b287-1ed3-41a1-9915-79f0904b4473.png)
- 문제잘못읽어서 시간이 오래걸림(60) TreeNode반환하면 채점기가 알아서 BFS탐색하는건데, 반환도 NumArray로 하는 줄 알았음. 
![image](https://user-images.githubusercontent.com/16419202/225495370-5ac69c08-a00b-4f76-af57-8b23e6227991.png)
