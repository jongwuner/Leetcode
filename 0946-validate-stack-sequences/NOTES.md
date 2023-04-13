![image](https://user-images.githubusercontent.com/16419202/231803147-f90db035-7d25-4a77-8636-c0a034a87135.png)
![image](https://user-images.githubusercontent.com/16419202/231805403-86d24ce3-53e8-4899-90f3-91bdf450d321.png)
- 리트코드 중에 이 만큼 계속 실수를 반복했던 적이 있나 싶을정도로 ㅋㅋㅋ 

### 문제정의
- Push/Pop List가 주어질 때, 가능한 Stack 구성인지 True/False를 반환하라. 

### 솔루션
- O(N). Hashmap + Stack 활용. 리스트요소와 인덱스를 (key, value)로 갖는 hashmap을 활용하여, popItem이 stack의 top이 될때까지 push를 한다. 현재까지의 pushList의 index보다 큰 값이 들어왔을 경우, 여러번의 Push가 진행되며, 현재까지의 pustList의 index보다 작은 값이 들어왔을 때, pop을 계속해주면 되는데, top값과 popList의 현재 인덱스가 가리키고 있는 값이 다를 경우, False를 반환하면 된다. 

### 기록
- Hashmap을 쓸 때, 구현 전에 제대로 정의하지 않으면 너무 헷갈리는 상황이 생긴다. 뭔가 계~속 헷갈리는 상황이 생김.
- Stack을 활용하는 상황에 대해서 아직 익숙치 않은 것 같다. 

### 접근과정
- 완전 다른 알고리즘으로 접근했었다.
  - stack을 쓰지 않고, 그냥 가장 큰 index가 등장했을 때는 그냥가고, 그보다 작은 index일 때는 오름차순이 등장하면 False라고 했는데, 반례가 있더라. 내림차순이어도 나와야할게 나오지 않으면 False인 경우도 있었는데, 아예 간과하고 있었다. 
  - ```python
    from typing import List

    class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        hashmap = {}
    
        for i, key in enumerate(pushed):
            hashmap[key] = i
            
        maxVal = -1
        i = 0
        while i < len(popped):
            nowKey = popped[i]
            if nowKey not in hashmap:
                return False
            
            nowIdx = hashmap[nowKey]
            
            if maxVal < nowIdx:
                maxVal = nowIdx
            elif i > 0 and prevIdx < nowIdx:
                return False
            
            i += 1
            prevIdx = nowIdx
            del hashmap[nowKey]

        if len(hashmap) > 0:
            return False                    
        return True
        
    sol = Solution()
    ans = sol.validateStackSequences(pushed = [1,2,3,4,5,6,7,8,9,10,11,12,13], popped = [7,6,5,9,12,13,11,10,8,4,3,2,1])
    print(ans)
    ```
