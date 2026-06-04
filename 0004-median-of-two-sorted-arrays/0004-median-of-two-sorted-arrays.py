class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=nums1.extend(nums2)
        b=nums1.sort()
        n = len(nums1)
        if n%2 != 0:
            half = -(-n//2)
            return nums1[half-1]
        else:
            half = n//2
            med = (nums1[half]+nums1[half-1])/2
            return med