class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ans = []
        count = Counter(nums)
        for i in range(k):
            top = max(count, key = count.get)
            ans.append(top)
            del count[top]
        return ans