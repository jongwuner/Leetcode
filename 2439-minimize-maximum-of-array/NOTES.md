![image](https://user-images.githubusercontent.com/16419202/230154947-5add4d65-4615-47bb-95f6-312c4a344f9e.png)
![image](https://user-images.githubusercontent.com/16419202/230154870-482aef61-e156-47a4-83d6-6c8cec70e4f8.png)


### 문제정의
- 임의 리스트에서 list[i]에서 -1을 하고, list[i-1]에서는 +1을 하게 된다. 그랬을 때, 이 리스트 전체의 max값을 최소화한 그 max값을 구하라.
### 솔루션
- O(N). Greedy + Math. 누적합을 가지고 수학적 계산으로 해결할 수 있는데, 거시적으로 보면 이 리스트에서는 오른쪽에서 왼쪽으로 값들을 넘겨줄 수가 있다. 그래서 nums[i]값이 최대값보다 크다면, 1차적으로 넘겨줄 수 있는 조건이 되며, 현재까지의 sum // idx의 값이 max보다도 더 클 때 확실히 넘겨줄 수 있게 된다.   
### 기록
- 부분문제로 접근하는 과정이 좋았다. 그 과정에서 Greedy임을 알게 된다. 
- PQ 안되는 이유. 명확하게. 
### 접근과정
- Bottom-up 부분문제로 접근하다가, Priroty Queue 최소힙, 최대힙 2개 쓰는 거 생각하다가, 시간복잡도 적으로 최악의 경우를 발견하고, 그것을 누적합으로 해결할 수 있지 않을까 하는 생각에 접근하게 되었다.  

![image](https://user-images.githubusercontent.com/16419202/230158344-227fddfa-ee82-4e60-a286-adbb8349c919.png)
