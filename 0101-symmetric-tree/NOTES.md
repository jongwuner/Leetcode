### 문제정의
- 입력된 Tree의 Root를 기준으로 Symetric한지를 반환한다. 
### 솔루션
- 왼쪽우선DFS와 오른쪽우선DFS의 탐색순서가 같은지를 확인한다.
- 대칭인지 확인하는 2개의 SubTreeNode를 가지고, 하나는 SubTreeNode의 왼쪽과, 다른 하나의 SubTreeNode의 오른쪽을 비교한다.  
### 기록
- Symetric한지는 어떤 Root기준을 중심으로 이뤄질 수 있다. Recursive한 문제가 아니다. 
- Tree 문제를 해결할 때, Recursive한지 부터 확인하는데, 선입견이 될 수 있음.  
- (문법) `if not` 그리고 여기서 and로 묶는 것
- `list`, `set` 모두 `clear()`
### 접근과정
- 3가지 아이디어
- ![image](https://user-images.githubusercontent.com/16419202/224589216-8e7291b5-b244-4f9a-89b8-af3e829060e8.png)
