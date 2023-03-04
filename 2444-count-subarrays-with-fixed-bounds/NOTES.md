### 문제정의
- int로 구성된 리스트와 minK, maxK값을 받아서, minK값이 최소값이며, maxK값이 최댓값인 subarray의 개수를 구하라. 단, subarray는 원본 리스트의 연속성을 유지해야한다. 

### 솔루션
- minK과 maxK의 범위에 벗어나는 인덱스들을 체크하여 제외하며 카운팅한다. 슬라이딩 윈도우. O(N)

### 메모
- 이 문제는 최신 maxK, minK값만 고려하기 때문에 Queue 자료구조는 필요가 없음. 
  - Queue : index. 탐색 순서 보존이 중요. (현재 조회하고 있는 인덱스와의 관계를 고려해서 문제가 많이 나옴.)
  - Priority Queue : Value. 값의 크기 순이 중요. (현재 조회하고 있는 인덱스와의 관계를 고려해서 문제가 많이 나옴.)
- 모노톤 큐(Monotone Queue)라는 것에 대해서 공부해봐야겠다. https://stonejjun.tistory.com/126 

### 접근과정
- DP인지를 접근해봤는데, 공간복잡도 O(N^2)였고, 시간복잡도 또한 O(N^2)였는데, 문제 조건을 고려했을 때 불가능했다.  
![image](https://user-images.githubusercontent.com/16419202/222871369-2139f3b8-dfbd-4c49-a56e-cf9eca4c54db.png)

- 문제를 잘못 읽고, 중복조합으로 해결하려고 했었다. minK, maxK으로 주어지는 값이 항상 Array에 있는 값으로 생각했다. 
![image](https://user-images.githubusercontent.com/16419202/222871380-34d06b54-ddae-491d-8277-4f88930c7aa6.png)

- Segment Tree를 생각했는데, 이것도 답이 아니었다. 답이 아닌 이유는 [i, j] 인덱스 범위 내에서는 이것이 문제 조건에 유효한 범위인지(minK, maxK가 subArray에서 성립되는지)를 알 수 있지만, [0, i], [j, N] 도 확인을 해야한다. 그리고 심지어 i-1, j+1 씩 연산하면서 구간을 늘려가야했기 때문에 이건 절대 세그먼트트리일 수가 없다고 생각했다. 
![image](https://user-images.githubusercontent.com/16419202/222871391-d55ebe87-c24b-4b04-ac0a-6f24e69a3958.png)

- nums[i] <= 10^6 인것을 보고, nums[i]의 value값으로 자료구조를 만들어야 하나 생각했었다. (해시테이블 or 선형리스트) 하지만, 결과적으로 Segmen Tree에서 막혔던 문제들이 해결되지 않았다. 
![image](https://user-images.githubusercontent.com/16419202/222871445-760139a1-4195-4f30-b7b8-bd4f26d43345.png)

- 그래서 슬라이딩 윈도우를 한번 생각하게 되었는데, 범위 내에 있는 모든 구간의 개수를 구하는 것이니까, 범위 바깥에 있는 것들을 제외하고 모두 센다고 생각해봤다. 
- outIdx라는 것으로 범위 바깥에 있는 값들 중 최신 idx를 가리키게 하고, maxK와 minK를 가리키는 인덱스들을 2개 본다. [maxK, minK] or [minK, maxK] 내에서는 outIdx가 존재하지 않아야하며, min(maxK, minK)와 outIdx의 길이, 그리고 내가 현재 조회하고 있는 idx가 max(maxK,minK)와 멀어지는 만큼, ans에 Subarray 개수가 더해진다. 
![image](https://user-images.githubusercontent.com/16419202/222871453-23100225-9917-47be-a490-9e8bbff60a09.png)


