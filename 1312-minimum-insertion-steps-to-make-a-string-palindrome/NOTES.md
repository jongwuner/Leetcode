![image](https://user-images.githubusercontent.com/16419202/233803497-080cb0cd-f4a7-4801-afb2-8c3d1d60c1aa.png)

### 문제정의
- 해당 문자열의 임의의 인덱스에 임의의 문자를 추가할 수 있다면, 펠린드롬을 만들 수 있는 최소 문자 추가 수를 구하여라.
### 솔루션
- O(N^2) by DP. 
### 기록
- 자꾸 O(N^3) DP로 헷갈리는 경우가 있다. 문자열의 길이가 6인 문제를 풀 때, [2, 4] / [3, 3] / [4, 2]의 문제는 풀 필요가 없다는 것을 이해해야한다. 
- 점화식 짜는 거에는 자신감이 붙고 있다.
- 요즘 문제 해결과정을 돌아보지 않는 악습관이 있다!! 
- 점화식 h 잡는 것이 어려웠다. 점화식에서 인덱스 혼동하는 것. 
- 점화식 k가 먼저냐, (i, j)가 먼저냐 이것도 헷갈렸었다. 
### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/233803504-395b6d9e-0f10-4736-8aca-b1135c37b624.png)
  - 그리디로 접근하기도 했었는데, 이건 문제가 있었다. 
- ![image](https://user-images.githubusercontent.com/16419202/233803508-99ea6883-e754-4fab-85ce-b6d0c4296fb2.png)
- ![image](https://user-images.githubusercontent.com/16419202/233803644-47d453fb-b550-4fdf-9182-f2252a9da0e6.png)
