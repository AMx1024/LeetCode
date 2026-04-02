class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = 0, 0
        n1, n2 = float("-inf"), float("-inf")

        for num in nums:
            if c1 == 0 and num != n2:
                n1 = num
                c1 = 1
            elif c2 == 0 and num != n1:
                n2 = num
                c2 = 1
            elif num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        c1, c2 = 0, 0

        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
        
        n = len(nums)
        minimum = n//3 + 1

        if c1 >= minimum and c2 >= minimum:
            return [n1, n2]
        elif c1 >= minimum and c2 < minimum:
            return [n1]
        elif c1 < minimum and c2 >= minimum:
            return [n2]
        else:
            return []
