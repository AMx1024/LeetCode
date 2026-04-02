class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # sort and initialise result
        nums.sort()
        res = []
        n = len(nums)

        # Start iterating from 0 to (n-1)
        for i in range(n-2):

            # if curr_i == prev_i then skip to prevent duplicates in result
            if i != 0:
                if nums[i] == nums[i-1]:
                    continue

            # Start 2 pointer from (i+1) and (n-1)
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                # if s == 0 append result. Increase j, decrease k till they are unique to skip duplicates
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
                # if s!= 0 then increase or decrease the 2 pointers based on s
                elif s > 0:
                    k -= 1

                else:
                    j += 1

        return res
                    

        