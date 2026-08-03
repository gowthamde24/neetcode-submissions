class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R=0,len(heights)-1
        max_area = 0
        while L < R:
            width = R-L
            current_height = min(heights[L],heights[R])
            current_area = width * current_height

            max_area = max(max_area, current_area)

            if heights[L] < heights[R]:
                L+=1

            else:
                R-=1
        return max_area


        