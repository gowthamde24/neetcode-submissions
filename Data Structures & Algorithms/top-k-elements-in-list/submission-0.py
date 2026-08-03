class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        freq_buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num]=count.get(num,0)+1
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        res=[]
        for i in range(len(freq_buckets)-1,0,-1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
                
        