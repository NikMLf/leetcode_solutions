class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_3 = nums1 + nums2
        nums_3.sort()
        if len(nums_3) % 2:
            return float(nums_3[len(nums_3)//2])
        else:
            return float(nums_3[len(nums_3)//2 - 1] + nums_3[len(nums_3)//2])/2