class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":0, "[": 0, "{": 0, ")": 0, "]": 0, "}": 0}
        for i in range(0, len(s)):
            d[s[i]] += 1
        return d["("] == d[")"] and d["["] == d["]"] and d["{"] == d["}"] and support(self, s)
    def support(self, s) -> bool:
        for i in range(0, len(s)):
            # In progress




