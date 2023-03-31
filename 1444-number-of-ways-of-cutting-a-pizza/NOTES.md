### 문제정의
- pizza 문자열 리스트가 주어질 때, 이것을 k의 조각으로 썰 수 있는 방법의 개수를 구하여라. 단, 피자를 썰 때, 조각마다 최소 1개 이상의 피자가 있어야 한다.  
### 솔루션
- Top-down DP, Memoization. O(N^4). 해당 피자 리스트에 존재하는 피자들을 모두 확인하면서, 가장 왼쪽 상단에 피자를 기준으로, 우측, 하단에 있는 피자를 만날 때마다, 좌상단 경계로 피자판을 짜름으로써, 2개의 부분문제로 나눠서 해결한다. 기저는 피자판에 피자 1조각 이하로 존재하는 경우이다.
(0을 반환)

### 기록
- 메모이제이션 DP 시간복잡도 계산은 왜 항상 어려운걸까. [비슷한 문제](https://github.com/jongwuner/Leetcode/tree/main/0087-scramble-string)
- 함수 인자를 정의할 때, 튜플도 하나의 변수일 뿐. 호출에서 튜플을 인자로 전달하면 정해지는 것이다. 
### 접근과정 
- ![image](https://user-images.githubusercontent.com/16419202/229206599-6bd69654-2908-4e88-b461-00a0dcd5c644.png)
  - 어떻게 가운데에 있는 것을을 처리하지? 라는생각을 했던 것 같다. 
  - ey,ex의 위치에 대해서 헷갈렸던 것 같다. 
- ![image](https://user-images.githubusercontent.com/16419202/229206635-acb7c7f2-5b6f-4f46-859c-44df8577c82a.png)
- ![image](https://user-images.githubusercontent.com/16419202/229206653-8cf653b4-9fd0-4f62-89bf-142900ba5a3e.png)
  - ![image](https://user-images.githubusercontent.com/16419202/229208574-179957bc-e4d5-40d4-87e2-ab2c2f97f4a5.png)
  - 재귀로 호출해버리면, 재귀트리 상에서 자식노드가 되는데, 자식노드들 간에는 데이터를 주고받기가 어렵다. 그래서 부모노드에서만이 알 수 있는 경우가 있는데, 이 문제가 딱 그랬다. 이것을 활용해서 재귀트리와 기저를 설계해야겠다. 
