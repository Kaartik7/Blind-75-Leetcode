class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        n = len(s)
        i = n - 1
        while i >= 0:
            if i < n-1 and dic[s[i]] < dic[s[i + 1]]:
                num = num - dic[s[i]]
            else:
                num = num + dic[s[i]]
            i = i - 1
        return num

