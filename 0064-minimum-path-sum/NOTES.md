![image](https://user-images.githubusercontent.com/16419202/227845995-c6b614d1-2821-4929-8b6d-f5e1572431e0.png)

### 문제정의
- 양의 정수로만 구성되어있는 Grid가 주어졌을 때, 왼쪽상단에서 시작하여, 오른쪽과 하단으로 이동하면서, 최우하단까지 도달할 때까지 그리드 요소의 합을 구할 때, 최소값을 구하여라. 
### 솔루션
- DP. O(M\*N). 점화식은 다음과 같다.
- ![image](https://user-images.githubusercontent.com/16419202/227846513-6543683a-b71b-4777-9332-75dc64a07ef0.png)

### 기록
- 문제 제대로 읽자
- 2차원 리스트 크기 정적할당 하는 방법
  - `dp = [[0 for j in range(N)] for i in range(M)]`
### 해결과정
- 문제 잘못읽고, 그냥 윗줄, 아랫줄 더하는건줄 알았는데, 우하단으로 이동하는 DP였구나. 
