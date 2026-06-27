from itertools import combinations
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums) + 1):
            for combo in combinations(nums, i):
                res.add(combo)
        return [list(subset) for subset in sorted(res)]