class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = set()
        ans2 = set()
        intersect = set()
        
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    intersect.add(num1)
        
        for num1 in nums1:
            if num1 not in intersect:
                ans1.add(num1)
        
        for num2 in nums2:
            if num2 not in intersect:
                ans2.add(num2)
        
        return [list(ans1), list(ans2)]