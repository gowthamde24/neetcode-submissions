class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        schar = {}
        tchar = {}

        for i in range(len(s)):
            schar[s[i]]= schar.get(s[i],0)+1
            tchar[t[i]]= tchar.get(t[i],0)+1
        
        return schar == tchar
        