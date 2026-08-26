class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        res = 0

        currsum = sum(arr[:k-1])

        for L in range(len(arr)-k+1):
            currsum += arr[L + k - 1]
            if (currsum / k)>= threshold:
                res += 1
            currsum -= arr[L]

        return res
        