class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = []
        t_char = []

        for i in s:
            s_char.append(i)

        for j in t:
            t_char.append(j)

        s_char.sort()
        t_char.sort()

        if s_char == t_char:
            return True
        return False
        