class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev = 0
            temp = x
            while temp != 0:
                d = temp % 10
                rev = (rev * 10) + d
                temp = temp // 10
            return rev == x

