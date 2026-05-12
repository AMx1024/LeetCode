class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        sqrt = math.sqrt(num)
        perfectsquare = abs(sqrt - round(sqrt)) < 1e-5
        return perfectsquare
