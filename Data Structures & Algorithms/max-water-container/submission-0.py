class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            new_area = (r-l)*min(heights[l],heights[r])
            if new_area > area:
                area = new_area
            elif heights[l] < heights[r]:
                l+=1
            else: 
                r-=1
        
        return area


            
            

        