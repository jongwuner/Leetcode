from bisect import bisect_left

class Solution(object):
    def singleNonDuplicate(self, nums):
        lenth = nums.__len__()
        left_idx = tmp_left_idx = 0
        right_idx = tmp_right_idx = lenth - 1

        while(1):
            lenth = right_idx - left_idx + 1
            mid = int((left_idx + right_idx) / 2)
            tmp_left_idx = bisect_left(nums, nums[mid])
            tmp_right_idx = tmp_left_idx + 1

            if lenth == 1 or nums[tmp_left_idx] != nums[tmp_right_idx]:
                left_idx = tmp_left_idx
                break

            elif ((tmp_left_idx - 1) - left_idx + 1) % 2 == 1: #왼쪽에 홀수?
                right_idx = tmp_left_idx - 1

            elif (right_idx - (tmp_right_idx + 1) + 1) % 2 == 1: #오른쪽에 홀수?
                left_idx = tmp_right_idx + 1
        
        return nums[left_idx]
