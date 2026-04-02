class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        if n == 0 or n == 1:
            return n
        for i in range(n-1):
            a, b = b, a+b
        return b