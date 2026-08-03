class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char=[]
        t_char=[]

        for i in s:
            s_char.append(i)

        for j in t:
            t_char.append(j)

        x=sorted(s_char)
        y=sorted(t_char)

        if x == y:
            return True

        else:
            return False

        