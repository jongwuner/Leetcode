![image](https://user-images.githubusercontent.com/16419202/235359694-0cd48ff3-5b17-4332-8824-2869a9016c39.png)


### 문제정의
- 입력된 그래프에는 3종류의 간선이 있다. Alice만 이용할 수 있는 간선, Bob만 이용할 수 있는 간선, 둘다 이용할 수 있는 간선. Alice와 Bob이 모든 노드를 탐색할 수 있다는 전제하에 최대한 제거할 수 있는 간선의 개수를 반환하라.  
### 솔루션
- O(N + V + E). unweighted graph에서 edge를 가지고 Tree만들기 (MST의 단순화, DSU 활용)
- 둘다 이용할 수 있는 간선으로 DSU를 활용한 방식으로 Tree를 만들어서, 사이클을 만들지 않는 간선의 최대 개수를 구한다. Alice와 Bob이 모든 노드를 탐색할 수 있다는 전제하에, 최소로 필요한 간선들은 N - 1 - bluemax(둘다 이용할 수 있는 간선의 최대개수)의 값이다. 각 유형의 Total 간선 개수에서 N - 1 - blueMax를 뺀 값을 모두 합하면, 답이 된다.
- Blue를 Max로 끌어올려야, 삭제할 수 있는 간선이 많아진다. (Alice, Bob은 간선의 유형이 나눠지기 때문에) 이것은 항상 타당한 논리다. 
### 기록
- 그래프는 [방향성 유무 / 가중치 여부 / 사이클 유무](https://github.com/jongwuner/Leetcode/blob/main/1697-checking-existence-of-edge-length-limited-paths/NOTES.md)에 따라서 알고리즘을 정리해놔야한다. 
- 유니온파인드의자신감을 많이 쌓았음. 
### 접근과정
- 처음에는 Adj 자료구조를 여러개 만들어야하나? 라는 생각을 했었다. 그리고 트리를 만드는 방식을 DFS Tree로 생각했었는데, MST 만드는 과정에서 DSU를 활용하는 방식을 떠올린 것이 유효했던 것 같다. 이렇게 트리를 만들 수 있다는 것도 하나 배웠던 문제였다. 
- ![image](https://user-images.githubusercontent.com/16419202/235360173-4857a539-06fb-4351-a629-528067f5d688.png)
- ![image](https://user-images.githubusercontent.com/16419202/235360183-da534715-f8a2-45da-9a53-8f228e37abfe.png)
- ![image](https://user-images.githubusercontent.com/16419202/235360192-ca5031e2-416b-4e91-af37-9718eecda9e0.png)
