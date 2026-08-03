class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0
            if cache[i]!=-1:
                return cache[i]
            skip = dfs(i+1)
            rob = nums[i]+dfs(i+2)
            cache[i]= max(rob,skip)

            return cache[i]

        return dfs(0)

            
        