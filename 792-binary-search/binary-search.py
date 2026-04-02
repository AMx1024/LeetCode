class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            mid = (l+r) // 2
            s = nums[mid]
            if s == target:
                return mid
            elif s > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1