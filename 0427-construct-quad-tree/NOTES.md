### 문제정의

전형적인 쿼드트리 문제다. Class 형식의 Node 인스턴스에다가 조건에 맞는 변수들을 입력하면 된다.  

### 솔루션

분할정복 쿼드트리다. 길이가 짧아서 O(N^2)으로 리프노드인지, 아닌지를 판단해도 아무런 문제가 되지 않는다. 리프노드가 아닌 것을 발견한 즉시, 4개의 분할문제로 쪼개면 된다. 

### 메모
- 문제 자체는 어렵지 않았다. 
- 시작점(y,x)와 length만 알면 풀 수 있었던 문제, (y1, x1), (y2, x2) 2개로 Recursion 하는 것보다 훨씬 단순하고 쉽다. 
- 리트코드 문제들의 톤앤매너가 헷갈렸던 문제. (Class Node는 조작가능하지 않다. level order, TC에 왜 NULL이 4개인지 이해가 안가서...)
- 그냥 Root 반환만 하면 됐던 문제다. 채점기가 알아서 순차적으로 돌면서 판단한다. (?) 

### 접근과정

![image](https://user-images.githubusercontent.com/16419202/221602979-4fe1a04b-6235-4afa-aeed-e05b62fe0c30.png)

![image](https://user-images.githubusercontent.com/16419202/221603855-938fc61d-b3c2-440d-a49b-ed1837dee52c.png)
