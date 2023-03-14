### 문제정의
- 루트에서 리프노드까지 경로 순으로 숫자로 된 문자열을 구성하여, 모두 더한 값을 반환하라.   
### 솔루션 
- 후위탐색(PostOrder)으로 Subtree의 루트에 리스트를 재귀적으로 반환하면서, 해당 루트에서는 'root.val인 문자' + "반환된 문자열" 연산을 해준다.
### 기록
- 0의 값을 사용할 때는 문자열이 편리하다는 것.
```python
def getDigits(num):
  cnt = 0
  while num > 0:
    num //= 10 # /로 하면 float형이 된다는 것을 명심.
    cnt += 1
  # num의 자리수 
```
- string에 0에다가 삽입할 때는 `+` 연산자를 활용하자. insert 말고, 사이에 넣어야할 때는 [a:b] 연산을 활용하자. 
- `for a,b in enumerate()` 에서 a가 idx고, b가 element이다.
### 접근과정
- preOrder인지, postOrder인지 헷갈렸다. 
