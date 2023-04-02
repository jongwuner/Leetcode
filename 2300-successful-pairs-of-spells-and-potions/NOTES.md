### 문제정의
- Potions와 Spell, success 리스트를 입력받았을 때, Potions에다가 Spells를 곱한 값들 중 success보다 높은 값들은 몇개나 있는지를 ans 리스트에 담아서 반환한다.
### 솔루션
- O(Potions.size\*log(Potions.size) + spells.size \* log(Potions.size)). Potions에다가 Spell들을 곱하면 시간초과가 나기 때문에, Success를 Spell들로 나눠서 그 값을 Potions에서 이분탐색으로 찾으면 된다. 
### 기록
- 결국 Parametric Search는 pivot값이랑 postion[mid]값의 방향성이 헷갈린다. 이것만 잘 잡으면 아무런 문제가 없는 문제들이 많이 나온다. 
### 접근과정
- success를 그냥 역으로 줄이면 쉽잖아. 
- ![image](https://user-images.githubusercontent.com/16419202/229359418-65352d0c-5f3b-439d-b956-f1fbdb41ee8c.png)
- ![image](https://user-images.githubusercontent.com/16419202/229359453-4c77bbb4-8abe-4c7f-b409-f97dce8df169.png)
- ![image](https://user-images.githubusercontent.com/16419202/229359459-e3a67489-4485-4ca3-8697-cab2d98b7e81.png)
