class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(min(nums), max(nums)):
            if i not in nums:
                out.append(i)
        return out
