class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people = sorted(people)
        L = 0
        R = len(people) - 1

        while L <= R:
            if L == R and people[L] <= limit:
                ans += 1
                L += 1
            elif people[L] + people[R] > limit:
                R -= 1
                ans += 1
            elif people[L] + people[R] <= limit:
                R -= 1
                L += 1
                ans += 1

        return ans