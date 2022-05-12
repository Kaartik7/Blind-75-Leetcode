class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for i in s:
            if i.isalpha() or i.isalnum():
                lst.append(i.lower())
        if len(lst) == 0:
            return True
        s = 0
        l = len(lst) - 1
        while s != l:
            if s > l:
                return True
            elif lst[s] != lst[l]:
                return False
            else:
                s = s + 1
                l = l - 1
        return True

