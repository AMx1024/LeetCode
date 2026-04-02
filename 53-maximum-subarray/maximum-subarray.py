class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo
        curr_sum, max_sum = 0, float("-inf")
        for num in nums:
            curr_sum += num
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum