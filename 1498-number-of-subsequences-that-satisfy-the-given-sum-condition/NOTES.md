![image](https://user-images.githubusercontent.com/16419202/236643596-339e1cb2-2027-4af7-a196-e0934d09b115.png)


### 문제정의
- nums 리스트를 입력받았을 때, subList 상에서 min값과 max값의 합이 target 값보다 작거나 같은 모든 subList의 수를 반환하라.  
### 솔루션
- O(NlogN). Binary Search + Math.
- List 를 정렬한 후에, List에 루프를 돌리면서, element가 가리키는 값에 대해 target값보다 작거나 같은 값중 최대값을 binary search로 찾을 수 있다. 이 때, 리스트가 정렬되어있으므로, L값과 R값의 사이에 있는 값들은 모두 SubList에 속할 수 있는 요소가 된다. [L, R] 이 정의된 구간에서 subList는 구간의 길이에 대해서, 2 ** (LIdx - RIdx) 값을 가진다. (등비수열의 합) 
### 기록
- 이 문제는 Binary search 대신 투포인터로도 풀 수 있다. 
- 등비수열의 합 공식

### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/236644056-43899324-d342-4bd0-afdd-0e2bb0902cf7.png)
- ![image](https://user-images.githubusercontent.com/16419202/236644063-44285e8b-5d6d-426f-8e37-d5b50e4d4783.png)
- ![image](https://user-images.githubusercontent.com/16419202/236644068-8bef9f3b-10b4-4d4a-8d7d-b33d2890e5e8.png)
