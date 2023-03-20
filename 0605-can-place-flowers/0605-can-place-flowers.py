class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, ele in enumerate(flowerbed):
            if ele == 1:
                if i - 1 >= 0:
                    flowerbed[i - 1] = -1
                if i + 1 <= len(flowerbed) - 1:
                    flowerbed[i + 1] = -1

        ans = 0
        cnt = 0

        for i, ele in enumerate(flowerbed):
            if ele == -1:
                ans += max((cnt-1) // 2 + 1, 0)
                cnt = 0
            elif ele == 0:
                cnt += 1

        ans += max((cnt-1) // 2 + 1, 0)
        return n <= ans