class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
                return True
        if x<0 or x%10 == 0:
            return False
        
        rev_x = 0
        n = int(math.log10(x)) + 1
        x = abs(x)

        while rev_x < x:
            rev_x = rev_x*10 + x%10
            x = x//10
        if n%2 == 0 and x == rev_x:
            return True
        elif n%2 != 0 and x == rev_x//10:
            return True
        else:
            return False        
        