from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {"a":".-", "b": "-...", "c": "-.-.", "d": "-..", "e":".", "f":"..-.", "g": "--.",
             "h":"....", "i":"..", "j": ".---", "k":"-.-", "l": ".-..", "m": "--",
             "n":"-.", "o": "---", "p":".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
             "u":"..-", "v":"...-", "w": ".--", "x": "-..-", "y": "-.--",
             "z":"--.."}
        lst = []
        for word in words:
            morse = ""
            for i in word:
                morse = morse + d[i]
            if morse not in lst:
                lst.append(morse)
        return len(lst)



