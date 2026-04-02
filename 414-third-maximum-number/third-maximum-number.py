class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = 0
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            elif num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num

        return max3 if max3 != float("-inf") else max1

        
