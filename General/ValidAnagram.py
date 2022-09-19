class Solution:
    """
        All alphabets of in s should be in t, equal no of times
    """
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = dict()
        d2 = dict()
        for i in s:
            d1[i] = 0
        for i in s:
            d1[i] = d1[i] + 1
        for i in t:
            d2[i] = 0
        for i in t:
            d2[i] = d2[i] + 1
        for i in s:
            if i not in d2 or d1[i] != d2[i]:
                return False

        return True
