class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L=0
        max_len=0
        count={}
        

        for R in range(len(s)):
            count[s[R]]=1 + count.get(s[R],0)

            while (R-L+1)-max(count.values())>k:
                count[s[L]]-=1

                L+=1

            max_len = max(max_len,R-L+1)

        return max_len


                
                

            

        return count
            
        