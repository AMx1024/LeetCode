class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        sum_n = int(n*(n+1)/2)
        return sum_n - sum_nums