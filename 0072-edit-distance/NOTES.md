## 문제정의

문자열 2개. word1, word2를 입력받아서, 문자열 1에서 3가지 연산을 거듭하여, 문자열 2와 같게 만드는 문제다. 

1) Insert : 문자열 1에 문자 1개를 임의의 인덱스에 삽입할 수 있다.
2) Delete : 문자열 1에 있는 임의의 문자를 1개 삭제할 수 있다. 
3) Replace : 문자열 1에 있는 문자 1개를 다른 문자로 대체할 수 있다. 

## 솔루션

DP[i][j] 점화식:
1) (word1[i][j] == word2[i][j] 일 경우) dp[i-1][j-1]
2) (word1[i][j] != word2[i][j] 일 경우) min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1 [insert, delete, replace 중 하나]

## 메모
- 직관적인 아이디어를 잘 발견했는데, 알고리즘으로 만들기까지가 어려웠던 그 과정을 기억해야한다. (LCS를 좀 더 잘 정리해뒀다면 수월했을 것이다.)
- LCS(Longest-Common Sequence)가 떠올랐다. LCS에서는 공통 문자를 만났을 때를 기준으로 DP테이블에 값이 더해지는데, 이 문제에서는 문자가 달랐을 때 값이 더해진다. 
- LCS는 문자열 2개를 활용하여, 2차원 DP테이블을 활용한다. 이정도만 기억해둬도 괜찮을 것 같다.  
- DP점화식이 정형화되어있는 문제들이 이렇게 변형될 수가 있다는 것을 배웠다. 

## 접근과정


- 직관적으로 접근했을 때, LCS와 닮아있다는 아이디어를 떠올랐다. LCS 중 하나를 찾았을 때, 간격에 있는 최장 문자열을 더하면 그것이 답이 된다고 생각을 했다. 하지만, 길이는 같더라도 어떤 LCS를 찾느냐에 따라 답이 달라져서 해맸다.

![image](https://user-images.githubusercontent.com/16419202/221390582-c65a76e9-6ce3-4cc2-9a3b-b751d2fc0ed8.png)

- 여러가지 반례를 만들어보고자 했다. horse, ros의 사례가 중요했는데, LCS를 rs로 잡느냐, os로 잡느냐 답이 달라지는 것을 발견하여, LCS가 여러개의 경우로 나오는 TC를 만드려고 했다.  

![image](https://user-images.githubusercontent.com/16419202/221390586-4b332e20-94fe-4f86-8bf6-1aa85eaaf272.png)

![image](https://user-images.githubusercontent.com/16419202/221390589-c3faad26-43b3-45c5-8e7b-32d841955139.png)
- LCS의 DP를 찾아가는 과정과 상당히 닮아있다. LCS는 2차원 DP테이블을 활용하여, word1[i][j] == word2[i][j]일 경우에 +1을 하지만, 이 문제에서는 반대다. word1[i][j] != word2[i][j]의 경우에 +1를 해주는 방식으로 점화식을 구성할 수가 있었다. 
![image](https://user-images.githubusercontent.com/16419202/221390592-a5f525de-605d-419f-a4e6-daa825e2425f.png)

![image](https://user-images.githubusercontent.com/16419202/221390597-543cfe60-f681-40ca-aab0-ced355012b8c.png)

