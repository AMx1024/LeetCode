class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r, ans_l = 0, n-1, -1

        while l <= r:
            mid = (l+r) // 2
            s = nums[mid]
            if s == target:
                ans_l = mid
                r = mid - 1
            elif s > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r, ans_r = 0, n-1, -1

        while l <= r:
            mid = (l+r) // 2
            s = nums[mid]
            if s == target:
                ans_r = mid
                l = mid + 1
            elif s > target:
                r = mid - 1
            else:
                l = mid + 1

        return [ans_l, ans_r]