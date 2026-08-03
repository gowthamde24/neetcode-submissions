class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""

        count_t={}
        for char in t:
            count_t[char]=1+count_t.get(char,0)
        
        window={}
        have,need=0,len(count_t)

        res,reslen = [-1,-1],float("infinity")

        L=0
        for R in range(len(s)):
            char = s[R]
            window[char]=1+window.get(char,0)


            if char in count_t and window[char]==count_t[char]:
                have+=1

            while have==need:
                if(R-L+1)<reslen:
                    res=[L,R]
                    reslen=R-L+1

                left_char=s[L]
                window[left_char]-=1

                if left_char in count_t and window[left_char]<count_t[left_char]:
                    have-=1
                L+=1

        left,right=res
        return s[left:right+1] if reslen != float("infinity") else ""



        
        





        

            
        