class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        ans = n
        while l <= r:
            mid = (l+r) // 2
            s = nums[mid]
            if s >= target:
                ans = mid
                r = mid-1
            else:
                l = mid + 1

        return ans