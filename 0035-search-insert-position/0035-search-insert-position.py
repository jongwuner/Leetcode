from bisect import bisect_left, bisect_right

class Solution(object):
    def searchInsert(self, nums, target):
        return bisect_left(nums, target)