class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)

        l=0
        r=n-1

        while l<=r:
            mid = (l + (r-l)//2)

            if nums[mid]<target:
                l+=1
            elif nums[mid]>target:
                r-=1

            else:
                nums[mid]==target
                return mid

        return -1
        