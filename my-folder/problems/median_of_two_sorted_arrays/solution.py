class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        tot_len = len(nums1) + len(nums2)
        
        l, r = 0, len(nums1)-1
        
        while True:
            
            m1 = (l + r) // 2
            m2 = (tot_len // 2) - m1 - 2
            
            left_1  = nums1[m1] if m1 >= 0 else float("-infinity")
            left_2  = nums2[m2] if m2 >= 0 else float("-infinity")

            right_1 = nums1[m1 + 1] if (m1 + 1) < len(nums1) else float("infinity")
            right_2 = nums2[m2 + 1] if (m2 + 1) < len(nums2) else float("infinity")
            
            if left_1 > right_2:
                r = m1-1
            
            elif left_2 > right_1:
                l = m1+1

            else:        
                if tot_len % 2 == 0:
                    return (max(left_1, left_2) + min(right_1, right_2)) / 2

                return min(right_1, right_2)