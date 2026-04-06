class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0
        if len(heights) == 2:
            return min(heights[0],heights[1])
        while left < right:
            indDifference = right - left
            minHeight = min(heights[left], heights[right])
            volume = indDifference * minHeight
            if volume > result:
                result = volume
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result