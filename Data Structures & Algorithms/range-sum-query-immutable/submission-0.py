class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for num in nums:
            curr+=num
            self.prefix.append(curr)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefix[right]
        leftsum = self.prefix[left-1] if left>0 else 0
        return rightsum - leftsum
        


