class Solution(object):
    def shipWithinDays(self, weights, days):
        L = max(weights) #답이 될 수 있는 후보의 최소값
        R = sum(weights) #답이 될 수 있는 후보의 최대값
        M = 0
        
        # 최대한 효율적으로 (컨베이어의 적재 무게를 최소화하는 Output)

        while(L <= R):
            M = int((L + R) / 2) # 지금 현재 '컨베이어' 의 무게.
            cnt = 1
            sumt = 0

            for wei in weights:
                if sumt + wei <= M: # 12500000
                    sumt += wei
                else :
                    cnt += 1
                    sumt = wei

            if cnt <= days : 
                ans = M
                R = M - 1
            else :
                L = M + 1

        return ans