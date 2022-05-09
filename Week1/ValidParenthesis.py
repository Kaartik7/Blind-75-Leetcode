class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        l1 = ["(", "{", "["]
        l2 = [")", "}", "]"]
        stack = []
        for ch in s:
            if ch in l1:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if ch == d[stack.pop()]:
                        continue
                    else:
                        return False
        return len(stack) == 0






