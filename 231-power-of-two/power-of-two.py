class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def is_int(n):
            if abs(n - (n//1)) < 1e-10:
                return True
            else:
                return False
        if n <= 0:
            return False
        x = math.log2(n)
        return is_int(x) 
        