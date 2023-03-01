class Solution(object):
    def sortArray(self, nums):
        def merge_sort(nums):
            if nums.__len__() == 1:
                return nums

            def split_list(list):
                length = list.__len__()
                half = list.__len__() // 2
                return list[:half], list[half:]

            newList = []
            nums1, nums2 = split_list(nums)

            nums1 = merge_sort(nums1)
            nums1_length = nums1.__len__()
            nums2 = merge_sort(nums2)
            nums2_length = nums2.__len__()

            ptr1 = ptr2 = 0

            while ptr1 < nums1_length or ptr2 < nums2_length:
                if ptr1 == nums1_length:
                    newList.append(nums2[ptr2])
                    ptr2 += 1
                elif ptr2 == nums2_length:
                    newList.append(nums1[ptr1])
                    ptr1 += 1
                elif nums1[ptr1] < nums2[ptr2]:
                     newList.append(nums1[ptr1])
                     ptr1 += 1
                else : 
                    newList.append(nums2[ptr2])
                    ptr2 += 1
            return newList
        return merge_sort(nums)