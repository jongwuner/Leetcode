### 문제정의
- [단방향 링크드리스트에서 사이클이 시작되는 지점 찾고, ListNode를 반환하라.](https://leetcode.com/problems/linked-list-cycle-ii/)
### 솔루션
- 링크드리스트를 선형 탐색하면서, 기존에 방문했던 고유 주소값을 2번째 방문하게 되는 nextNode를 반환한다. 
### 메모
- Python의 주소값 개념(C/C++의 Pointer)이 없어서 오래걸렸다. 
  - [ID함수](https://wjunsea.tistory.com/82)
- 그래프의 Cycle 판별 알고리즘을 알아야하나 싶었다. 
  - [사이클 판별 알고리즘 1, 유니온 파인드 활용](https://www.google.com/search?q=%EC%82%AC%EC%9D%B4%ED%81%B4+%EA%B2%80%EC%82%AC+%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98&sxsrf=AJOqlzXKjk0b1PZ1gELakwMlFoSoOs-27Q%3A1678347008438&ei=AIsJZLimGp-12roP5YC8oA4&ved=0ahUKEwi4pv3pqc79AhWfmlYBHWUAD-QQ4dUDCA8&uact=5&oq=%EC%82%AC%EC%9D%B4%ED%81%B4+%EA%B2%80%EC%82%AC+%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzoKCAAQRxDWBBCwAzoLCAAQgAQQsQMQgwE6EAgAEIAEEBQQhwIQsQMQgwE6BQgAEIAEOgoIABCABBAUEIcCOgcIIxDqAhAnOhEILhCABBCxAxCDARDHARDRAzoECAAQAzoLCC4QgAQQsQMQgwE6BAgAEEM6CAguEIAEELEDOggIABCABBCxAzoFCC4QgAQ6BAgAEB5KBAhBGABQxQRYoSpgiitoBnABeAaAAa0CiAG_NZIBCTAuMjIuMTEuMZgBAKABAbABCsgBCsABAQ&sclient=gws-wiz-serp)
  - [사이클 판별 알고리즘 2, DFS](https://velog.io/@since-1994/%EA%B7%B8%EB%9E%98%ED%94%84-Detection-cycle-%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%B0%BE%EA%B8%B0)
  - [사이클 판별 알고리즘 3, 유향 그래프](https://deep-learning-study.tistory.com/582)
  - [사이클 판별 알고리즘 4, 무향 그래프](https://deep-learning-study.tistory.com/584)
- 토끼와 거북이 알고리즘 
  - 해당 리스트에서 사이클이 존재할 경우, 처음 시작지점(Head) 이후, 토끼(+2칸), 거북이(+1칸)는 반드시 사이클 구간의 어디에선가 만나게 된다. (사이클의 시작점, Tail이 아닐 수 있음) 그 이후, 거북이는 Head로 이동시키고, 거북이와 토끼가 사이클 내부에서 만난 지점에 위치시킨다. 토끼와 거북이가 현 위치에서 +1칸씩 이동시켰을 때 반드시 만날 수 밖에 없는 이유는 현 위치 8번 인덱스에서 만났기 때문[0-index]이다. 8번 인덱스에서 만나게 된 상황은 토끼는 2의 배수만큼 움직였고, 거북이는 1의 배수만큼 움직였을 때 만났던 지점이기 때문에, 토끼의 속도 2에서 1로 줄더라도 8번 인덱스는 거북이가 Head로 돌아가더라도, 무조건 다시 만날 수 밖에 없는 위치가 된다. 토끼의 속도가 1로 거북이와 같아졌기 때문에, 사이클 내부로 진입하게 되는 순간부터 토끼와 거북이는 계속 같은 위치에 있게 된다. 토끼가 속도 2일 때, 8번 인덱스에서 만났으며, 토끼가 속도 1일 때도 8번 인덱스에서 다시 만나게 된다. 이것으로 미뤄볼 때, 사이클 내부 구간에서는 계속 같이 움직이게 되며, 거북이가 Head로 돌아가고 나서 처음 다시 만나게 되는 지점을 사이클이 시작되는 지점이라고 정의할 수 있다. 
  - ↓ 이거 두번째 다시 만날 때, 빨간색 부분 오류가 있음. 
  - ![image](https://user-images.githubusercontent.com/16419202/224460819-c9b0615c-1399-4bed-b1a9-524c43d2eb83.png)


### 접근과정
- Python의 주소값 개념(C/C++의 Pointer)이 없어서 오래걸렸다. 
- 유니크한 고유 주소값을 기준으로 Visited Set을 활용하면 될 것 같았다. 
- 그래프의 Cycle 판별 알고리즘을 알아야하나 싶었다. 다음 노드는 항상 1개씩이기 떄문에 DFS을 활용한 사이클 판별 알고리즘은 활용할 필요가 없다고 생각했다. (이미 활용했을지도 모르지만 간소화된 형태일 수도 있다.)
- 문제 조건이 잘못된 건 아닌지 생각해봤고, 토론했다. 
- 
![image](https://user-images.githubusercontent.com/16419202/223955764-f57ec1b2-c5c1-495f-84a8-91e2b442db39.png)

