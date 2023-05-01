class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        maxSal = 900
        minSal = int(1e7)
        for ele in salary:
            maxSal = max(maxSal, ele)
            minSal = min(minSal, ele)
            sum += ele
        sum -= (maxSal + minSal)
        return sum / (len(salary) - 2)