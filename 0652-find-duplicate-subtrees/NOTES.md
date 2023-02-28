### 문제정의 
- 해당 Tree에서 Duplicate Tree의 Root들을 모두 추출해라.

### 솔루션
- PostOrder 순회로 해결하는 문제. logN으로 삽입, 조회할 수 있는 자료구조가 필요하다. 매 노드마다 Root, LS, RS를 활용하여, 같은 Root, LS, RS 상태가 있었는지를 조회하며(logN), 이전에 없었던 Root, LS, RS 상태라면 새롭게 삽입해준다. (logN). PostOrder 한번 x 2 x logN이므로 O(NlogN)으로 해결 가능.  

### 메모
- 리트코드의 톤앤매너. 문제에서 Root 만 반환하면 된다고 했는데, TC에는 그렇게 쓰여있지 않아서 허송시간을 보냈다. 이것때문에 늦어짐. [2,4], [4]
- O(N^N)으로 접근을 했다. 매 Node에서 문자열을 비교하겠다는 거였는데, 그것보다 훨씬 쉬운 방법이 있었다. 'LS + RS + 자기자신' 문자열로 바꿔서, logN으로 존재 유무를 조회할 수 있는 자료구조에다가 저장하는 것이 합리적이다. 결과적으로는 O(NlogN). 

### 접근과정
- LCA(최소 공통 조상)이라는 생각을 했다. 자기 자신의 Subtree에서는 자신과 Duplicate Tree가 있을 수 없기 때문이다. 
![image](https://user-images.githubusercontent.com/16419202/221883110-0b8314c8-13d0-4ded-bcc6-633209104d56.png)

- 답이 한쪽의 Subtree에 다 있는 경우, 양쪽의 Subtree에 다 있는 경우, 답이 없는 경우로 나눠서 푸는 분할정복이라는 생각을 했었다. 이때부터 PosstOrder라는 확신을 가졌다. 
![image](https://user-images.githubusercontent.com/16419202/221883480-6135ab6f-8b26-4bc9-8a44-85d46cbcc454.png)

- PostOrder을 하면 그냥 트리 형태를 알 수 있지 않겠는가. 라는 가설을 듣고 납득이 되었다. 빈칸에는 NULL값을 넣고, 완전트리로 만들면 된다. 
![image](https://user-images.githubusercontent.com/16419202/221883726-4e9b759f-29b3-422e-ab30-9e924862b9e2.png)

- (★) PostOrder를 하고, 문자열을 비교해주면 되겠다고 생각했는데, 이것보다 더 효과적인 것은 Python 상에서 Counter, Dict 등을 사용하는 것이 훨씬 좋은 접근이었다. Key값으로 조회할 때 logN에 접근 가능. 이 과정에서 O(N) 만에 문자열을 비교하는 것에 미련을 버리지 못했다.  
