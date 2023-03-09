### 문제정의
- 단방향 링크드리스트에서 사이클이 시작되는 지점 찾고, ListNode를 반환하라. 
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
### 접근과정
- Python의 주소값 개념(C/C++의 Pointer)이 없어서 오래걸렸다. 
- 유니크한 고유 주소값을 기준으로 Visited Set을 활용하면 될 것 같았다. 
- 그래프의 Cycle 판별 알고리즘을 알아야하나 싶었다. 
![image](https://user-images.githubusercontent.com/16419202/223955764-f57ec1b2-c5c1-495f-84a8-91e2b442db39.png)

