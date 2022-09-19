class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = "[.]"
        lst = list(address)
        x = ""
        for i in range(0, len(lst)):
            if lst[i] == ".":
                lst.pop(i)
                lst.insert(i, s)
            x = x + lst[i]
        return x
