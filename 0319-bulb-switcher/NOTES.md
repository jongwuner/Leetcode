![image](https://user-images.githubusercontent.com/16419202/234837271-4bb3ea4e-e863-4f6c-a8de-5a1b2cfe78b8.png)

### 문제정의
- n개의 전구가 있으며, n개의 라운드가 있다. 1번째 라운드에는 모든 전구가 켜져있다. n번째 라운드에는 n번째 마다의 전구를 toggle한다. n라운드를 마치고 켜져있는 전구의 수를 반환하라.  
### 솔루션
- O(1). sqrt(Math). i번째 전구는 i의 약수 라운드 때, toggle을 하게 된다. 처음엔 항상 켜져있기 때문에 홀수번 toggle을 하면 켜져있게 되고, 짝수번 toggle을 하면 꺼지게 된다. 결국 켜져있는 전구의 수를 묻는 문제이기 때문에, 홀수번 toggle을 하는 i들이 몇개인지를 찾는 문제다. 홀수번 toggle이라는 것은 약수가 홀수개 라는 것을 의미하며, 약수가 홀수개는 완전제곱수의 특징이다. 결국 n을 입력받았을 때, n과 가장 가까운 완전제곱수가 무엇인지를 물어보는 문제와 같아진다.  
### 기록
- DP로 접근했다가 수학으로 접근하는 과정 괜찮았다. 풀이과정에 만족한다. 
### 접근과정
- ![image](https://user-images.githubusercontent.com/16419202/234837371-8107ea93-c768-47d3-a9f8-76964d6dba62.png)
- ![image](https://user-images.githubusercontent.com/16419202/234837389-eadcbf5b-6d79-45aa-b929-43d4c1b0107c.png)
