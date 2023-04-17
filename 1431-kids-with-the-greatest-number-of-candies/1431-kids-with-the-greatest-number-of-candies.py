class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxval = -1
        for candy in candies:
            maxval = max(maxval, candy)
        for candy in candies:
            if candy + extraCandies >= maxval:
                ans.append(True)
            else:
                ans.append(False)
        return ans