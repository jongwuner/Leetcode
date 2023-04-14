![image](https://user-images.githubusercontent.com/16419202/232037811-b438aaf6-3810-472a-bd94-810adb642082.png)


### 문제정의
- 문자열을 입력받을 때, 순서를 보존한 상태에서 문자를 일부 제거한 Subsequence 중 최대 펠린드롬의 길이를 구하라. 
 
### 솔루션
- O(N^2). Bottom-Up DP. 
- DP[i][j] => (s[i] != s[j] 일 경우) max(DP[i+1][j], DP[i][j-1])
           => (s[i] == s[j] 일 경우) max(DP[i][j], DP[i+1][j-1] + 2)

### 기록
- O(N^3)으로 착각했던 이유. 길이마다 DP[i][j] = DP[i][k], DP[i][N-1-K] (0<=k<=N-1)

### 접근과정
- O(N^3)이었다가, O(N^2)만으로 최적화가 된다는 것을 꺠달음. 모든 구간을 볼 필요가 없다는 것을 깨달음. 

![image](https://user-images.githubusercontent.com/16419202/232040050-cd4343b7-f4be-4b9e-8914-f7ca41f3c65c.png)
![image](https://user-images.githubusercontent.com/16419202/232040071-874cbe73-bc46-46e3-a394-1b4230428969.png)
