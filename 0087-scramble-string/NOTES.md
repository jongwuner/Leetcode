다시 꼭 복습해볼 문제.

### 문제정의
- 문자열 2개를 입력받았을 때, 다음의 규칙으로 변형될 수 있는 문자열인지를 반환하라. (True or False). 문자열의 어떤 요소를 기준으로 slice를 할 수 있으며, slice된 2개의 구간은 서로 순서를 바꿀 수 있다. 이 작업은 재귀적으로 진행될 수 있다. 
### 솔루션
- DP by Memoization. 
### 기록
- 분할정복인데, 부분문제가 반복될 수 있는 경우, Top-down DP처럼 Memoization을 도입하라.
- 부분문제가 반복되지 않을 것 같다는 생각을 버리지 못했는데, 부분문제가 어떤 식으로 반복될 수 있는 것일까?  
- 시간복잡도 짜는게 상당히 어려웠다고 느꼈던 문제다. 
### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/228937462-87c0c2e8-1992-4735-a99d-7181613ef0ec.png)
- ![image](https://user-images.githubusercontent.com/16419202/228937612-58d1fbcb-98e2-498c-940b-86d21b6f593f.png)
- ![image](https://user-images.githubusercontent.com/16419202/228937633-e3d496e3-6ce6-452b-adfa-2601445c0792.png)
