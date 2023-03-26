### 문제정의
- 정점마다 outEdge가 최대 1개씩 있는 방향 그래프에 대해서 가장 큰 사이클의 길이를 반환하라
### 솔루션
- DFS. O(N). 각 정점에서 Backedge를 찾았을 때, 방문시간(times)의 차를 구하면 사이클의 길이를 알 수 있다.  
### 기록
- 스패닝트리, DFS 스패닝트리, 최소 스패닝트리의 개념 공부를 다시 한번 해야할 것 같다.
- 4가지 간선에 대해서 정리했다. 
  - ![image](https://user-images.githubusercontent.com/16419202/227760485-3ee84daf-1190-4b92-9bf3-5519ef3bb0c9.png)
- BFS로는 왜 사이클을 찾을 수 없는것일까? 
- (★) 내가 문제 풀다가 헷갈려서 시간이 오래걸렸던 부분들 (아직 미제 내용들이 좀 있음)
  - 방문을 할 때마다, Stack에다가 넣으면 된다. 
  - 어떤 노드에 방문할 때, visited == True & finished == False인 게 있다. 발견을 하면, finished를 True로 만들어주는 노드를 종료할 때, 뭔가 여기서 해줄 수 있는 mark를 해줘야한다.  
  - 방문을 종료할 때, Finished = True를 해주고, stack pop을 해서 본인 curr이 나올 때까지 pop을 해야하며, 그 사이즈를 기록해야한다. 
  - 근데 이걸 계속 반복하는 게 맞을까? 사이클이 자기 자신을호부터 시작되는 게 여러 개일 때는 어떻게 하는 걸까? 
  - Stack에다가 pop했던 것을 다시 push 해야하는 상황은 없는걸까?
  - 종료되는 순서가 어떻게 되는걸까?
  - 근데 이렇게 하면 짜잘짜잘한 모든 사이클의 개수까지는 모르지 않나?
  - 정말 모든 사이클 개수를 찾으려면 BFS를 해야하지 않을까? BFS로도 사이클을 찾을 수 있을까? 이 알고리즘으로 하는 걸 본 적은 없다. 하지만 생각을 한번 해보긴 해야한다. 공부해봐야하긴 하겠다.  
  - 사이클의 최대 깊이를 찾으려면 DFS를 해야하지 않을까? 
- (★) 왜 [3, 3, 4, 2, 5, 3, 3, 8, 9, -1] 답이 4지? 6아닌가? 
  - ![image](https://user-images.githubusercontent.com/16419202/227760768-62a0494a-597d-4d1d-912d-3e095c6b30f0.png)
- 그래프 응용에서 사이클은 무조건 많이 나오겠구나. 공부해둬야겠다. 
  - https://www.acmicpc.net/problem/16724
  - https://www.acmicpc.net/problem/9466
  - https://nicotina04.tistory.com/148

### 접근과정
- backedge 개념이 잘 떠오르지 않았다. 사이클을 볼 때는 backedge만 보면 된다. 
- 처음에 이게 기억이 잘 안났다. backedge만 보면 되는 건 기억이 나서, 좀 더 자세히 공부를 먼저하려고 알고리즘설계 노트를 바로 한번 봤다.
- 사이클 관련 공부하다가, 아예 Edge관련 모든 걸 공부하려다보니, 공부가 목적을 잃고 너무 확장되서 시간이 오래걸렸다. 
![image](https://user-images.githubusercontent.com/16419202/227760240-8df814f1-25c3-4c0d-9ab3-2253c8cb5af1.png)
![image](https://user-images.githubusercontent.com/16419202/227760241-69d9d27d-2c2f-45c0-b090-0febea363bbc.png)
- 근데 outEdge가 1개 밖에 없어서 그렇게 어려운 문제가 아니었다. 
![image](https://user-images.githubusercontent.com/16419202/227760245-6be3ea4e-ba76-4c62-97ba-65ca14064821.png)
