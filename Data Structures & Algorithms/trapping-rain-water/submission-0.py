class Solution:
    def trap(self, height: List[int]) -> int:
        temp_left = [height[0]]
        temp_right = [height[-1]]
        result = 0
        for i in range(len(height)-1):
            temp_left.append(max(height[i+1], temp_left[i]))
        for i in range(len(height)-1):
            temp_right.append(max(height[-i-1], temp_right[i]))
        temp_right = temp_right[::-1]
        for i in range(len(height)):
            temp = min(temp_left[i], temp_right[i]) - height[i]
            if temp <= 0:
                result += 0
            else:
                result += temp
        return result