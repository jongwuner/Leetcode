### 문제정의
- 연결 리스트의 Head값을 받아서, 리스트 내부의 val값을 Random하게 반환하라. 

### 솔루션
- Class Solution의 init으로 리스트 size와 val값을 조회하면서 저장해두고(O(N)), getRandom()함수로 O(1)에 반환해준다.

### 메모
- Leetcode의 연결리스트 톤앤매너. 이제 거의 잡아가는 중.
### 접근과정
- 이거 ListNode들의 val값 List를 매개변수로 받는 건지, 아니면 또 Head만 받는건지 계속 헷갈렸다. 
  - ListNode들의 val값 List를 받지 않으면... Class Solution의 init에 뭐가 들어가야할 지 몰랐기 때문이다. 
  - 근데 시간복잡도를 보니깐 init이 어떤 역할을 해야할지 느낌이 왔었다. 
