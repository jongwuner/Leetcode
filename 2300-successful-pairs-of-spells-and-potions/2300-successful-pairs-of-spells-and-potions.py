class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions = sorted(potions)

        for spell in spells:
            L = 0
            R = len(potions) - 1
            pivot = success / spell
            tans = len(potions)

            while L <= R:
                mid = (L + R) // 2
                if pivot <= potions[mid]:
                    tans = mid
                    R = mid - 1
                else: # pivot > potions
                    L = mid + 1

            ans.append(len(potions) - tans)

        return ans
