![image](https://user-images.githubusercontent.com/16419202/235305052-7a05301a-138a-483a-8c88-35200d31599b.png)


### 문제정의
- edge와 queries 리스트를 입력받았을 때, queries 리스트에 입력받은 경로가 가능한지 True/False로 반환하라.
### 솔루션
- O(NlogN + MlogM + N + M). Union-Find + HashTable. 
- queries와 edges를 오름차순으로 정렬한 다음에, queries와 edges를 투포인터로 완전탐색한다. queries의 edge보다 작은 edges들(from, to)를 모두 merge시키면서, query에서의 from, to 정점이 같은 독립집합 내에 속하는 지를 확인한다. 그것이 True/False로 저장되는데, queries가 오름차순으로 정렬하면서 origin order를 해시테이블(Set, defaultdict(list))로 보존해둬야한다
### 기록
- 유니온파인드는 DFS/BFS로 해결할 수 있다. 연결요소의 DFS문제는 거의 모두 Union-Find로도 풀 수 있겠구나. 
- 이 문제는 MST로도 접근이 가능할 것 같다. MST(Minimum-Spanning Tree) 공부를 해두자. 
- 그래프 문제에서 아이디어 발상이 되지 않을 때, 오늘 했던 접근이 괜찮았다. 
  - BFS / DFS
  - Dijkstra, Bellman-Ford, Floyd-warshall
  - MST (Tree)
  - Union-Find
  - 위상정렬
  - SFPA (?)
- List를 Key로 활용하기 위해서는 table[tuple(List)]
- 정렬 `arr = sorted(arr, key=lambda arr: arr[0])`
- defaultdict(list)는 리스트 형태로 value, defaultdict(int)는 Counter를 모두 대체가능
### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/235305344-0aaaa99e-6ac2-46d0-a755-6eb022b32f25.png)
  - 처음에는 다익스트라, 혹은 메모이제이션을 활용한 DFS/BFS인줄 알았는데 도저히 시간복잡도가 나오지 않았다. 
  - 위상정렬인가도 싶었는데, 방향이 없는 그래프여서 의미가 없다고 생각했다. 
  - 아무리 봐도, 다익스트라, 벨만포드면 시작점이 정해져야할텐데. 하지만 벨만포드는 음의 사이클 요소가 아예 등장하지 않았기 때문에 벨만포드는 아닐거라 생각했다. 
- ![image](https://user-images.githubusercontent.com/16419202/235305349-68a3ced5-0c45-4864-b49d-e2b592303037.png)
  - 그래서 그래프 관련 알고리즘을 모조리 적어보기 시작했다. 
  - 최종적으로 Union-Find나 MST가 아닐까 했는데, Union-Find로 가능한 것 같았다.
- ![image](https://user-images.githubusercontent.com/16419202/235305358-dfd0a890-d03a-4608-998b-2f2311d6603c.png)
  - 그래서 투포인터의 방식으로 완전탐색을 하면 가능한 것 같긴 했다. 알고리즘을 설계해봤다. 해결할 수 있었다. 
