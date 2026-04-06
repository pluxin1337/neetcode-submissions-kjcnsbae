class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = sorted(set(nums))
        temp = 1
        temp_max = 1
        if len(result) == 0:
            return 0
        for i in range(len(result)-1):
            if result[i+1] - result[i] == 1:
                temp += 1
            else:
                if temp >= temp_max:
                    temp_max = temp
                temp = 1
        return max(temp, temp_max)