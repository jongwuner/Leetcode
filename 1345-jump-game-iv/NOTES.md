### 문제정의
- 0 인덱스에서 시작하여 N-1에 최단 경로로 도달하라. 
- 인덱스 i에서 i+1, i-1로 이동할 수 있으며, arr[i] == arr[j]인 j로 이동할 수 있다.

### 솔루션
- BFS
- 같은 value의 해시테이블은 딱 한번만 조회하면 되기 때문에, O(V^2) -> O(V)로 최적화가 가능한 문제.

### 메모
- 그리드그래프에서의 E는 O(N^2)개수가 맞다. 

### 접근과정
- 보자마자 BFS 같긴 했는데, O(V+E)의 시간복잡도가 현재 자료구조에서는 O(N^2)인지, O(N)인지가 헷갈렸다. 
- E개수로 치자면 O(N^2)가 맞긴한데, 이 E를 모두 볼 필요가 없어지거나, 안보게끔 소거하는 방법을 떠올리는 게 좀 오래걸렸다. 그래서 다른 알고리즘들을 생각했다. 
- 그래서 슬라이딩윈도우와 DP를 생각 했다. 해당 idx까지 도달하는 최소 길이를 저장하는 그런 메모이제이션을 생각했으나, 현재 조회하고 있는 idx보다 작은 idx값에도 업데이트를 해줘야한다는 것 때문에 슬라이딩윈도우는 아니라는 생각을 했고, DP는 부분문제를 탐색하는 개수가 일정하지 않다는 것 때문에 아니라는 것을 깨달았다.  
- Priority Queue를 N개 활용하는 생각도 했었는데, 항상 최솟값 하나만 보면 되기 때문에 아니라는 생각이 들었다. 
- 다익스트라도 잠시 떠올렸던 것 같다. 처음엔 다익스트라 일리가 없다고 생각했었던 이유는 Jump를 할 때, 항상 1의 가중치가 소모되기 때문이다. 모든 E의 가중치가 1일 때 최단경로를 구하는 알고리즘은 BFS다. 하지만 현재 idx에서 Jump하게 되는 idx의 길이를 가중치라고 생각했다. 이건 완전히 순간적으로 범했던 오류다.   
![image](https://user-images.githubusercontent.com/16419202/222956772-2ee993e2-ac5f-4f2e-9b29-fba8aceea687.png)

- 에지의 개수는 최대 O(V^2)이지만, 여기서 같은 가중치 끼리 이동하는 E는 value값을 최초에 탐색할 때, 딱 한번만 보면 된다. 그래서 O(V)로 탐색을 할 수 있게 된다. 
![image](https://user-images.githubusercontent.com/16419202/222956782-3084674f-89f7-4953-ae9c-c97312a53174.png)
![image](https://user-images.githubusercontent.com/16419202/222956786-217338d5-2314-4556-885a-2c633a0b674a.png)

