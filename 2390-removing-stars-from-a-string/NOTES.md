### 문제정의
- 문자열 입력을 받았을 때, \*를 입력받으면 왼쪽에 가장 가까운 문자를 제거한다. 결과적으로 출력하게되는 문자열을 출력하시오.

### 솔루션
- O(N). 오른쪽에서 왼쪽으로 탐색하면서, \* 입력받았을 때, 그냥 cnt를 늘리고, cnt만큼 스킵하면된다. 

### 기록
- cnt >0 인 상태에서 항상 cnt =0로 만든다고 생각했는데, 이건 잘못된 생각이었다. 

### 접근과정
- 