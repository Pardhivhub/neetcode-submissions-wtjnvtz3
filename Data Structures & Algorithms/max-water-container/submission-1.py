class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        left=0
        right=len(heights)-1
        while right>left:
            width=right-left
            height=min(heights[left],heights[right])
            area=width*height
            max_area=max(area,max_area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return max_area





        