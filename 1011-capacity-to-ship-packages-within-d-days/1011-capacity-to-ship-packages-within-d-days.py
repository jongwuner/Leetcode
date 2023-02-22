class Solution(object):
    def shipWithinDays(self, weights, days):
        L = max(weights)
        R = 25000000
        M = 0

        while(L <= R):
            M = int((L + R) / 2)
            cnt = 1
            sum = 0

            for wei in weights:
                if sum + wei <= M:
                    sum += wei
                else :
                    cnt += 1
                    sum = wei

            if cnt <= days : 
                ans = M
                R = M - 1
            else :
                L = M + 1

        return ans