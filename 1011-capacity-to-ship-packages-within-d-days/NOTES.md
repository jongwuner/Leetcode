![image](https://user-images.githubusercontent.com/16419202/220512289-8a172c3d-9aec-425c-a03a-7fcc39a231e9.png)
![image](https://user-images.githubusercontent.com/16419202/220512373-00d662a3-c6b9-46d8-8d58-9e80d7b55bd3.png)

최대값들의 최소값을 묻는 문항이었다. 이게 박정흠 교수님께 배웠을 때, 명확한 용어가 있었는데 기억이 잘안나네.
DP에 강하게 꽃혀있었는데, 시간복잡도를 보니까 days * weight.length 여서, 1억이 초과하는 수치였다. 그래서 생각을 하다보니까, wei[i]<=500인 것을 발견했다. 좀 이상해서 확인을 해보니까, Output의 최댓값이 500 \* 5 \* 10^4인것을 발견했다. Parametric Search가 아닐까 하는 생각이 들었고, 시간복잡도를 확인해보니까 충분히 통과될 것 같았다. 

Parametric Search에서 답이 맞는지를 검증하는 과정에 구현이 항상 버겁게 느껴진다.
그리고 답이 되는 후보. Answer들이 뭔지를 검증하는 로직에서 항상 시간이 오래걸린다. 
