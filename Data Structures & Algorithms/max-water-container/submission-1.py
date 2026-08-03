class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area=0
        l,r=0,len(height)-1

        while l<r:

            width = r-l
            curr_height = min(height[l],height[r])
            cal_area = width * curr_height
            max_area = max(max_area, cal_area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area

            
        