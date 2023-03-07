### 문제정의
- 컴퓨터 n대를 batteries 리스트를 활용하여, 최대한 길게 유지할 수 있는 시간을 출력하라. 배터리 게이지 1당 1분 지속할 수 있다.   

### 솔루션
- 수학문제. 오름차순 정렬된 batteries 리스트를 활용하여, 역순으로 리스트를 조회한다. 이 때, 조회하고 있는 idx의 batteries[idx] 값 만큼, PC n대를 동시에 유지할 수 있는지를 확인한다. 이 때, n대를 동시에 유지할 수 있는 시간은 최소 batteries[idx]일 것이며, n이 낮을 수록, batteries[idx]보다 긴 시간동안 유지할 수도 있다. 만약 여기서 total // n  < batteries[idx] 인 경우에는, 리스트 내에서 현재 조회값보다 더 작은 값과 비교하며, 그 작은 값을 기준으로 n대를 동시에 유지할 수 있는 시간을 계산해야한다. 이때 n -= 1 를 하게 되는데, batteries[idx-1] 값보다 batteries[idx]는 항상 클 수 밖에 없으며, answer가 batteries[idx-1] <= value < batteries[idx]로 결정나더라도, batteries[idx]에는 아무런 지장이 없는 상태가 된다. batteries[0], batteries[1], ... , batteries[idx-2]은 모두 batteries[idx-1]로 값을 만들 수 있는지 확인해야한다. total(batteries[idx]가 제외된) // n (n-=1) 보다 batteries[idx-1]의 값을 비교하면 결국 답을 출력할 수 있다. 

### 메모
- Division의 의미. N/3은 `N//3` + `N//3` + `N//3` + `N%3` 로 구성 되어있다.
- 수학적 추론으로 풀어야한다. 
- 문제 조건이 자꾸 헷갈리는데, i배터리에서, j배터리로 나눠줄 수가 없다. 
- 문제

### 접근과정
- Parametric Search + PQ로 접근
- 내림차순 리스트에서 N만큼 최소값 PQ를 가지고 있다. [value, N-th] 이렇게 가지고 있으면, PQ의 Top과 PQ의 Top+1만 매번 조회할 때, 지금 상태에서 다음 상태까지 어떤 값으로 만들어줘야하는 지 알 수 있다. 
![image](https://user-images.githubusercontent.com/16419202/223330132-c4f96779-843e-4d0a-8b76-6cd0b68a2a0a.png)

- 시행착오하다가 좋은 방법을 발견했다. 
- 오름차순 리스트에서 Total // N의 연산결과와 현재 리스트에서 보고 있는 가장 큰 값을 비교했을 때, 가장 큰 값이 최소 배터리를 지속할 수 있는 시간이다. 만약 가장 큰 값이 안되는 경우, 그 값만큼 지속할 수 없다는 결론을 얻을 수 있다. 
- 그 다음 작은 값으로 조회할 때는 N -= 1의 연산을 해줘야한다. 현재 값을 기준으로 작은 값들이 지금 현재 값으로 만들어질 수 있는지가 중요하다. 
- ex. [12, 15, 15]로 n=2를 만들어야할 때. 이 경우가 사실 [12, 15, 15, 19] N=3으로 문제가 주어질 수 있다. 그런 전제하에 n=2일 경우, 원본 리스트의 마지막 인덱스 19는 애초에 고려할 필요가 없다.  
![image](https://user-images.githubusercontent.com/16419202/223330144-b89006be-123d-4c8a-9484-6e60c10876b6.png)
![image](https://user-images.githubusercontent.com/16419202/223330152-d0cfc10c-ef0b-4f02-8aaa-ab7c8955ff84.png)
![image](https://user-images.githubusercontent.com/16419202/223330159-725ab3b8-e195-46a3-a1a9-3e7d21652982.png)
