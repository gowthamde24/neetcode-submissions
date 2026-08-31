class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], nums: List[int],pick: List[bool]):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    curr.append(nums[i])
                    pick[i]=True
                    backtrack(curr,nums,pick)
                    curr.pop()
                    pick[i]=False
        backtrack([],nums,[False] * len(nums))
        return res
        
            

            
        