class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        def TotalHours(piles, k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours

        l, r = 1, max(piles)
        ans = 0
        while l <= r:
            mid = (l+r) // 2
            hours = TotalHours(piles, mid)
            if hours <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans
        