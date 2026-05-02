class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n-2
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        while l <= r:
            m = (l+r) // 2
            if nums[m-1] != nums[m] and nums[m] != nums[m+1]:
                return nums[m]

            elif (m % 2 == 0 and nums[m] == nums[m+1]) or (m % 2 and nums[m] == nums[m-1]):
                l = m + 1

            else:
                r = m