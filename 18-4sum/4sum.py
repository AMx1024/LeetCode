class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, i = len(nums), 0
        if n <= 3:
            return []

        res = []
        while i < n-3:
            j = i+1
            while j < n-2:
                l, r = j+1, n-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

                    elif s > target:
                        r -= 1

                    else:
                        l += 1

                j += 1
                while j < n-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < n-3 and nums[i] == nums[i-1]:
                i += 1
        
        return res