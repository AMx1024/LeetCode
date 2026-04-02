class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n-1
        area_max = 0
        while i < j:
            area_curr = (j-i) * min(height[i], height[j])
            if area_curr > area_max:
                area_max = area_curr
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1
        return area_max

