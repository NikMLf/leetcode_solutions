class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = {}
        key_max = nums[0]
        for i in nums:
            if n.get(i) is None:
                n.update({i : 1})
            else:
                n[i] += 1
        for i in n.keys():
            if n[i] > n[key_max]:
                key_max = i

        return key_max