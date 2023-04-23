![image](https://user-images.githubusercontent.com/16419202/233829756-5e8b804d-ec48-4bda-b269-cd92f54591ec.png)


### 문제정의
- s와 k가 주어질 때, s를 ,로 split하여 k이하인 수로 구성된 배열들로 나눌 수 있는 경우의 수를 구하여라.
### 솔루션
- O(N). DFS using memoization. [s, e] 구간을 부분문제로 나눌 때, i에 대한 루프로 [s, s+i] / [s+i+1, e]로 나눠서 해결하면 된다.    
### 기록
- Top-Down DP 방식으로 잘 안보였던 이유는?
- 이것을 Bottom-up으로 해결하려면 어떻게 해야하나?
- Queue로는 답이 왜 안되는 걸까?
- 이 문제는 왜 수학으로 풀지 못할까?
### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/233829925-f90fafd2-1d56-4b7e-a1be-7c67fccdf61b.png)
  - 처음에는 조합 수로 생각했다. 그런데 이제 여기서 깨달아야하는 건, 이걸로 풀릴리가 없다는 생각도 하면 좋을 것 같다. 예외와 조건이 있으니까.. 그리고 수학으로 먼저 접근해보는 건 Top-down 방식의 풀이이다. 
- ![image](https://user-images.githubusercontent.com/16419202/233829935-072ed9f3-64ea-4a61-8bb1-933ac8db59e9.png)
  - 수학이 아니라는 것을 깨닫고, 어떻게 풀 수 있을까? 비트마스크? 상태보존을 어떻게 하지? 길이가 10^9만큼인데,,,, 이걸 무슨 수로 할 수 있지. 다른 자료구조가 가능한가?
  - DFS를 떠올리긴 했는데, 시간복잡도 계산을 할줄을 몰랐어서 어려웠다. 거의 다 O(N)에 끝낼 수 있는 것이 Memoization DP이다. 이 뉘앙스를 설명할 수 있어야한다.
- ![image](https://user-images.githubusercontent.com/16419202/233829949-38c4e00d-a301-4dd0-8c25-3949d54a7d0a.png)
  - O(NlogN) 이나 O(N)인데, 여기서 쓸 수 있는 자료구조나 알고리즘 풀이 방식은 무엇일까? 구간DP는 최소 O(N^2), Stack? Queue? PQ? BST? 이런 게 바로바로 떠오를 수 있을 정도로 공부해두어야 한다. 
- ![image](https://user-images.githubusercontent.com/16419202/233829965-55f12a31-5f3c-4540-999e-5f05132171d6.png)
  - Queue로도 한번 시도해봤는데, 답이 보이지 않았다. 
- ![image](https://user-images.githubusercontent.com/16419202/233829974-d3bb2af0-f10d-449c-8e70-0cdd52ee619c.png)
  - Top-down DP라는 것을 깨달았다. 
