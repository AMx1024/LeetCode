class Solution:
    def reverse(self, x: int) -> int:
        rev_x = 0
        if x == 0:
            return x
        elif x > 0:
            a = 1
        else:
            a = -1
        x = abs(x)
        while x > 0:
            rev_x = rev_x * 10 + x % 10
            x = x // 10
        if (-1 * 2**31 > (rev_x * a)) or ((rev_x * a) > 2**31 - 1):
            return 0
        else:
            return rev_x * a
