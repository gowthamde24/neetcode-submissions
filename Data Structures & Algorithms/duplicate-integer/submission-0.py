class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasnums = set(nums)
        return len(hasnums)!=len(nums)