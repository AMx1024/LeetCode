class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x

        while l <= r:
            mid = (l+r) // 2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
