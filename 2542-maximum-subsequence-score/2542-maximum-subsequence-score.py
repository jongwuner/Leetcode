class Solution(object):
    def maxScore(self, nums1, nums2, k):

        N = nums1.__len__()
        sum = 0

        pair_list = []
        minHeap = []

        for i in range (N):
            pair_list.append([nums2[i], nums1[i]])

        pair_list.sort(reverse=True)
        answer = int(-10e5)

        for i in range (N):
            n1 = pair_list[i][1]
            n2 = pair_list[i][0]
            if i < k - 1:
                sum += n1
                heappush(minHeap, n1)
            else:
                heap_root = minHeap[0] if minHeap.__len__() > 0 else 0  

                if k == 1 and i == 0:
                    answer = n1 * n2
                else:
                    answer = max(answer, (n1 + sum) * n2)    
                    if sum < sum - heap_root + n1:
                        sum += n1
                        heappush(minHeap, n1)
                        sum -= heappop(minHeap)

        return answer