class Solution:
    def specialArray(self, nums: List[int]) -> int:

        l,r = 1,len(nums)

        while l<=r:
            mid = (l + r) >> 1
            cnt = sum(1 for num in nums if num>=mid)

            if cnt == mid:
                return mid
            elif cnt < mid:
                r-=1
            else:
                l+=1
        return -1
        