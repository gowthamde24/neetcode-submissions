class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        
        for i in range(len(nums)-k+1):
            maximum = nums[i]
            for j in range(i,i+k):
                maximum = max(maximum,nums[j])

            res.append(maximum)
        return res



        