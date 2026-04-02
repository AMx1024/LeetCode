class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        i, j = 2, 2
        while i < n:
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
  